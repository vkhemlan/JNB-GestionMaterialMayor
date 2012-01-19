# coding: utf-8

from django.conf import settings
from django.contrib import auth
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, Http404
from django.forms.models import inlineformset_factory

import re
from datetime import date
import xlrd
from xlwt import Workbook, easyxf, Formula, XFStyle, Font
from xlwt.Formatting import Alignment
from interface.forms.formulario_cambio_pauta_mantencion_chasis_material_mayor import FormularioCambioPautaMantencionChasisMaterialMayor
from interface.forms.formulario_dar_de_baja_material_mayor import FormularioDarDeBajaMaterialMayor

from interface.models import MaterialMayor, EventoHojaVidaMaterialMayor, Rol, AsignacionPatenteMaterialMayor, UsoMaterialMayor, PautaMantencionCarrosado, PautaMantencionChasis, ModeloChasisMaterialMayor, FrecuenciaOperacion, MantencionProgramada, OperacionMantencionProgramada, EjecucionOperacionMantencionProgramada
from interface.forms import FormularioAdquisicionCompraMaterialMayor, FormularioAdquisicionDonacionMaterialMayor, MaterialMayorSearchForm, FormularioAgregarMaterialMayor, FormularioEditarMaterialMayor, FormularioAsignacionCuerpoMaterialMayor, FormularioAsignacionCompaniaMaterialMayor, FormularioAsignacionPatenteMaterialMayor, FormularioAgregarPautaMantencionCarrosado, FormularioAgregarPautaMantencionChasis, FormularioCambioPautaMantencionCarrosadoMaterialMayor, FormularioCambioNumeroChasisMaterialMayor, FormularioCambioNumeroMotorMaterialMayor, FormularioPautaMantencionCarrosadoAgregar, FormularioPautaMantencionChasisAgregar, FormularioCambioCertificadoAnotacionesVigentes, FormularioAsignacionSolicitudPrimeraInscripcion, FormularioAgregarArchivoMantencionProgramada
from django.http import HttpResponseRedirect
from interface.models.archivo_mantencion_programada import ArchivoMantencionProgramada
from interface.models.cambio_pauta_mantencion_carrosado_material_mayor import CambioPautaMantencionCarrosadoMaterialMayor
from interface.models.operacion_mantencion_pauta import OperacionMantencionPauta
from interface.utils import convert_camelcase_to_lowercase, log
from django.contrib.auth.decorators import login_required

from authentication import authorize, authorize_material_mayor_access

@login_required
def logout(request):
    """
    Vista de cierre de sesión, boilerplate
    """
    request.flash['success'] = 'Ha salido exitosamente del sistema'
    log('User %s logged out' % request.user.username)
    auth.logout(request)
    return redirect('login')

@login_required
def index(request):
    """
    Vista de la página de inicio para cualquier usuario logueado
    """
    
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
        form = FormularioAgregarMaterialMayor(request.POST, request.FILES, user=request.user)
        form_adquisicion = FormularioAdquisicion(request.POST, request.FILES, user=request.user)
        if form.is_valid() and form_adquisicion.is_valid():
            data_form = FormularioAgregarMaterialMayor(request.POST, user=request.user)
            data_form.is_valid()

            material_mayor_data = data_form.instance
            material_mayor_data.save()
            
            form = FormularioAgregarMaterialMayor(request.POST, request.FILES, user=request.user, instance=material_mayor_data)
            form.is_valid()

            material_mayor = form.get_instance()
            material_mayor.adquisicion = form_adquisicion.get_instance(request.user)
            material_mayor.save()
            
            #adquisicion.materialmayor = material_mayor
            #adquisicion.save()

            #material_mayor.save()
            
            if request.user.get_profile().is_staff_cuerpo():
                material_mayor.cuerpo = request.user.get_profile().cuerpo
                material_mayor.validado_por_operaciones = False
                material_mayor.save()
                material_mayor.notify_operaciones_of_dada_de_alta()
            
            request.flash['success'] = 'Material mayor dado de alta exitosamente'
            
            if material_mayor.validado_por_operaciones:
                url = reverse('interface.views.material_mayor')
            else:
                url = reverse('interface.views.material_mayor_sin_validar')
            return HttpResponseRedirect(url)
    else:
        # Utilizamos dos formularios pues uno se encarga estrictamente de la parte técnica del
        # vehículo (motor, chasis, etc) y el otro de sus detalles de adquisicion (orden de compra, 
        # factura comercial, etc). Además el formulario técnico es único, pero el de adquisicion
        # es instanciado dependiendo del origen de la adquisición (compra o donacion)
        form = FormularioAgregarMaterialMayor(user=request.user)
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
    
def _material_mayor_sin_validar(request):
    fields = [
            ['modelo_chasis.marca', u'Marca chasis'],
            ['modelo_chasis', u'Modelo chasis'],
            ['marca_carrosado', u'Marca carrosado'],
            ['numero_chasis', u'N° chasis'],
            ['numero_motor', u'N° motor'],
            ['adquisicion.cuerpo_destinatario', u'Cuerpo de destino']
        ]
    
    if request.user.get_profile().is_staff_jnbc():
        materiales_mayores_sin_validar = MaterialMayor.objects.filter(validado_por_operaciones=False)
    else:
        materiales_mayores_sin_validar = MaterialMayor.objects.filter(validado_por_operaciones=False, adquisicion__cuerpo_destinatario=request.user.get_profile().cuerpo)
        
    field_keys = [field[0] for field in fields]
    field_values = [field[1] for field in fields]
    
    materiales_mayores_sin_validar_formateados = [material_mayor.extract_data(field_keys) for material_mayor in materiales_mayores_sin_validar]
                
    return materiales_mayores_sin_validar_formateados, field_values
    
@authorize(roles=(Rol.OPERACIONES(), Rol.ADQUISICIONES()), cargos=(settings.CARGOS_CUERPO['Comandante'],))
def material_mayor_sin_validar(request):
    # Vista que muestra el listado de material mayor que aun no ha sido asignado a un cuerpo
    
    materiales_mayores_formateados, fields = _material_mayor_sin_validar(request)
    
    return render_to_response('staff/material_mayor_sin_validar.html', {
            'material_mayor': materiales_mayores_formateados,
            'fields': fields,
        }, 
        context_instance=RequestContext(request))
        
@authorize(roles=(Rol.OPERACIONES(), Rol.ADQUISICIONES()), cargos=(settings.CARGOS_CUERPO['Comandante'],))
def material_mayor_sin_validar_excel(request):
    material_mayor, fields = _material_mayor_sin_validar(request)

    response = HttpResponse(mimetype="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=material_mayor_sin_validar_%s.xls' % str(date.today())
    
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

    
    for idx, field in enumerate(fields):
        ws.write(current_row, idx, field, bold_style)
        
    current_row += 1
    
    for vehiculo in material_mayor:
        idx = 0
        for idx, field in enumerate(vehiculo['data']):
            ws.write(current_row, idx, field)
             
        editar_link = settings.SITE_URL + reverse('interface.views.editar_material_mayor', args=[vehiculo['id']])
        
        if request.user.get_profile().puede_validar_material_mayor():
            edit_text = 'Revisar y validar'
        else:
            edit_text = 'Editar'
        
        ws.write(current_row, idx+1, Formula('HYPERLINK("%s";"%s")' % (editar_link, edit_text, )), link_style)
        
        current_row += 1

    wb.save(response)
    return response

@authorize(roles=(Rol.OPERACIONES(),),)
@authorize_material_mayor_access(requiere_validacion_operaciones=False)    
def eliminar_material_mayor(request, material_mayor):
    if request.method == 'POST':
        material_mayor.delete()
        request.flash['success'] = u'Material mayor eliminado exitosamente'
        url = reverse('interface.views.material_mayor')
        return HttpResponseRedirect(url)
    else:
        return render_to_response('staff/eliminar_material_mayor.html', {
            'material_mayor': material_mayor,
        }, 
        context_instance=RequestContext(request))
    
@authorize(roles=(Rol.OPERACIONES(),),)
@authorize_material_mayor_access(requiere_validacion_operaciones=False)
def cambiar_pauta_mantencion_carrosado(request, material_mayor):
    if request.method == 'POST':
        form = FormularioCambioPautaMantencionCarrosadoMaterialMayor(request.POST)
        if form.is_valid():
            instance = CambioPautaMantencionCarrosadoMaterialMayor()
            instance.nueva_pauta_mantencion_carrosado = form.cleaned_data['pauta_mantencion_carrosado'].name

            instance.cargar_informacion_hoja_de_vida(material_mayor, request.user, 'CambioPautaMantencionCarrosadoMaterialMayor')
            instance.save()
            
            material_mayor.pauta_mantencion_carrosado = form.cleaned_data['pauta_mantencion_carrosado']
            material_mayor.save()
            
            request.flash['success'] = u'Cambio de pauta de mantención realizado exitosamente'
            url = reverse('interface.views.editar_material_mayor', args=[material_mayor.id])
            return HttpResponseRedirect(url)
    else:
        form = FormularioCambioPautaMantencionCarrosadoMaterialMayor()
    return render_to_response('staff/cambiar_pauta_mantencion_carrosado.html', {
        'form': form,
        'material_mayor': material_mayor
    }, 
    context_instance=RequestContext(request))
    
@authorize(roles=(Rol.OPERACIONES(),), cargos=(settings.CARGOS_CUERPO['Inspector de Material Mayor'],) )
@authorize_material_mayor_access(requiere_validacion_operaciones=False)
def cambiar_numero_chasis_material_mayor(request, material_mayor):
    if request.method == 'POST':
        form = FormularioCambioNumeroChasisMaterialMayor(request.POST)
        if form.is_valid():
            instance = form.instance
            instance.cargar_informacion_hoja_de_vida(material_mayor, request.user, 'CambioNumeroChasisMaterialMayor')
            instance.save()
            
            material_mayor.numero_chasis = instance.nuevo_numero_chasis
            material_mayor.save()
            
            request.flash['success'] = u'Cambio de número de chasis realizado exitosamente'
            url = reverse('interface.views.editar_material_mayor', args=[material_mayor.id])
            return HttpResponseRedirect(url)
    else:
        form = FormularioCambioNumeroChasisMaterialMayor() 
    return render_to_response('staff/cambiar_numero_chasis_material_mayor.html', {
        'form': form,
        'material_mayor': material_mayor
    }, 
    context_instance=RequestContext(request))

@authorize(roles=(Rol.OPERACIONES(),),)
@authorize_material_mayor_access(requiere_validacion_operaciones=True)
def dar_de_baja_material_mayor(request, material_mayor):
    if request.method == 'POST':
        form = FormularioDarDeBajaMaterialMayor(request.POST)
        if form.is_valid():
            instance = form.instance
            instance.cargar_informacion_hoja_de_vida(material_mayor, request.user, 'DadaDeBajaMaterialMayor')
            instance.save()

            material_mayor.dada_de_baja = instance
            material_mayor.save()

            request.flash['success'] = u'Material dado de baja exitosamente'
            url = reverse('interface.views.editar_material_mayor', args=[material_mayor.id])
            return HttpResponseRedirect(url)
    else:
        form = FormularioDarDeBajaMaterialMayor()
    return render_to_response('staff/dar_de_baja_material_mayor.html', {
        'form': form,
        'material_mayor': material_mayor
    },
    context_instance=RequestContext(request))
    
@authorize(roles=(Rol.OPERACIONES(),), cargos=(settings.CARGOS_CUERPO['Inspector de Material Mayor'],))
@authorize_material_mayor_access(requiere_validacion_operaciones=False)
def cambiar_numero_motor_material_mayor(request, material_mayor):
    if request.method == 'POST':
        form = FormularioCambioNumeroMotorMaterialMayor(request.POST)
        if form.is_valid():
            instance = form.instance

            instance.cargar_informacion_hoja_de_vida(material_mayor, request.user, 'CambioNumeroMotorMaterialMayor')
            instance.save()

            material_mayor.numero_motor = instance.nuevo_numero_motor
            material_mayor.save()
            
            request.flash['success'] = u'Cambio de número de motor realizado exitosamente'
            url = reverse('interface.views.editar_material_mayor', args=[material_mayor.id])
            return HttpResponseRedirect(url)
    else:
        form = FormularioCambioNumeroMotorMaterialMayor() 
    return render_to_response('staff/cambiar_numero_motor_material_mayor.html', {
        'form': form,
        'material_mayor': material_mayor
    }, 
    context_instance=RequestContext(request))


@authorize(roles=(Rol.OPERACIONES(), Rol.ADQUISICIONES(), Rol.JURIDICA()), cargos=(settings.CARGOS_CUERPO['Comandante'], settings.CARGOS_CUERPO['Inspector de Material Mayor'],))
@authorize_material_mayor_access(requiere_validacion_operaciones=False, requiere_material_en_servicio=False)
def editar_material_mayor(request, material_mayor):
    # Vista de edición de los datos técnicos de un material mayor
    next = None
    asignacion_link = None

    if material_mayor.validado_por_operaciones:
        if request.user.get_profile().rol == Rol.OPERACIONES():
            asignacion_link = reverse('interface.views.asignar_material_mayor_a_cuerpo', args=[material_mayor.id])
        elif request.user.get_profile().is_comandante():
            asignacion_link = reverse('interface.views.asignar_material_mayor_a_compania', args=[material_mayor.id])
    
    if request.method == 'POST':
        if material_mayor.dada_de_baja:
            request.flash['error'] = 'El material fue dado de baja'
            url = reverse('interface.views.editar_material_mayor', args=[material_mayor.id])
            return HttpResponseRedirect(url)

        form = FormularioEditarMaterialMayor(request.POST, request.FILES, instance=material_mayor, user=request.user)
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
        form = FormularioEditarMaterialMayor.get_from_instance(material_mayor, request.user)

        if 'next' in request.GET:
            next = request.GET['next']
    
    return render_to_response('staff/editar_material_mayor.html', {
            'form': form,
            'next': next,
            'asignacion_link': asignacion_link,
            'others_uses_ids': [uso.id for uso in UsoMaterialMayor.objects.filter(is_others_option=True)],
            'dado_de_baja': form.instance.dada_de_baja
        }, 
        context_instance=RequestContext(request))

@authorize(roles=(Rol.OPERACIONES(), Rol.ADQUISICIONES(), Rol.JURIDICA()), cargos=(settings.CARGOS_CUERPO['Comandante'], settings.CARGOS_CUERPO['Inspector de Material Mayor'],))
@authorize_material_mayor_access(requiere_validacion_operaciones=False, requiere_material_en_servicio=False)
def editar_adquisicion_material_mayor(request, material_mayor):
    # Vista de edición de los datos de adquisición de cierto material mayor
    # Nota: La adquisicion puede ser o por compra o por donación, pero
    # el sistema carga la correcta a través de un polimorfismo simulado
    
    adquisicion = material_mayor.adquisicion.get_polymorphic_instance()
    Form = eval('Formulario%s' % adquisicion.__class__.__name__)
    if request.method == 'POST':
        if material_mayor.dada_de_baja:
            request.flash['error'] = 'El material fue dado de baja'
            url = reverse('interface.views.editar_material_mayor', args=[material_mayor.id])
            return HttpResponseRedirect(url)

        form = Form(request.POST, request.FILES, instance=adquisicion, user=request.user)
        if form.is_valid():
            adquisicion = form.instance
            adquisicion.save()
            request.flash['success'] = u'Datos de adquisición actualizados exitosamente'
            url = reverse('interface.views.editar_adquisicion_material_mayor', args=[material_mayor.id])
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
            instance = form.instance

            instance.cargar_informacion_hoja_de_vida(material_mayor, request.user, 'AsignacionCuerpoMaterialMayor')
            instance.save()

            material_mayor.cuerpo = instance.cuerpo
            material_mayor.compania = instance.compania
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
            instance = form.instance

            instance.cargar_informacion_hoja_de_vida(material_mayor, request.user, 'AsignacionCompaniaMaterialMayor')
            instance.save()

            material_mayor.compania = instance.compania
            material_mayor.save()
            material_mayor.notify_operaciones_of_asignacion_a_compania()

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


@authorize(roles=(Rol.OPERACIONES(), Rol.ADQUISICIONES(), Rol.JURIDICA()), cargos=(settings.CARGOS_CUERPO['Comandante'], settings.CARGOS_CUERPO['Inspector de Material Mayor'],) )
@authorize_material_mayor_access(requiere_validacion_operaciones=False, requiere_material_en_servicio=False)
def detalles_hoja_de_vida_material_mayor(request, material_mayor):
    # Vista que despliega el listado de eventos en la hoja de vida de un material mayor en particular
    
    events = [event.get_polymorphic_instance() for event in EventoHojaVidaMaterialMayor.objects.filter(material_mayor=material_mayor).order_by('-fecha')]
    
    return render_to_response('staff/detalles_hoja_de_vida_material_mayor.html', {
            'material_mayor': material_mayor,
            'events': events
        }, 
        context_instance=RequestContext(request))
        

@authorize(roles=(Rol.OPERACIONES(), Rol.ADQUISICIONES(), Rol.JURIDICA()), cargos=(settings.CARGOS_CUERPO['Comandante'], settings.CARGOS_CUERPO['Inspector de Material Mayor'],) )
@authorize_material_mayor_access(requiere_validacion_operaciones=False, requiere_material_en_servicio=False)
def detalle_evento_hoja_de_vida_material_mayor(request, material_mayor, evento_id):
    # Vista que despliega el detalle de alguno de los eventos de la hoja de vida de cierto material mayor
    evento = EventoHojaVidaMaterialMayor.objects.get(pk=evento_id).get_polymorphic_instance()
    
    if evento.material_mayor != material_mayor:
        raise ValueError

    my_forms = __import__('interface.forms', fromlist=['interface'])
    Form = getattr(my_forms, 'FormularioHojaVida' + evento.__class__.__name__)
    
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

@authorize(roles=(Rol.OPERACIONES(), Rol.ADQUISICIONES(), Rol.JURIDICA()), cargos=(settings.CARGOS_CUERPO['Comandante'], settings.CARGOS_CUERPO['Inspector de Material Mayor'],))
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

            instance.cargar_informacion_hoja_de_vida(material_mayor, request.user, 'AsignacionPatenteMaterialMayor')
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
@authorize_material_mayor_access(requiere_validacion_operaciones=True, requiere_material_en_servicio=False)
def detalles_patente_material_mayor(request, material_mayor):
    asignacion_patente = AsignacionPatenteMaterialMayor.objects.get(material_mayor=material_mayor)
    return detalle_evento_hoja_de_vida_material_mayor(request, material_mayor=material_mayor.id, evento_id=asignacion_patente.id)
    
@authorize(roles=(Rol.OPERACIONES(),),)
@authorize_material_mayor_access(requiere_validacion_operaciones=False)
def validar_material_mayor(request, material_mayor):
    if material_mayor.validado_por_operaciones:
        request.flash['error'] = 'El material mayor ya está validado'
        url = reverse('interface.views.editar_material_mayor', args=[material_mayor.id])
        return HttpResponseRedirect(url)
        
    validation_errors = []
    if not material_mayor.pauta_mantencion_carrosado:
        url = reverse('interface.views.cambiar_pauta_mantencion_carrosado', args=[material_mayor.id])
        validation_errors.append(['El material aún no tiene asignada una pauta de mantención de carrosado', url])
        
    if request.method == 'POST':
        if validation_errors:
            request.flash['error'] = 'Error en el proceso de validación'
        else:
            material_mayor.validado_por_operaciones = True
            material_mayor.save()
            request.flash['success'] = 'Material mayor validado exitosamente'
        url = reverse('interface.views.editar_material_mayor', args=[material_mayor.id])
        return HttpResponseRedirect(url)
    else:
        return render_to_response('staff/validar_material_mayor.html', {
            'material_mayor': material_mayor,
            'validation_errors': validation_errors
        }, 
        context_instance=RequestContext(request))
        
# Métodos comunes de manejo de pautas de mantencion

def _editar_pauta_mantencion(request, tipo, ClasePautaMantencion, FormularioAgregarPautaMantencion, instance):
    PautaMantencionInlineFormSet = inlineformset_factory(ClasePautaMantencion, OperacionMantencionPauta)
    prevent_validation_errors = False
    formset = PautaMantencionInlineFormSet()
    
    if request.method == 'POST':
        form = FormularioAgregarPautaMantencion(request.POST, instance=instance)
        if 'add' in request.POST:
            formset_data = request.POST.copy()
            total_forms_field_name = 'operacionmantencionpauta_set-TOTAL_FORMS'
            total_forms_quantity = int(formset_data[total_forms_field_name])
            formset_data[total_forms_field_name] = str(total_forms_quantity + 1)
            formset = PautaMantencionInlineFormSet(formset_data, instance=instance)
            prevent_validation_errors = True
        elif 'delete' in request.POST:
            formset = PautaMantencionInlineFormSet(request.POST, instance=instance)

            for f in formset.deleted_forms:
                if f.instance.id:
                    f.instance.delete()

            url = reverse('interface.views.pauta_mantencion_%s_editar' % tipo, args=[instance.id])
            return HttpResponseRedirect(url + '?refresh=True')
        elif 'save' in request.POST:
            formset = PautaMantencionInlineFormSet(request.POST, instance=instance)
            if form.is_valid() and formset.is_valid():
                form.save()
                
                for f in formset.forms:
                    if f.has_changed():
                        f.instance.pauta = form.instance
                        f.instance.save()
                        
                commit_ids = [f.instance.id for f in formset.forms if f.instance.id]
                
                for referral_object in formset.queryset:
                    if referral_object.id not in commit_ids:
                        referral_object.delete()
                
                request.flash['success'] = 'Pauta de mantención guardada exitosamente'
                url = reverse('interface.views.pauta_mantencion_%s' % tipo)
                return HttpResponseRedirect(url)
    else:
        formset = PautaMantencionInlineFormSet(instance=instance)
        form = FormularioAgregarPautaMantencion(instance=instance)
        
    return render_to_response('staff/pauta_mantencion_%s_editar.html' % tipo, {
        'form': form,
        'formset': formset,
        'prevent_validation_errors': prevent_validation_errors,
        'instance': instance
    }, 
        context_instance=RequestContext(request))
        
# Sistema de mantención de pautas de mantención de carrosados
    
def _parse_pauta_mantencion_contents(input_file, ModelClass):
    try:
        wb = xlrd.open_workbook(file_contents=input_file.read())
        sh = wb.sheet_by_index(0)

        number_metadata_rows = 4
        number_operations = sh.nrows - number_metadata_rows
    
        nombre_pauta = sh.cell(1, 0).value
    
        m = ModelClass(name=nombre_pauta)
    except Exception:
        print '1'
        return None
        
    m.save()

    try:
        for operation_index in range(number_operations):
            row_operation = operation_index + number_metadata_rows
            operation_name = sh.cell(row_operation, 0).value
            if operation_name:
                operation_frequency = sh.cell(row_operation, 1).value
                r = re.match(r'(\d+) meses$', operation_frequency)
                operation_frequency_value = int(r.groups()[0])
                print operation_frequency_value
                frecuencia = FrecuenciaOperacion.objects.get(numero_meses=operation_frequency_value)
                op = OperacionMantencionPauta(pauta=m, descripcion=operation_name, frecuencia=frecuencia)
                op.save()
    except Exception, e:
        m.delete()
        print e.message
        return None
        
    return m
        
@authorize(roles=(Rol.OPERACIONES(),),)
def agregar_pauta_mantencion_carrosado(request):
    if request.method == 'POST':
        form = FormularioPautaMantencionCarrosadoAgregar(request.POST, request.FILES)
        if form.is_valid():
            input_excel = request.FILES['pauta_mantencion']
            pauta_mantencion = _parse_pauta_mantencion_contents(input_excel, PautaMantencionCarrosado)
            if pauta_mantencion:
                request.flash['success'] = u'Pauta de mantención subida exitosamente'
                url = reverse('interface.views.pauta_mantencion_carrosado')
                return HttpResponseRedirect(url)
            else:
                form._errors['pauta_mantencion'] = form.error_class([u'Existe un error en el archivo XLS subido'])
    else:
        form = FormularioPautaMantencionCarrosadoAgregar()
    return render_to_response('staff/pauta_mantencion_carrosado_agregar.html', {
            'form': form
        }, 
        context_instance=RequestContext(request))

    
@authorize(roles=(Rol.OPERACIONES(),),)
def pauta_mantencion_carrosado(request):
    pautas_mantencion_carrosado = PautaMantencionCarrosado.objects.all()
    return render_to_response('staff/pauta_mantencion_carrosado.html', {
        'pautas': pautas_mantencion_carrosado
        }, 
        context_instance=RequestContext(request))
        
@authorize(roles=(Rol.OPERACIONES(),),)
def pauta_mantencion_carrosado_editar(request, pauta_mantencion_carrosado_id):
    pauta_mantencion_carrosado = PautaMantencionCarrosado.objects.get(pk=pauta_mantencion_carrosado_id)
    return _editar_pauta_mantencion(request, 'carrosado', PautaMantencionCarrosado, FormularioAgregarPautaMantencionCarrosado, pauta_mantencion_carrosado)
    
@authorize(roles=(Rol.OPERACIONES(),),)
def pauta_mantencion_carrosado_eliminar(request, pauta_mantencion_carrosado_id):
    pauta_mantencion_carrosado = PautaMantencionCarrosado.objects.get(pk=pauta_mantencion_carrosado_id)
    material_mayor = MaterialMayor.objects.filter(pauta_mantencion_carrosado=pauta_mantencion_carrosado)
    
    if request.method == 'POST':
        if material_mayor:
            request.flash['error'] = 'Error en la eliminación de pauta de mantención'
        else:
            pauta_mantencion_carrosado.delete()
            request.flash['success'] = 'Pauta de mantención eliminada exitosamente'
            
        url = reverse('interface.views.pauta_mantencion_carrosado')
        return HttpResponseRedirect(url)
            
    return render_to_response('staff/pauta_mantencion_carrosado_eliminar.html', {
        'pauta': pauta_mantencion_carrosado,
        'material_mayor': material_mayor
        }, 
        context_instance=RequestContext(request))
        
# Sistema de mantención de pautas de mantención de chasis
        
@authorize(roles=(Rol.OPERACIONES(),),)
def agregar_pauta_mantencion_chasis(request):
    if request.method == 'POST':
        form = FormularioPautaMantencionChasisAgregar(request.POST, request.FILES)
        if form.is_valid():
            input_excel = request.FILES['pauta_mantencion']
            pauta_mantencion = _parse_pauta_mantencion_contents(input_excel, PautaMantencionChasis)
            if pauta_mantencion:
                request.flash['success'] = u'Pauta de mantención subida exitosamente'
                url = reverse('interface.views.pauta_mantencion_chasis')
                return HttpResponseRedirect(url)
            else:
                form._errors['pauta_mantencion'] = form.error_class([u'Existe un error en el archivo XLS subido'])
    else:
        form = FormularioPautaMantencionChasisAgregar()
    return render_to_response('staff/pauta_mantencion_chasis_agregar.html', {
            'form': form
        }, 
        context_instance=RequestContext(request))

    
@authorize(roles=(Rol.OPERACIONES(),),)
def pauta_mantencion_chasis(request):
    pautas_mantencion_chasis = PautaMantencionChasis.objects.all()
    return render_to_response('staff/pauta_mantencion_chasis.html', {
        'pautas': pautas_mantencion_chasis
        }, 
        context_instance=RequestContext(request))
        
@authorize(roles=(Rol.OPERACIONES(),),)
def pauta_mantencion_chasis_editar(request, pauta_mantencion_chasis_id):
    pauta_mantencion_chasis = PautaMantencionChasis.objects.get(pk=pauta_mantencion_chasis_id)
    return _editar_pauta_mantencion(request, 'chasis', PautaMantencionChasis, FormularioAgregarPautaMantencionChasis, pauta_mantencion_chasis)
    
@authorize(roles=(Rol.OPERACIONES(),),)
def pauta_mantencion_chasis_eliminar(request, pauta_mantencion_chasis_id):
    pauta_mantencion_chasis = PautaMantencionChasis.objects.get(pk=pauta_mantencion_chasis_id)
    modelos_chasis = ModeloChasisMaterialMayor.objects.filter(pauta_mantencion=pauta_mantencion_chasis)
    
    if request.method == 'POST':
        if modelos_chasis:
            request.flash['error'] = 'Error en la eliminación de pauta de mantención'
        else:
            pauta_mantencion_chasis.delete()
            request.flash['success'] = 'Pauta de mantención eliminada exitosamente'
            
        url = reverse('interface.views.pauta_mantencion_chasis')
        return HttpResponseRedirect(url)
            
    return render_to_response('staff/pauta_mantencion_chasis_eliminar.html', {
        'pauta': pauta_mantencion_chasis,
        'modelos_chasis': modelos_chasis
        }, 
        context_instance=RequestContext(request))

@authorize(roles=(Rol.OPERACIONES(),),)
@authorize_material_mayor_access(requiere_validacion_operaciones=False)
def cambiar_certificado_anotaciones_vigentes(request, material_mayor):
    if request.method == 'POST':
        form = FormularioCambioCertificadoAnotacionesVigentes(request.POST, request.FILES)
        if form.is_valid():
            instance = form.instance
            instance.cargar_informacion_hoja_de_vida(material_mayor, request.user, 'CambioCertificadoAnotacionesVigentes')
            instance.save()

            material_mayor.certificado_de_anotaciones_vigentes = instance
            material_mayor.save()

            request.flash['success'] = u'Cambio de certificado realizado exitosamente'
            url = reverse('interface.views.editar_material_mayor', args=[material_mayor.id])
            return HttpResponseRedirect(url)
    else:
        form = FormularioCambioCertificadoAnotacionesVigentes()
    return render_to_response('staff/cambio_certificado_anotaciones_vigentes.html', {
        'form': form,
        'material_mayor': material_mayor
    },
    context_instance=RequestContext(request))

@authorize(roles=(Rol.OPERACIONES(),),)
@authorize_material_mayor_access(requiere_validacion_operaciones=False)
def asignar_solicitud_primera_inscripcion(request, material_mayor):
    if request.method == 'POST':
        form = FormularioAsignacionSolicitudPrimeraInscripcion(request.POST, request.FILES)
        if form.is_valid():
            instance = form.instance
            instance.cargar_informacion_hoja_de_vida(material_mayor, request.user, 'AsignacionSolicitudPrimeraInscripcion')
            instance.save()

            material_mayor.asignacion_solicitud_primera_inscripcion = instance
            material_mayor.save()

            request.flash['success'] = u'Asignación de solicitud de primera inscripción realizada exitosamente'
            url = reverse('interface.views.editar_material_mayor', args=[material_mayor.id])
            return HttpResponseRedirect(url)
    else:
        form = FormularioAsignacionSolicitudPrimeraInscripcion()
    return render_to_response('staff/asignacion_solicitud_primera_inscripcion.html', {
        'form': form,
        'material_mayor': material_mayor
    },
    context_instance=RequestContext(request))

@authorize(roles=(Rol.OPERACIONES(),), cargos=(settings.CARGOS_CUERPO['Comandante'], settings.CARGOS_CUERPO['Inspector de Material Mayor'],) )
@authorize_material_mayor_access(requiere_validacion_operaciones=False, requiere_material_en_servicio=False)
def mantenciones_programadas(request, material_mayor):
    mantenciones_programadas = MantencionProgramada.objects.filter(material_mayor=material_mayor).order_by('-fecha')
    for mantencion_programada in mantenciones_programadas:
        if mantencion_programada.operacionmantencionprogramada_set.filter(ejecucion__isnull=True, observaciones__isnull=True):
            mantencion_programada.importante = True
        elif mantencion_programada.operacionmantencionprogramada_set.filter(ejecucion__isnull=True, observaciones__isnull=False):
            mantencion_programada.warning = True
    return render_to_response('staff/mantenciones_programadas.html', {
        'mantenciones_programadas': mantenciones_programadas,
        'material_mayor': material_mayor
    },
    context_instance=RequestContext(request))

@authorize(roles=(Rol.OPERACIONES(),), cargos=(settings.CARGOS_CUERPO['Comandante'], settings.CARGOS_CUERPO['Inspector de Material Mayor'],) )
@authorize_material_mayor_access(requiere_validacion_operaciones=True, requiere_material_en_servicio=False)
def detalle_mantencion_programada(request, material_mayor, mantencion_programada_id):
    mantencion_programada = MantencionProgramada.objects.get(pk=mantencion_programada_id)
    if mantencion_programada.material_mayor != material_mayor:
        raise Http404

    operaciones_mantencion = mantencion_programada.operacionmantencionprogramada_set.all()

    return render_to_response('staff/detalle_mantencion_programada.html', {
        'mantencion_programada': mantencion_programada,
        'operaciones_mantencion': operaciones_mantencion,
        'material_mayor': material_mayor
    },
    context_instance=RequestContext(request))

@authorize(roles=(Rol.OPERACIONES(),), cargos=(settings.CARGOS_CUERPO['Comandante'], settings.CARGOS_CUERPO['Inspector de Material Mayor'],) )
@authorize_material_mayor_access(requiere_validacion_operaciones=True, requiere_material_en_servicio=False)
def detalle_mantencion_programada_excel(request, material_mayor, mantencion_programada_id):
    mantencion_programada = MantencionProgramada.objects.get(pk=mantencion_programada_id)
    if mantencion_programada.material_mayor != material_mayor:
        raise Http404

    operaciones_mantencion = mantencion_programada.operacionmantencionprogramada_set.all()

    response = HttpResponse(mimetype="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=pauta_mantencion_material_mayor.xls'

    title_style = XFStyle()
    title_font = Font()
    title_font.bold = True
    title_font.height = 300
    title_style.font = title_font

    wb = Workbook()
    ws = wb.add_sheet(u'Operaciones')


    ws.row(0).height = 500
    ws.col(0).width = 20000
    ws.col(1).width = 10000

    current_row = 0
    ws.write(current_row, 0, u'Operaciones de mantención programada', title_style)
    current_row += 1

    bold_style = XFStyle()
    bold_font = Font()
    bold_font.bold = True
    bold_style.font = bold_font

    al1 = Alignment()
    al1.horz = Alignment.HORZ_LEFT
    al1.vert = Alignment.VERT_TOP
    al1.wrap = Alignment.WRAP_AT_RIGHT

    style1 = XFStyle()
    style1.alignment = al1

    ws.write(current_row, 0, 'Material mayor: %s' % unicode(material_mayor), bold_style)
    current_row += 2

    ws.write(current_row, 0, u'Operación de mantención', bold_style)
    ws.write(current_row, 1, u'Observaciones', bold_style)
    current_row += 1


    for operacion in operaciones_mantencion:
        ws.write(current_row, 0, operacion.descripcion, style1)
        ws.row(current_row).height = 600
        current_row += 1

    wb.save(response)
    return response


@authorize(roles=(Rol.OPERACIONES(),), cargos=(settings.CARGOS_CUERPO['Comandante'], settings.CARGOS_CUERPO['Inspector de Material Mayor'],) )
@authorize_material_mayor_access(requiere_validacion_operaciones=True)
def marcar_operacion_mantencion_programada_como_ejecutada(request, material_mayor, mantencion_programada_id, operacion_mantencion_id):
    mantencion_programada = MantencionProgramada.objects.get(pk=mantencion_programada_id)
    operacion_mantencion = OperacionMantencionProgramada.objects.get(pk=operacion_mantencion_id)

    if mantencion_programada.material_mayor != material_mayor or operacion_mantencion.mantencion != mantencion_programada:
        raise Http404

    if request.method != 'POST' or operacion_mantencion.ejecucion:
        raise Http404

    observaciones = request.POST['observaciones'].strip()
    if not observaciones:
        observaciones = None

    instance = EjecucionOperacionMantencionProgramada()
    instance.cargar_informacion_hoja_de_vida(material_mayor, request.user, 'EjecucionOperacionMantencionProgramada')
    instance.save()

    operacion_mantencion.ejecucion = instance
    operacion_mantencion.observaciones = observaciones
    operacion_mantencion.save()

    url = reverse('interface.views.detalle_mantencion_programada', args=[material_mayor.id, mantencion_programada.id])
    return HttpResponseRedirect(url)

@authorize(roles=(Rol.OPERACIONES(),), cargos=(settings.CARGOS_CUERPO['Comandante'], settings.CARGOS_CUERPO['Inspector de Material Mayor'],) )
@authorize_material_mayor_access(requiere_validacion_operaciones=True)
def marcar_operacion_mantencion_programada_como_pospuesta(request, material_mayor, mantencion_programada_id, operacion_mantencion_id):
    mantencion_programada = MantencionProgramada.objects.get(pk=mantencion_programada_id)
    operacion_mantencion = OperacionMantencionProgramada.objects.get(pk=operacion_mantencion_id)

    if mantencion_programada.material_mayor != material_mayor or operacion_mantencion.mantencion != mantencion_programada:
        raise Http404

    if request.method != 'POST' or operacion_mantencion.ejecucion:
        raise Http404

    observaciones = request.POST['observaciones'].strip()
    if not observaciones:
        request.flash['error'] = 'Debe indicar el motivo por el que se pospone la mantención'
        url = reverse('interface.views.detalle_mantencion_programada', args=[material_mayor.id, mantencion_programada.id])
        return HttpResponseRedirect(url)

    operacion_mantencion.observaciones = observaciones
    operacion_mantencion.save()

    url = reverse('interface.views.detalle_mantencion_programada', args=[material_mayor.id, mantencion_programada.id])
    return HttpResponseRedirect(url)

@authorize(roles=(Rol.OPERACIONES(),), cargos=(settings.CARGOS_CUERPO['Comandante'], settings.CARGOS_CUERPO['Inspector de Material Mayor'],) )
@authorize_material_mayor_access(requiere_validacion_operaciones=True)
def agregar_archivo_mantencion_programada(request, material_mayor, mantencion_programada_id):
    mantencion_programada = MantencionProgramada.objects.get(pk=mantencion_programada_id)

    if mantencion_programada.material_mayor != material_mayor:
        raise Http404

    if request.method == 'POST':
        form = FormularioAgregarArchivoMantencionProgramada(request.POST, request.FILES)
        if form.is_valid():
            temp_form = FormularioAgregarArchivoMantencionProgramada(request.POST)
            temp_form.is_valid()
            temp_instance = temp_form.instance
            temp_instance.mantencion = mantencion_programada

            temp_instance.save()

            form = FormularioAgregarArchivoMantencionProgramada(request.POST, request.FILES, instance=temp_instance)
            form.save()

            request.flash['success'] = 'Archivo subido exitosamente'
            url = reverse('interface.views.detalle_mantencion_programada', args=[material_mayor.id, mantencion_programada.id])
            return HttpResponseRedirect(url)
    else:
        form = FormularioAgregarArchivoMantencionProgramada()

    return render_to_response('staff/agregar_archivo_mantencion_programada.html', {
        'form': form,
        'mantencion_programada': mantencion_programada,
        'material_mayor': material_mayor
    },
    context_instance=RequestContext(request))

@authorize(roles=(Rol.OPERACIONES(),), cargos=(settings.CARGOS_CUERPO['Comandante'], settings.CARGOS_CUERPO['Inspector de Material Mayor'],) )
@authorize_material_mayor_access(requiere_validacion_operaciones=True)
def eliminar_archivo_mantencion_programada(request, material_mayor, mantencion_programada_id, archivo_id):
    mantencion_programada = MantencionProgramada.objects.get(pk=mantencion_programada_id)
    archivo = ArchivoMantencionProgramada.objects.get(pk=archivo_id)

    if archivo.mantencion != mantencion_programada or mantencion_programada.material_mayor != material_mayor:
        raise Http404

    if request.method == 'POST':
        archivo.archivo.delete()
        archivo.delete()

        request.flash['success'] = 'Archivo eliminado exitosamente'
        url = reverse('interface.views.detalle_mantencion_programada', args=[material_mayor.id, mantencion_programada.id])
        return HttpResponseRedirect(url)
    else:
        return render_to_response('staff/eliminar_archivo_mantencion_programada.html', {
            'archivo': archivo,
            'mantencion_programada': mantencion_programada,
            'material_mayor': material_mayor
        },
        context_instance=RequestContext(request))

@authorize(roles=(Rol.OPERACIONES(),),)
def modelos_chasis(request):
    modelos_chasis = ModeloChasisMaterialMayor.objects.all()
    return render_to_response('staff/modelos_chasis.html', {
        'modelos_chasis': modelos_chasis,
    },
    context_instance=RequestContext(request))

@authorize(roles=(Rol.OPERACIONES(),),)
def cambiar_pauta_modelo_chasis(request, modelo_chasis_id):
    modelo_chasis = ModeloChasisMaterialMayor.objects.get(pk=modelo_chasis_id)
    if request.method == 'POST':
        form = FormularioCambioPautaMantencionChasisMaterialMayor(request.POST, instance=modelo_chasis)
        if form.is_valid():
            form.save()
            request.flash['success'] = 'Pauta cambiada exitosamente'
            url = reverse('interface.views.modelos_chasis')
            return HttpResponseRedirect(url)
    else:
        form = FormularioCambioPautaMantencionChasisMaterialMayor(instance=modelo_chasis)

    return render_to_response('staff/cambiar_pauta_modelo_chasis.html', {
        'modelo_chasis': modelo_chasis,
        'form': form,
    },
    context_instance=RequestContext(request))

@authorize(roles=(Rol.OPERACIONES(),), cargos=(settings.CARGOS_CUERPO['Comandante'], settings.CARGOS_CUERPO['Inspector de Material Mayor'],) )
def mantenciones_programadas_pendientes(request):
    cuerpo = None
    if request.user.get_profile().is_staff_cuerpo():
        cuerpo = request.user.get_profile().cuerpo

    mantenciones_programadas_pendientes = MantencionProgramada.get_pendientes(cuerpo)

    return render_to_response('staff/mantenciones_programadas_pendientes.html', {
        'mantenciones_programadas_pendientes': mantenciones_programadas_pendientes,
    },
    context_instance=RequestContext(request))