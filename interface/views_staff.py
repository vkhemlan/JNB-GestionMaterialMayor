from django.shortcuts import render_to_response
from django.template import RequestContext

from interface.forms import FormularioDarDeAltaMaterialMayor

def _index(request):
    return render_to_response('staff/index.html', {}, 
                                context_instance=RequestContext(request))

def dar_de_alta_material_mayor(request):
    if request.method == 'POST':
        form = FormularioDarDeAltaMaterialMayor(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            request.flash['success'] = 'Material mayor dado de alta exitosamente'
    else:
        form = FormularioDarDeAltaMaterialMayor()

    return render_to_response(
        'staff/dar_de_alta_material_mayor.html', 
        {
            'form': form
        }, 
        context_instance=RequestContext(request))   
