from django.shortcuts import render_to_response
from django.template import RequestContext

from interface.forms import FormularioAdquisicionCompraMaterialMayor, FormularioAdquisicionDonacionMaterialMayor

def _index(request):
    return render_to_response('staff/index.html', {}, 
                                context_instance=RequestContext(request))

def adquisicion_compra_material_mayor(request):
    if request.method == 'POST':
        form = FormularioAdquisicionCompraMaterialMayor(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            request.flash['success'] = 'Material mayor dado de alta exitosamente'
    else:
        form = FormularioAdquisicionCompraMaterialMayor()

    return render_to_response(
        'staff/adquisicion_compra_material_mayor.html', 
        {
            'form': form
        }, 
        context_instance=RequestContext(request))   

def adquisicion_donacion_material_mayor(request):
    if request.method == 'POST':
        form = FormularioAdquisicionDonacionMaterialMayor(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            request.flash['success'] = 'Material mayor dado de alta exitosamente'
    else:
        form = FormularioAdquisicionDonacionMaterialMayor()

    return render_to_response(
        'staff/adquisicion_donacion_material_mayor.html', 
        {
            'form': form
        }, 
        context_instance=RequestContext(request))  