# coding: utf-8

from django.conf import settings
from django.contrib import auth
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, Http404

from datetime import date
from xlwt import Workbook, easyxf, Formula, XFStyle, Font

from interface.models import Cuerpo, MaterialMayor, AdquisicionCompraMaterialMayor, AdquisicionDonacionMaterialMayor, TipoEventoHojaVidaMaterialMayor, EventoHojaVidaMaterialMayor, Rol, AsignacionPatenteMaterialMayor, UsoMaterialMayor
from interface.forms import FormularioAdquisicionCompraMaterialMayor, FormularioAdquisicionDonacionMaterialMayor, MaterialMayorSearchForm, FormularioDarDeAltaMaterialMayor, FormularioAsignacionCuerpoMaterialMayor, FormularioHojaVidaAsignacionCuerpoMaterialMayor, FormularioAsignacionCompaniaMaterialMayor, FormularioHojaVidaAsignacionCompaniaMaterialMayor, FormularioAsignacionPatenteMaterialMayor, FormularioHojaVidaAsignacionPatenteMaterialMayor
from django.http import HttpResponseRedirect
from interface.utils import convert_camelcase_to_lowercase, log
from django.contrib.auth.decorators import login_required

from authentication import authorize, authorize_material_mayor_access

@login_required
def logout(request):
    # Vista de cierre de sesión, todo boilerplate
    request.flash['success'] = 'Ha salido exitosamente del sistema'
    log('User %s logged out' % request.user.username)
    auth.logout(request)
    return redirect('login')

@login_required
def index(request):
    # Vista de la página de inicio para cualquier usuario logueado
    return render_to_response('staff/index.html', {}, 
                                context_instance=RequestContext(request))
                                
def _adquisicion_material_mayor(request, FormularioAdquisicion, template):
    # Método genérico que procesa el agregado de un nuevo material mayor mediante
    # compra o donación.
    # Parámetros:
    #   FormularioAdquisicion: Clase del formulario seleccionado por el usuario, de tipo
    #       FormularioAdquisicionMaterialMayor e instanciado por 
    #       FormularioAdquisicionCompraMaterialMayor o FormularioAdquisicionDonacionMaterialMayor
    if request.method == 'POST':
        # Los formularios deben recibir el usuario en su constructor porque al desplegarse pueden
        # mostrar íconos para agregar opciones a sus combobox, pero esa posibilidad sólo está disponible
        # para el staff de la JNBC, no para los usuarios de cuerpos bomberiles.
        form = FormularioDarDeAltaMaterialMayor(request.POST, request.FILES, user=request.user)
        form_adquisicion = FormularioAdquisicion(request.POST, request.FILES, user=request.user)
        if form.is_valid() and form_adquisicion.is_valid():
            data_form = FormularioDarDeAltaMaterialMayor(request.POST, user=request.user)
            data_form.is_valid()
            material_mayor_data = data_form.instance
            material_mayor_data.save()
            
            form = FormularioDarDeAltaMaterialMayor(request.POST, request.FILES, user=request.user, instance=material_mayor_data)
            form.is_valid()
            
            material_mayor = form.instance
            
            adquisicion = form_adquisicion.get_instance(request.user)
            material_mayor.save()
            
            adquisicion.materialmayor = material_mayor
            adquisicion.save()
            
            material_mayor.adquisicion = adquisicion
            material_mayor.save()
            
            request.flash['success'] = 'Material mayor dado de alta exitosamente'
            url = reverse('interface.views.material_mayor')
            
            if request.user.get_profile().is_staff_cuerpo():
                material_mayor.cuerpo = request.user.get_profile().cuerpo
                material_mayor.save()
                material_mayor.validado_por_operaciones = False
                material_mayor.notify_operaciones_of_dada_de_alta()
            
            return HttpResponseRedirect(url)
    else:
        # Utilizamos dos formularios pues uno se encarga estrictamente de la parte técnica del
        # vehículo (motor, chasis, etc) y el otro de sus detalles de adquisicion (orden de compra, 
        # factura comercial, etc). Además el formulario técnico es único, pero el de adquisicion
        # es instanciado dependiendo del origen de la adquisición (compra o donacion)
        form = FormularioDarDeAltaMaterialMayor(user=request.user)
        form_adquisicion = FormularioAdquisicion(user=request.user)
        
    others_uses_ids = [uso.id for uso in UsoMaterialMayor.objects.filter(is_others_option=True)]

    return render_to_response(
        template, 
        {
            'form': form,
            'form_adquisicion': form_adquisicion,
            'others_uses_ids': others_uses_ids
        }, 
        context_instance=RequestContext(request))   

@authorize(roles=(Rol.OPERACIONES(), Rol.ADQUISICIONES()), cargos=(settings.CARGOS_CUERPO['Comandante'],))
def adquisicion_compra_material_mayor(request):
    # Vista para dar de alta material mayor adquirido por compra
    return _adquisicion_material_mayor(request, FormularioAdquisicionCompraMaterialMayor, 'staff/adquisicion_compra_material_mayor.html')

@authorize(roles=(Rol.OPERACIONES(), Rol.ADQUISICIONES()), cargos=(settings.CARGOS_CUERPO['Comandante'],))
def adquisicion_donacion_material_mayor(request):
    # Vista para dar de alta material mayor adquirido por donación
    return _adquisicion_material_mayor(request, FormularioAdquisicionDonacionMaterialMayor, 'staff/adquisicion_donacion_material_mayor.html')
    
def _material_mayor_sin_asignar(request):
    materiales_mayores_sin_asignar = MaterialMayor.objects.filter(cuerpo__isnull=True)
    
    fields = [
            ['modelo_chasis.marca', u'Marca chasis'],
            ['modelo_chasis', u'Modelo chasis'],
            ['marca_carrosado', u'Marca carrosado'],
            ['numero_chasis', u'N° chasis'],
            ['numero_motor', u'N° motor'],
            ['adquisicion.cuerpo_destinatario', u'Cuerpo de destino']
        ]
        
    # may_assign_material_mayor es un flag para ver si mostramos el link al proceso de "Asignar"
    # para cada material mayor en la tabla resumen. Es necesario pues sólo Operaciones Bomberiles puede 
    # asignar material mayor.
        
    may_assign_material_mayor = request.user.get_profile().rol == Rol.OPERACIONES()
    
    # materiales_mayores_por_fuente es la estructura de datos que almacenará temporalmemte los
    # resultados de la consulta. Es una lista en la que cada elemento representa una "sección"
    # de la página mostrada. Por ejemplo, operaciones bomberiles ve dos secciones, correspondientes
    # al material subido desde la JNBC y aquel subido directamente por los cuerpos
    # Cada sección tiene dos atributos:
    #  predicate: Nombre de una función en UserProfile que será aplicada al usuario que subió el material mayor
    #             Si el filtro retorna True entonces ese material mayor será agregado a esta sección.
    
    materiales_mayores_por_fuente = [
        {
            'predicate': 'is_staff_jnbc',
            'title': 'Dados de alta por la JNBC'
        }
    ]
        
    field_keys = [field[0] for field in fields]
    field_values = [field[1] for field in fields]
        
    # Para cada sección...
    for material_mayor_por_fuente in materiales_mayores_por_fuente:
        material_mayor_por_fuente['material_mayor'] = []
        # Para cada posible vehículo...
        for material_mayor in materiales_mayores_sin_asignar:            
            # Si el usuario que subió dicho vehiculo cumple con el predicado de la sección, agregarlo a ella
            if getattr(material_mayor.adquisicion.usuario.get_profile(), material_mayor_por_fuente['predicate'])():
                material_mayor_por_fuente['material_mayor'].append(material_mayor.extract_data(field_keys))
                
    return materiales_mayores_por_fuente, field_values, may_assign_material_mayor
    
@authorize(roles=(Rol.OPERACIONES(), Rol.ADQUISICIONES()))
def material_mayor_sin_asignar(request):
    # Vista que muestra el listado de material mayor que aun no ha sido asignado a un cuerpo
    
    materiales_mayores_por_fuente, fields, may_assign_material_mayor = _material_mayor_sin_asignar(request)
    
    return render_to_response('staff/material_mayor_sin_asignar.html', {
            'material_mayor': materiales_mayores_por_fuente,
            'fields': fields,
            'may_assign_material_mayor': may_assign_material_mayor,
        }, 
        context_instance=RequestContext(request))
        
@authorize(roles=(Rol.OPERACIONES(), Rol.ADQUISICIONES()))
def material_mayor_sin_asignar_excel(request):
    material_mayor, fields, may_assign_material_mayor = _material_mayor_sin_asignar(request)

    response = HttpResponse(mimetype="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=material_mayor_sin_asignar_%s.xls' % str(date.today())
    
    title_style = XFStyle()
    title_font = Font()
    title_font.bold = True
    title_font.height = 300
    title_style.font = title_font
    
    wb = Workbook()
    ws = wb.add_sheet('Material Mayor sin asignar')
    
    ws.row(0).height = 500
    ws.col(0).width = 5000
    ws.col(1).width = 5000
    ws.col(2).width = 7000
    ws.col(3).width = 7000
    ws.col(4).width = 7000
    ws.col(5).width = 7000
    ws.col(6).width = 4000
    ws.col(7).width = 4000
    
    current_row = 0
    ws.write(current_row, 0, 'Material mayor sin asignar', title_style)
    current_row += 1
    
    link_style = easyxf('font: underline single') 
    
    bold_style = XFStyle()
    bold_font = Font()
    bold_font.bold = True
    bold_style.font = bold_font

    
    for value in material_mayor:
        for idx, field in enumerate(fields):
            ws.write(current_row, idx, field, bold_style)
            
        current_row += 1
        
        for vehiculo in value['material_mayor']:
            for idx, field in enumerate(vehiculo['data']):
                ws.write(current_row, idx, field)
                 
            editar_link = settings.SITE_URL + reverse('interface.views.editar_material_mayor', args=[vehiculo['id']])
            ws.write(current_row, idx+1, Formula('HYPERLINK("%s";"Editar")' % editar_link), link_style)
            
            if may_assign_material_mayor:
                asignar_link = settings.SITE_URL + reverse('interface.views.asignar_material_mayor_a_cuerpo', args=[vehiculo['id']])
                ws.write(current_row, idx+2, Formula('HYPERLINK("%s";"Asignar")' % asignar_link), link_style)
            current_row += 1

    wb.save(response)
    return response

@authorize(roles=(Rol.OPERACIONES(), Rol.ADQUISICIONES(), Rol.JURIDICA()), cargos=(settings.CARGOS_CUERPO['Comandante'],))
@authorize_material_mayor_access(requiere_validacion_operaciones=False)
def editar_material_mayor(request, material_mayor):
    # Vista de edición de los datos técnicos de un material mayor
    
    asignacion_link = None
    if material_mayor.validado_por_operaciones:
        if request.user.get_profile().rol == Rol.OPERACIONES():
            asignacion_link = reverse('interface.views.asignar_material_mayor_a_cuerpo', args=[material_mayor.id])
        elif request.user.get_profile().is_staff_cuerpo():
            asignacion_link = reverse('interface.views.asignar_material_mayor_a_compania', args=[material_mayor.id])
    
    if request.method == 'POST':
        form = FormularioDarDeAltaMaterialMayor(request.POST, request.FILES, instance=material_mayor, user=request.user)
        if form.is_valid():
            material_mayor = form.instance
            material_mayor.save()
            request.flash['success'] = 'Material mayor actualizado exitosamente'
            
            if 'next' in request.POST:
                url = request.POST['next']
            else:
                url = reverse('interface.views.editar_material_mayor', args=[material_mayor.id])
            return HttpResponseRedirect(url)
    else:
        form = FormularioDarDeAltaMaterialMayor.get_from_instance(material_mayor, request.user)
        if 'next' in request.GET:
            next = request.GET['next']
        else:
            next = None
    
    return render_to_response('staff/editar_material_mayor.html', {
            'form': form,
            'next': next,
            'asignacion_link': asignacion_link,
        }, 
        context_instance=RequestContext(request))

@authorize(roles=(Rol.OPERACIONES(), Rol.ADQUISICIONES(), Rol.JURIDICA()), cargos=(settings.CARGOS_CUERPO['Comandante'],))
@authorize_material_mayor_access(requiere_validacion_operaciones=False)
def editar_adquisicion_material_mayor(request, material_mayor):
    # Vista de edición de los datos de adquisición de cierto material mayor
    # Nota: La adquisicion puede ser o por compra o por donación, pero
    # el sistema carga la correcta a través de un polimorfismo simulado
    
    adquisicion = material_mayor.adquisicion.get_polymorphic_instance()
    Form = eval('Formulario%s' % (adquisicion.__class__.__name__))
    if request.method == 'POST':
        form = Form(request.POST, request.FILES, instance=adquisicion, user=request.user)
        if form.is_valid():
            adquisicion = form.instance
            adquisicion.save()
            request.flash['success'] = u'Datos de adquisición actualizados exitosamente'
            url = reverse('interface.views.editar_material_mayor', args=[material_mayor.id])
            return HttpResponseRedirect(url)
    else:
        form = Form.get_from_instance(adquisicion, request.user)
    
    return render_to_response('staff/editar_adquisicion_material_mayor.html', {
            'form': form,
        }, 
        context_instance=RequestContext(request))

@authorize(roles=(Rol.OPERACIONES(),))
@authorize_material_mayor_access(requiere_validacion_operaciones=True)
def asignar_material_mayor_a_cuerpo(request, material_mayor):
    # Vista de (re)asignación de material mayor a cierto cuerpo/compañía
    # Sólo Operaciones tiene acceso a esta capacidad
    if request.method == 'POST':
        form = FormularioAsignacionCuerpoMaterialMayor(request.POST, request.FILES)
        if form.is_valid():
            asignacion_material_mayor = form.instance
            
            asignacion_material_mayor.material_mayor = material_mayor
            asignacion_material_mayor.usuario = request.user
            asignacion_material_mayor.tipo = TipoEventoHojaVidaMaterialMayor.objects.get(classname='AsignacionCuerpoMaterialMayor')
            asignacion_material_mayor.save()

            material_mayor.cuerpo = asignacion_material_mayor.cuerpo
            material_mayor.compania = asignacion_material_mayor.compania
            material_mayor.save()

            request.flash['success'] = u'Material mayor asignado correctamente'
            url = reverse('interface.views.editar_material_mayor', args=[material_mayor.id])
            return HttpResponseRedirect(url)
    else:
        form = FormularioAsignacionCuerpoMaterialMayor()
        
    default_cuerpo = material_mayor.adquisicion.cuerpo_destinatario
    default_compania_id = 0
    
    if material_mayor.cuerpo:
        default_cuerpo = material_mayor.cuerpo
        
    if material_mayor.compania:
        default_compania_id = material_mayor.compania.id
    
    return render_to_response('staff/asignar_material_mayor_a_cuerpo.html', {
            'material_mayor': material_mayor,
            'form': form,
            'default_cuerpo': default_cuerpo,
            'default_compania_id': default_compania_id
        }, 
        context_instance=RequestContext(request))
        
@authorize(cargos=(settings.CARGOS_CUERPO['Comandante'],))
@authorize_material_mayor_access(requiere_validacion_operaciones=True)
def asignar_material_mayor_a_compania(request, material_mayor):
    # Vista de (re)asignación de material mayor a cierta compañía
    # Sólo los responsables de cada cuerpo tienen acceso a esta funcionalidad
    if request.method == 'POST':
        form = FormularioAsignacionCompaniaMaterialMayor(material_mayor, request.POST, request.FILES)
        if form.is_valid():
            asignacion_material_mayor = form.instance
            
            asignacion_material_mayor.material_mayor = material_mayor
            asignacion_material_mayor.usuario = request.user
            asignacion_material_mayor.tipo = TipoEventoHojaVidaMaterialMayor.objects.get(classname='AsignacionCompaniaMaterialMayor')
            asignacion_material_mayor.save()

            material_mayor.compania = asignacion_material_mayor.compania
            material_mayor.save()

            request.flash['success'] = u'Material mayor asignado correctamente'
            url = reverse('interface.views.editar_material_mayor', args=[material_mayor.id])
            return HttpResponseRedirect(url)
    else:
        form = FormularioAsignacionCompaniaMaterialMayor(material_mayor)
    
    return render_to_response('staff/asignar_material_mayor_a_compania.html', {
            'material_mayor': material_mayor,
            'form': form,
        }, 
        context_instance=RequestContext(request))      


@authorize(roles=(Rol.OPERACIONES(), Rol.ADQUISICIONES(), Rol.JURIDICA()), cargos=(settings.CARGOS_CUERPO['Comandante'],))
@authorize_material_mayor_access(requiere_validacion_operaciones=False)
def detalles_hoja_de_vida_material_mayor(request, material_mayor):
    # Vista que despliega el listado de eventos en la hoja de vida de un material mayor en particular
    
    events = [event.get_polymorphic_instance() for event in EventoHojaVidaMaterialMayor.objects.filter(material_mayor=material_mayor).order_by('fecha')]
    
    return render_to_response('staff/detalles_hoja_de_vida_material_mayor.html', {
            'material_mayor': material_mayor,
            'events': events
        }, 
        context_instance=RequestContext(request))
        

@authorize(roles=(Rol.OPERACIONES(), Rol.ADQUISICIONES(), Rol.JURIDICA()), cargos=(settings.CARGOS_CUERPO['Comandante'],))
@authorize_material_mayor_access(requiere_validacion_operaciones=False)
def detalle_evento_hoja_de_vida_material_mayor(request, material_mayor, evento_id):
    # Vista que despliega el detalle de alguno de los eventos de la hoja de vida de cierto material mayor
    evento = EventoHojaVidaMaterialMayor.objects.get(pk=evento_id).get_polymorphic_instance()
    
    if evento.material_mayor != material_mayor:
        raise ValueError
        
    Form = eval('FormularioHojaVida' + evento.__class__.__name__)
    
    if request.method == 'POST':
        form = Form(request.POST, request.FILES, instance=evento)
        if form.is_valid():
            form.instance.save()
            
            request.flash['success'] = u'Evento actualizado exitosamente'
            url = reverse('interface.views.detalle_evento_hoja_de_vida_material_mayor', args=[material_mayor.id, evento.id])
            return HttpResponseRedirect(url)
    else:
        form = Form(instance=evento)
        
    template = convert_camelcase_to_lowercase(evento.__class__.__name__)
        
    return render_to_response('staff/detalle_evento_%s.html' % template, {
            'material_mayor': material_mayor,
            'form': form
        }, 
        context_instance=RequestContext(request))
        
def _material_mayor(request):
    if request.user.get_profile().is_staff_jnbc():
        data = request.GET
        title = 'Navegador de material mayor'
    else:
        data = {
            'region': request.user.get_profile().cuerpo.comuna.provincia.region.id,
            'cuerpo': request.user.get_profile().cuerpo.id
        }
        title = 'Material mayor del cuerpo'
        
    form = MaterialMayorSearchForm(data)
    material_mayor = form.get_filtered_material_mayor()
    return form, material_mayor, title

@authorize(roles=(Rol.OPERACIONES(), Rol.ADQUISICIONES(), Rol.JURIDICA()), cargos=(settings.CARGOS_CUERPO['Comandante'],))
def material_mayor(request):
    form, material_mayor, title = _material_mayor(request)
    
    if request.user.get_profile().is_staff_jnbc():
        template = 'staff/material_mayor.html'
    else:
        template = 'staff/material_mayor_cuerpo.html'
        
    return render_to_response(template, {
            'form': form,
            'material_mayor': material_mayor,
            'title': title
        }, 
        context_instance=RequestContext(request))
        
@authorize(roles=(Rol.OPERACIONES(), Rol.ADQUISICIONES(), Rol.JURIDICA()), cargos=(settings.CARGOS_CUERPO['Comandante'],))
def material_mayor_excel(request):
    form, material_mayor, title = _material_mayor(request)
    
    response = HttpResponse(mimetype="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=material_mayor_%s.xls' % str(date.today())
    
    title_style = XFStyle()
    title_font = Font()
    title_font.bold = True
    title_font.height = 300
    title_style.font = title_font
    
    wb = Workbook()
    ws = wb.add_sheet('Material Mayor')
    
    ws.row(0).height = 500
    ws.col(0).width = 5000
    ws.col(1).width = 5000
    ws.col(2).width = 7000
    ws.col(3).width = 7000
    ws.col(4).width = 7000
    ws.col(5).width = 7000
    ws.col(6).width = 4000
    ws.col(7).width = 4000
    
    current_row = 0
    ws.write(current_row, 0, title, title_style)
    current_row += 1
    
    link_style = easyxf('font: underline single') 
    
    bold_style = XFStyle()
    bold_font = Font()
    bold_font.bold = True
    bold_style.font = bold_font

    
    ws.write(current_row, 0, u'Marca chasis', bold_style)
    ws.write(current_row, 1, u'Modelo chasis', bold_style)
    ws.write(current_row, 2, u'Marca carrosado', bold_style)
    ws.write(current_row, 3, u'N° chasis', bold_style)
    ws.write(current_row, 4, u'N° motor', bold_style)
    ws.write(current_row, 5, u'Cuerpo', bold_style)
    ws.write(current_row, 6, u'Compañía', bold_style)
            
    current_row += 1
        
    for material_mayor in material_mayor:
        ws.write(current_row, 0, unicode(material_mayor.modelo_chasis.marca))
        ws.write(current_row, 1, unicode(material_mayor.modelo_chasis))
        ws.write(current_row, 2, unicode(material_mayor.marca_carrosado))
        ws.write(current_row, 3, unicode(material_mayor.numero_chasis))
        ws.write(current_row, 4, unicode(material_mayor.numero_motor))
        if material_mayor.cuerpo:
            cuerpo_string = unicode(material_mayor.cuerpo)
        else:
            cuerpo_string = 'No asignado'
        ws.write(current_row, 5, cuerpo_string)
        if material_mayor.compania:
            compania_string = unicode(material_mayor.compania)
        else:
            compania_string = 'No asignado'
        ws.write(current_row, 6, compania_string)
             
        editar_link = settings.SITE_URL + reverse('interface.views.editar_material_mayor', args=[material_mayor.id])
        ws.write(current_row, 7, Formula('HYPERLINK("%s";"Editar")' % editar_link), link_style)
        
        current_row += 1

    wb.save(response)
    return response
        
@authorize(roles=(Rol.OPERACIONES(),))
@authorize_material_mayor_access(requiere_validacion_operaciones=True)
def asignar_patente_a_material_mayor(request, material_mayor):
    if material_mayor.asignacion_de_patente:
        request.flash['error'] = 'Material mayor ya tiene patente'
        url = reverse('interface.views.material_mayor')
        
        return HttpResponseRedirect(url)
        
    if request.method == 'POST':
        form = FormularioAsignacionPatenteMaterialMayor(request.POST)
        if form.is_valid():
            instance = form.instance
            
            instance.material_mayor = material_mayor
            instance.usuario = request.user
            instance.tipo = TipoEventoHojaVidaMaterialMayor.objects.get(classname='AsignacionPatenteMaterialMayor')
            instance.save()
            
            material_mayor.asignacion_de_patente = instance
            material_mayor.save()
            
            request.flash['success'] = 'Patente asignada correctamente'
            url = reverse('interface.views.editar_material_mayor', args=[material_mayor.id])
            
            return HttpResponseRedirect(url)
    else:
        form = FormularioAsignacionPatenteMaterialMayor()
    return render_to_response('staff/asignar_patente_a_material_mayor.html', {
            'form': form,
            'material_mayor': material_mayor
        }, 
        context_instance=RequestContext(request))

@authorize(roles=(Rol.OPERACIONES(), Rol.ADQUISICIONES(), Rol.JURIDICA()), cargos=(settings.CARGOS_CUERPO['Comandante'],))
@authorize_material_mayor_access(requiere_validacion_operaciones=True)
def detalles_patente_material_mayor(request, material_mayor):
    asignacion_patente = AsignacionPatenteMaterialMayor.objects.get(material_mayor=material_mayor)
    return detalle_evento_hoja_de_vida_material_mayor(request, material_mayor_id=material_mayor.id, evento_id=asignacion_patente.id)
    
@authorize(roles=(Rol.OPERACIONES(),),)
@authorize_material_mayor_access(requiere_validacion_operaciones=False)
def validar_material_mayor(request, material_mayor):
    if request.method == 'POST':
        material_mayor.validado_por_operaciones = True
        material_mayor.save()
        request.flash['success'] = 'Material mayor validado exitosamente'
        url = reverse('interface.views.editar_material_mayor', args=[material_mayor.id])
        return HttpResponseRedirect(url)
        
@authorize(roles=(Rol.OPERACIONES(),),)
def agregar_pauta_mantencion_chasis(request):
    pass
