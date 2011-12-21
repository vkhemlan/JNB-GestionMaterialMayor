import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from interface.utils import notificar_mantenciones_pendientes

notificar_mantenciones_pendientes()
    
