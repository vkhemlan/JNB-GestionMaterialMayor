from django.shortcuts import render_to_response
from django.template import RequestContext
from interface.models import Cuerpo
from interface.forms import FormularioAdquisicionCompraMaterialMayor, FormularioAdquisicionDonacionMaterialMayor, MaterialMayorSearchForm, FormularioDarDeAltaMaterialMayor

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

def adquisicion_compra_material_mayor(request):
    if request.method == 'POST':
        form = FormularioDarDeAltaMaterialMayor(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            request.flash['success'] = 'Material mayor dado de alta exitosamente'
    else:
        form = FormularioDarDeAltaMaterialMayor()
        form_adquisicion = FormularioAdquisicionCompraMaterialMayor()

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
        if form.is_valid():
            form.save()
            request.flash['success'] = 'Material mayor dado de alta exitosamente'
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
