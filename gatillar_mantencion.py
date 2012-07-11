import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'JNB-GestionMaterialMayor.settings'

from interface.models import *
from interface.utils import notificar_mantenciones_pendientes

material_mayor = MaterialMayor.objects.get(pk=5)
material_mayor.gatillar_operaciones_mantencion_manualmente(12)
notificar_mantenciones_pendientes()
    
