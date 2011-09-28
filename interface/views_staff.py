# coding: utf-8

from django.shortcuts import render_to_response
from django.template import RequestContext
from interface.models import Cuerpo, MaterialMayor, AdquisicionCompraMaterialMayor, AdquisicionDonacionMaterialMayor, TipoEventoHojaVidaMaterialMayor, EventoHojaVidaMaterialMayor
from django.core.urlresolvers import reverse
from interface.forms import FormularioAdquisicionCompraMaterialMayor, FormularioAdquisicionDonacionMaterialMayor, MaterialMayorSearchForm, FormularioDarDeAltaMaterialMayor, FormularioAsignacionCuerpoMaterialMayor
from django.http import HttpResponseRedirect
from interface.utils import convert_camelcase_to_lowercase

def _index(request):
    return render_to_response('staff/index.html', {}, 
                                context_instance=RequestContext(request))
                                
def adquisicion_compra_material_mayor(request):
    if request.method == 'POST':
        form = FormularioDarDeAltaMaterialMayor(request.POST, request.FILES)
        form_adquisicion = FormularioAdquisicionCompraMaterialMayor(request.POST, request.FILES)
        if form.is_valid() and form_adquisicion.is_valid():
            adquisicion = form_adquisicion.instance
            adquisicion.usuario = request.user
            adquisicion.save()
            material_mayor = form.instance
            material_mayor.adquisicion = adquisicion
            material_mayor.save()
            request.flash['success'] = 'Material mayor dado de alta exitosamente'
            url = reverse('interface.views_staff.material_mayor_sin_asignar')
            return HttpResponseRedirect(url)
    else:
        form_adquisicion = FormularioAdquisicionCompraMaterialMayor()
        form = FormularioDarDeAltaMaterialMayor()

    return render_to_response(
        'staff/adquisicion_compra_material_mayor.html', 
        {
            'form': form,
            'form_adquisicion': form_adquisicion,
        }, 
        context_instance=RequestContext(request))   

def adquisicion_donacion_material_mayor(request):
    if request.method == 'POST':
        form = FormularioDarDeAltaMaterialMayor(request.POST, request.FILES)
        form_adquisicion = FormularioAdquisicionDonacionMaterialMayor(request.POST, request.FILES)
        if form.is_valid() and form_adquisicion.is_valid():
            adquisicion = form_adquisicion.instance
            adquisicion.usuario = request.user
            adquisicion.save()
            material_mayor = form.instance
            material_mayor.adquisicion = adquisicion
            material_mayor.save()
            request.flash['success'] = 'Material mayor dado de alta exitosamente'
            url = reverse('interface.views_staff.material_mayor_sin_asignar')
            return HttpResponseRedirect(url)
    else:
        form = FormularioDarDeAltaMaterialMayor()
        form_adquisicion = FormularioAdquisicionDonacionMaterialMayor()

    return render_to_response(
        'staff/adquisicion_donacion_material_mayor.html', 
        {
            'form': form,
            'form_adquisicion': form_adquisicion,
        }, 
        context_instance=RequestContext(request))  
                                
def material_mayor_sin_asignar(request):
    material_mayor = MaterialMayor.objects.filter(cuerpo__isnull=True)
    return render_to_response('staff/material_mayor_sin_asignar.html', {
            'material_mayor': material_mayor
        }, 
        context_instance=RequestContext(request))

def editar_material_mayor(request, material_mayor_id):
    material_mayor = MaterialMayor.objects.get(pk=material_mayor_id)
    if request.method == 'POST':
        form = FormularioDarDeAltaMaterialMayor(request.POST, request.FILES, instance=material_mayor)
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
            url = reverse('interface.views_staff.editar_material_mayor', args=[material_mayor.id])
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
            url = reverse('interface.views_staff.editar_material_mayor', args=[material_mayor.id])
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
