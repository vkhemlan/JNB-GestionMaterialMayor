from interface.models import MaterialMayor, EventoHojaVidaMaterialMayor
from django.http import Http404, HttpResponse
from authentication import authorize_material_mayor_access
from django.contrib.auth.decorators import login_required
from interface.models.archivo_mantencion_programada import ArchivoMantencionProgramada
from interface.models.mantencion_programada import MantencionProgramada

@authorize_material_mayor_access(requiere_validacion_operaciones=False, requiere_material_en_servicio=False)
def descargar_documento_material_mayor(request, material_mayor, field_name, extension):
    document = getattr(material_mayor, field_name).file.read()
    response = HttpResponse(document, mimetype='application/force-download')
    return response

@authorize_material_mayor_access(requiere_validacion_operaciones=False, requiere_material_en_servicio=False)
def descargar_documento_evento_material_mayor(request, material_mayor, evento_id, field_name, extension):
    evento = EventoHojaVidaMaterialMayor.objects.get(pk=evento_id).get_polymorphic_instance()
    
    if evento.material_mayor != material_mayor:
        raise Http404
        
    document = getattr(evento, field_name).file.read()
    response = HttpResponse(document, mimetype='application/force-download')
    return response

@authorize_material_mayor_access(requiere_validacion_operaciones=False, requiere_material_en_servicio=False)
def descargar_fotografia_material_mayor(request, material_mayor, field_name, extension):
    picture = getattr(material_mayor, field_name).file.read()
    response = HttpResponse(picture, mimetype='image/%s' % extension)
    
    return response

@authorize_material_mayor_access(requiere_validacion_operaciones=False, requiere_material_en_servicio=False)
def descargar_documento_adquisicion_material_mayor(request, material_mayor, field_name, extension):
    document = getattr(material_mayor.adquisicion.get_polymorphic_instance(), field_name).file.read()
    response = HttpResponse(document, mimetype='application/force-download')
    return response

@authorize_material_mayor_access(requiere_validacion_operaciones=True, requiere_material_en_servicio=False)
def descargar_documento_mantencion_programada_material_mayor(request, material_mayor, mantencion_id,  archivo_id, extension):
    archivo = ArchivoMantencionProgramada.objects.get(pk=archivo_id)
    mantencion = MantencionProgramada.objects.get(pk=mantencion_id)
    if mantencion.material_mayor != material_mayor or archivo.mantencion != mantencion:
        raise Http404
    response = HttpResponse(archivo.archivo.read(), mimetype='application/force-download')
    return response