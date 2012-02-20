try:
    import json
except ImportError:
    import simplejson as json
from django.http import HttpResponse
from django.core import serializers
from interface.models import ModeloChasisMaterialMayor, ModeloCajaCambioMaterialMayor, ModeloBombaMaterialMayor

def part_model_list(request):
    part_name = request.GET['part_name']
    brand_id = request.GET['brand_id']
    conversion_dict = {
        'chasis': ModeloChasisMaterialMayor,
        'caja_cambio': ModeloCajaCambioMaterialMayor,
        'bomba': ModeloBombaMaterialMayor
    }
    class_ = conversion_dict[part_name]
    result = [[model.id, unicode(model), model.marca.id] for model in class_.objects.filter(marca__id=brand_id)]
    
    mimetype = 'application/javascript'
    data = json.dumps(result)
    return HttpResponse(data, mimetype)
    
