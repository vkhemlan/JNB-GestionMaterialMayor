from interface.models import MaterialMayor, EventoHojaVidaMaterialMayor
from django.http import Http404, HttpResponse

def descargar_documento_material_mayor(request, material_mayor_id, field_name, extension):
    material_mayor = MaterialMayor.objects.get(pk=material_mayor_id)
    if not request.user.is_authenticated() or not request.user.get_profile().may_access_material_mayor(material_mayor):
        raise Http404
        
    document = getattr(material_mayor, field_name).file.read()
    response = HttpResponse(document, mimetype='application/force-download')
    return response
        
def descargar_documento_evento_material_mayor(request, material_mayor_id, evento_id, field_name, extension):
    material_mayor = MaterialMayor.objects.get(pk=material_mayor_id)
    evento = EventoHojaVidaMaterialMayor.objects.get(pk=evento_id).get_polymorphic_instance()
    
    if evento.material_mayor != material_mayor:
        raise Http404
    if not request.user.is_authenticated() or not request.user.get_profile().may_access_material_mayor(material_mayor):
        raise Http404
        
    document = getattr(evento, field_name).file.read()
    response = HttpResponse(document, mimetype='application/force-download')
    return response
        
def descargar_fotografia_material_mayor(request, material_mayor_id, field_name, extension):
    material_mayor = MaterialMayor.objects.get(pk=material_mayor_id)
    if not request.user.is_authenticated() or not request.user.get_profile().may_access_material_mayor(material_mayor):
        raise Http404
        
    picture = getattr(material_mayor, field_name).file.read()
    response = HttpResponse(picture, mimetype='image/%s' % extension)
    
    return response
    
def descargar_documento_adquisicion_material_mayor(request, material_mayor_id, field_name, extension):
    material_mayor = MaterialMayor.objects.get(pk=material_mayor_id)
    if not request.user.is_authenticated() or not request.user.get_profile().may_access_material_mayor(material_mayor):
        raise Http404
        
    document = getattr(material_mayor.adquisicion.get_polymorphic_instance(), field_name).file.read()
    response = HttpResponse(document, mimetype='application/force-download')
    return response
