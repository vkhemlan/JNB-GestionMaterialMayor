# coding: utf-8

from django.shortcuts import render_to_response
from django.template import RequestContext
from interface.models import Cuerpo, MaterialMayor, AdquisicionCompraMaterialMayor, AdquisicionDonacionMaterialMayor
from django.core.urlresolvers import reverse
from interface.forms import FormularioAdquisicionCompraMaterialMayor, FormularioAdquisicionDonacionMaterialMayor, MaterialMayorSearchForm, FormularioDarDeAltaMaterialMayor
from django.http import HttpResponseRedirect

def _index(request):
    return render_to_response('staff/index.html', {}, 
                                context_instance=RequestContext(request))
                                
def material_mayor(request):
    form = MaterialMayorSearchForm(request.GET)
    search_result = form.get_filtered_material_mayor()
    return render_to_response('staff/material_mayor.html', {
            'form': form,
            'search_result': search_result,
        }, 
        context_instance=RequestContext(request))

def material_mayor_details(request, material_mayor_id):
    material_mayor = MaterialMayor.objects.get(pk=material_mayor_id)
    if request.method == 'POST':
        form = FormularioDarDeAltaMaterialMayor(request.POST, request.FILES, instance=material_mayor)
        if form.is_valid():
            material_mayor = form.instance
            material_mayor.save()
            request.flash['success'] = 'Material mayor actualizado exitosamente'
            url = reverse('interface.views_staff.material_mayor')
            return HttpResponseRedirect(url)
    else:
        form = FormularioDarDeAltaMaterialMayor.get_from_instance(material_mayor)
    
    return render_to_response('staff/material_mayor_details.html', {
            'form': form,
        }, 
        context_instance=RequestContext(request))
        
def material_mayor_adquisicion_details(request, material_mayor_id):
    material_mayor = MaterialMayor.objects.get(pk=material_mayor_id)
    adquisicion = material_mayor.adquisicion.get_polymorphic_instance()
    Form = eval('Formulario%s' % (adquisicion.__class__.__name__))
    if request.method == 'POST':
        form = Form(request.POST, request.FILES, instance=adquisicion)
        if form.is_valid():
            adquisicion = form.instance
            adquisicion.save()
            request.flash['success'] = u'Datos de adquisición actualizados exitosamente'
            url = reverse('interface.views_staff.material_mayor_details', args=[material_mayor.id])
            return HttpResponseRedirect(url)
    else:
        form = Form(instance=adquisicion)
    
    return render_to_response('staff/material_mayor_adquisicion_details.html', {
            'form': form,
        }, 
        context_instance=RequestContext(request))
        
def adquisicion_compra_material_mayor(request):
    if request.method == 'POST':
        form = FormularioDarDeAltaMaterialMayor(request.POST, request.FILES)
        form_adquisicion = FormularioAdquisicionCompraMaterialMayor(request.POST, request.FILES)
        if form.is_valid() and form_adquisicion.is_valid():
            adquisicion = form_adquisicion.instance
            adquisicion.save()
            material_mayor = form.instance
            material_mayor.adquisicion = adquisicion
            material_mayor.save()
            request.flash['success'] = 'Material mayor dado de alta exitosamente'
            url = reverse('interface.views_staff.material_mayor')
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
            adquisicion.save()
            material_mayor = form.instance
            material_mayor.adquisicion = adquisicion
            material_mayor.save()
            request.flash['success'] = 'Material mayor dado de alta exitosamente'
            url = reverse('interface.views_staff.material_mayor')
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
