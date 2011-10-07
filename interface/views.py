# coding: utf-8

from django.conf import settings
from django.contrib import auth
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, Http404

from interface.models import Cuerpo, MaterialMayor, AdquisicionCompraMaterialMayor, AdquisicionDonacionMaterialMayor, TipoEventoHojaVidaMaterialMayor, EventoHojaVidaMaterialMayor, Rol, AsignacionPatenteMaterialMayor
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
            url = reverse('interface.views.material_mayor_sin_asignar')
            
            if request.user.get_profile().is_staff_cuerpo():
                material_mayor.notify_operaciones_of_dada_de_alta()
            
            return HttpResponseRedirect(url)
    else:
        # Utilizamos dos formularios pues uno se encarga estrictamente de la parte técnica del
        # vehículo (motor, chasis, etc) y el otro de sus detalles de adquisicion (orden de compra, 
        # factura comercial, etc). Además el formulario técnico es único, pero el de adquisicion
        # es instanciado dependiendo del origen de la adquisición (compra o donacion)
        form = FormularioDarDeAltaMaterialMayor(user=request.user)
        form_adquisicion = FormularioAdquisicion(user=request.user)

    return render_to_response(
        template, 
        {
            'form': form,
            'form_adquisicion': form_adquisicion,
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
    
@authorize(roles=(Rol.OPERACIONES(), Rol.ADQUISICIONES()), cargos=(settings.CARGOS_CUERPO['Comandante'],))
def material_mayor_sin_asignar(request):
    # Vista que muestra el listado de material mayor que aun no ha sido asignado a un cuerpo
    # Para el staff de la JNBC le muestra todo el material mayor a nivel nacional que no ha sido asignado
    # Para los usuarios de cuerpos bomberiles les muestra solamente aquel material mayor que tiene 
    # como destinatario su cuerpo
    
    materiales_mayores_sin_asignar = MaterialMayor.objects.filter(cuerpo__isnull=True)
    
    # Fields es un arreglo que contiene los campos que se quieren desplegar en la tabla del template
    # Este arreglo es necesario porque hay información que no le queremos mostrar
    # a los usuarios de cuerpo porque, por ejemplo, el campo es redundante ("Cuerpo destinario")
    
    fields = [
            ['modelo_chasis.marca', 'Marca chasis'],
            ['modelo_chasis', 'Modelo chasis'],
            ['marca_carrosado', 'Marca carrosado'],
            ['numero_chasis', 'N° chasis'],
            ['numero_motor', 'N° motor'],
        ]
        
    # may_assign_material_mayor es un flag para ver si mostramos el link al proceso de "Asignar"
    # para cada material mayor en la tabla resumen. Es necesario pues sólo Operaciones Bomberiles puede 
    # asignar material mayor.
        
    may_assign_material_mayor = request.user.get_profile().rol == Rol.OPERACIONES()
    
    # materiales_mayores_por_fuente es la estructura de datos que almacenará temporalmemte los
    # resultados de la consulta. Es una lista en la que cada elemento representa una "sección"
    # de la página mostrada. Por ejemplo, operaciones bomberiles ve dos secciones, correspondientes
    # al material subido desde la JNBC y aquel subido directamente por los cuerpos, mientras que los
    # usuarios cuerpo solo pueden ver el material subido por ellos mismos.
    # Cada sección tiene dos atributos:
    #  predicate: Nombre de una función en UserProfile que será aplicada al usuario que subió el material mayor
    #             Si el filtro retorna True entonces ese material mayor será agregado a esta sección.
    #  title: Título en texto plano de la sección para ser desplegado en el template
    
    if request.user.get_profile().is_staff_cuerpo():   
        materiales_mayores_por_fuente = [
            {
                'predicate': 'is_staff_cuerpo',
                'title': 'Dados de alta por el cuerpo de %s' % (unicode(request.user.get_profile().cuerpo),)
            }
        ]    
        
        title = 'Material pendiente de asignación al cuerpo'
    else:
    
        fields.insert(5, ['adquisicion.cuerpo_destinatario', 'Cuerpo de destino'])
        materiales_mayores_por_fuente = [
            {
                'predicate': 'is_staff_jnbc',
                'title': 'Dados de alta por la JNBC'
            },
            {
                'predicate': 'is_staff_cuerpo',
                'title': 'Dados de alta por cuerpos'
            }
        ]
        
        title = 'Material mayor sin asignar'
        
    field_keys = [field[0] for field in fields]
        
    # Para cada sección...
    for material_mayor_por_fuente in materiales_mayores_por_fuente:
        material_mayor_por_fuente['material_mayor'] = []
        # Para cada posible vehículo...
        for material_mayor in materiales_mayores_sin_asignar:            
            # Si el usuario que subió dicho vehiculo cumple con el predicado de la sección, agregarlo a ella
            if getattr(material_mayor.adquisicion.usuario.get_profile(), material_mayor_por_fuente['predicate'])():
                material_mayor_por_fuente['material_mayor'].append(material_mayor.extract_data(field_keys))
    
    return render_to_response('staff/material_mayor_sin_asignar.html', {
            'material_mayor': materiales_mayores_por_fuente,
            'fields': fields,
            'may_assign_material_mayor': may_assign_material_mayor,
            'title': title,
        }, 
        context_instance=RequestContext(request))

@authorize(roles=(Rol.OPERACIONES(), Rol.ADQUISICIONES(), Rol.JURIDICA()), cargos=(settings.CARGOS_CUERPO['Comandante'],))
@authorize_material_mayor_access
def editar_material_mayor(request, material_mayor_id):
    # Vista de edición de los datos técnicos de un material mayor
    material_mayor = MaterialMayor.objects.get(pk=material_mayor_id)
    
    asignacion_link = None
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
@authorize_material_mayor_access
def editar_adquisicion_material_mayor(request, material_mayor_id):
    # Vista de edición de los datos de adquisición de cierto material mayor
    # Nota: La adquisicion puede ser o por compra o por donación, pero
    # el sistema carga la correcta a través de un polimorfismo simulado
    
    material_mayor = MaterialMayor.objects.get(pk=material_mayor_id)
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
@authorize_material_mayor_access
def asignar_material_mayor_a_cuerpo(request, material_mayor_id):
    # Vista de (re)asignación de material mayor a cierto cuerpo/compañía
    # Sólo Operaciones tiene acceso a esta capacidad
    material_mayor = MaterialMayor.objects.get(pk=material_mayor_id)
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
@authorize_material_mayor_access
def asignar_material_mayor_a_compania(request, material_mayor_id):
    # Vista de (re)asignación de material mayor a cierta compañía
    # Sólo los responsables de cada cuerpo tienen acceso a esta funcionalidad
    material_mayor = MaterialMayor.objects.get(pk=material_mayor_id)
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
@authorize_material_mayor_access
def detalles_hoja_de_vida_material_mayor(request, material_mayor_id):
    # Vista que despliega el listado de eventos en la hoja de vida de un material mayor en particular
    material_mayor = MaterialMayor.objects.get(pk=material_mayor_id)
    
    events = [event.get_polymorphic_instance() for event in EventoHojaVidaMaterialMayor.objects.filter(material_mayor=material_mayor).order_by('fecha')]
    
    return render_to_response('staff/detalles_hoja_de_vida_material_mayor.html', {
            'material_mayor': material_mayor,
            'events': events
        }, 
        context_instance=RequestContext(request))
        

@authorize(roles=(Rol.OPERACIONES(), Rol.ADQUISICIONES(), Rol.JURIDICA()), cargos=(settings.CARGOS_CUERPO['Comandante'],))
@authorize_material_mayor_access
def detalle_evento_hoja_de_vida_material_mayor(request, material_mayor_id, evento_id):
    # Vista que despliega el detalle de alguno de los eventos de la hoja de vida de cierto material mayor
    material_mayor = MaterialMayor.objects.get(pk=material_mayor_id)
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

@authorize(roles=(Rol.OPERACIONES(), Rol.ADQUISICIONES(), Rol.JURIDICA()), cargos=(settings.CARGOS_CUERPO['Comandante'],))
def material_mayor(request):
    if request.user.get_profile().is_staff_jnbc():
        data = request.GET
        template = 'staff/material_mayor.html'
    else:
        data = {
            'region': request.user.get_profile().cuerpo.comuna.provincia.region.id,
            'cuerpo': request.user.get_profile().cuerpo.id
        }
        template = 'staff/material_mayor_cuerpo.html'
    form = MaterialMayorSearchForm(data)
    search_result = form.get_filtered_material_mayor()
    return render_to_response(template, {
            'form': form,
            'search_result': search_result,
        }, 
        context_instance=RequestContext(request))
        
@authorize(roles=(Rol.OPERACIONES(),))
@authorize_material_mayor_access
def asignar_patente_a_material_mayor(request, material_mayor_id):
    material_mayor = MaterialMayor.objects.get(pk=material_mayor_id)
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
@authorize_material_mayor_access        
def detalles_patente_material_mayor(request, material_mayor_id):
    asignacion_patente = AsignacionPatenteMaterialMayor.objects.get(material_mayor__pk=material_mayor_id)
    return detalle_evento_hoja_de_vida_material_mayor(request, material_mayor_id=material_mayor_id, evento_id=asignacion_patente.id)
