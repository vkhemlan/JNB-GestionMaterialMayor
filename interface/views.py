# coding: utf-8

from django.conf import settings
from django.contrib import auth
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect

from interface.models import Cuerpo, MaterialMayor, AdquisicionCompraMaterialMayor, AdquisicionDonacionMaterialMayor, TipoEventoHojaVidaMaterialMayor, EventoHojaVidaMaterialMayor, Rol
from interface.forms import FormularioAdquisicionCompraMaterialMayor, FormularioAdquisicionDonacionMaterialMayor, MaterialMayorSearchForm, FormularioDarDeAltaMaterialMayor, FormularioAsignacionCuerpoMaterialMayor
from django.http import HttpResponseRedirect
from interface.utils import convert_camelcase_to_lowercase, log
from django.contrib.auth.decorators import login_required

from authentication import authorize

@login_required
def logout(request):
    request.flash['success'] = 'Ha salido exitosamente del sistema'
    log('User %s logged out' % request.user.username)
    auth.logout(request)
    return redirect('login')

@login_required
def index(request):
    return render_to_response('staff/index.html', {}, 
                                context_instance=RequestContext(request))
                                
def _adquisicion_material_mayor(request, FormularioAdquisicion):
    if request.method == 'POST':
        form = FormularioDarDeAltaMaterialMayor(request.POST, request.FILES, user=request.user)
        form_adquisicion = FormularioAdquisicion(request.POST, request.FILES, user=request.user)
        if form.is_valid() and form_adquisicion.is_valid():
            adquisicion = form_adquisicion.get_instance(request.user)
            adquisicion.save()
            material_mayor = form.instance
            material_mayor.adquisicion = adquisicion
            material_mayor.save()
            request.flash['success'] = 'Material mayor dado de alta exitosamente'
            url = reverse('interface.views.material_mayor_sin_asignar')
            
            if request.user.get_profile().is_staff_cuerpo():
                material_mayor.notify_operaciones_of_dada_de_alta()
            
            return HttpResponseRedirect(url)
    else:
        form = FormularioDarDeAltaMaterialMayor(user=request.user)
        form_adquisicion = FormularioAdquisicion(user=request.user)

    return render_to_response(
        'staff/adquisicion_compra_material_mayor.html', 
        {
            'form': form,
            'form_adquisicion': form_adquisicion,
        }, 
        context_instance=RequestContext(request))   

@authorize(roles=(Rol.OPERACIONES(), Rol.ADQUISICIONES()), cargos=(settings.CARGOS_CUERPO['Comandante'],))
def adquisicion_compra_material_mayor(request):
    return _adquisicion_material_mayor(request, FormularioAdquisicionCompraMaterialMayor)

@authorize(roles=(Rol.OPERACIONES(), Rol.ADQUISICIONES()), cargos=(settings.CARGOS_CUERPO['Comandante'],))
def adquisicion_donacion_material_mayor(request):
    return _adquisicion_material_mayor(request, FormularioAdquisicionDonacionMaterialMayor)
    
@authorize(roles=(Rol.OPERACIONES(), Rol.ADQUISICIONES()), cargos=(settings.CARGOS_CUERPO['Comandante'],))
def material_mayor_sin_asignar(request):
    materiales_mayores_sin_asignar = MaterialMayor.objects.filter(cuerpo__isnull=True)
    
    fields = [
            ['modelo_chasis.marca', 'Marca chasis'],
            ['modelo_chasis', 'Modelo chasis'],
            ['numero_chasis', 'N° chasis'],
            ['marca_carrosado', 'Marca carrosado'],
            ['numero_motor', 'N° motor'],
        ]
        
    may_assign_material_mayor = False
    
    if request.user.get_profile().is_staff_cuerpo():    
        materiales_mayores_por_fuente = [
            {
                'predicate': 'is_staff_cuerpo',
                'title': 'Dados de alta por el cuerpo de %s' % (unicode(request.user.get_profile().cuerpo),)
            }
        ]
                
    else:
        may_assign_material_mayor = True
    
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
        
        
    field_keys = [field[0] for field in fields]
        
    for material_mayor_por_fuente in materiales_mayores_por_fuente:
        material_mayor_por_fuente['material_mayor'] = []
        for material_mayor in materiales_mayores_sin_asignar:            
            if getattr(material_mayor.adquisicion.usuario.get_profile(), material_mayor_por_fuente['predicate'])():
                material_mayor_por_fuente['material_mayor'].append(material_mayor.extract_data(field_keys))
    
    return render_to_response('staff/material_mayor_sin_asignar.html', {
            'material_mayor': materiales_mayores_por_fuente,
            'fields': fields,
            'may_assign_material_mayor': may_assign_material_mayor
        }, 
        context_instance=RequestContext(request))
             
################
# Pending
################

def editar_material_mayor(request, material_mayor_id):
    material_mayor = MaterialMayor.objects.get(pk=material_mayor_id)
    if request.method == 'POST':
        form = FormularioDarDeAltaMaterialMayor(request.POST, request.FILES, instance=material_mayor, user=request.user)
        if form.is_valid():
            material_mayor = form.instance
            material_mayor.save()
            request.flash['success'] = 'Material mayor actualizado exitosamente'
            
            if 'next' in request.POST:
                url = request.POST['next']
            else:
                url = reverse('interface.views.index')
            return HttpResponseRedirect(url)
    else:
        form = FormularioDarDeAltaMaterialMayor.get_from_instance(material_mayor)
        if 'next' in request.GET:
            next = request.GET['next']
        else:
            next = None
    
    return render_to_response('staff/editar_material_mayor.html', {
            'form': form,
            'next': next,
        }, 
        context_instance=RequestContext(request))
        
def editar_adquisicion_material_mayor(request, material_mayor_id):
    material_mayor = MaterialMayor.objects.get(pk=material_mayor_id)
    adquisicion = material_mayor.adquisicion.get_polymorphic_instance()
    Form = eval('Formulario%s' % (adquisicion.__class__.__name__))
    if request.method == 'POST':
        form = Form(request.POST, request.FILES, instance=adquisicion)
        if form.is_valid():
            adquisicion = form.instance
            adquisicion.save()
            request.flash['success'] = u'Datos de adquisición actualizados exitosamente'
            url = reverse('interface.views.editar_material_mayor', args=[material_mayor.id])
            return HttpResponseRedirect(url)
    else:
        form = Form.get_from_instance(adquisicion)
    
    return render_to_response('staff/editar_adquisicion_material_mayor.html', {
            'form': form,
        }, 
        context_instance=RequestContext(request))
        
def asignar_material_mayor_a_cuerpo(request, material_mayor_id):
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

def detalles_hoja_de_vida_material_mayor(request, material_mayor_id):
    material_mayor = MaterialMayor.objects.get(pk=material_mayor_id)
    
    events = [event.get_polymorphic_instance() for event in EventoHojaVidaMaterialMayor.objects.filter(material_mayor=material_mayor).order_by('fecha')]
    
    return render_to_response('staff/detalles_hoja_de_vida_material_mayor.html', {
            'material_mayor': material_mayor,
            'events': events
        }, 
        context_instance=RequestContext(request))
        
        
def detalle_evento_hoja_de_vida_material_mayor(request, material_mayor_id, evento_id):
    material_mayor = MaterialMayor.objects.get(pk=material_mayor_id)
    evento = EventoHojaVidaMaterialMayor.objects.get(pk=evento_id).get_polymorphic_instance()
    
    if evento.material_mayor != material_mayor:
        raise ValueError
        
    template = convert_camelcase_to_lowercase(evento.__class__.__name__)
        
    return render_to_response('staff/detalle_evento_%s.html' % template, {
            'material_mayor': material_mayor,
            'evento': evento
        }, 
        context_instance=RequestContext(request))
        
def material_mayor(request):
    form = MaterialMayorSearchForm(request.GET)
    search_result = form.get_filtered_material_mayor()
    return render_to_response('staff/material_mayor.html', {
            'form': form,
            'search_result': search_result,
        }, 
        context_instance=RequestContext(request))
