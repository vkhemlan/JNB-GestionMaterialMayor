import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from interface.utils import update_data_from_webservice, notificar_mantenciones_pendientes

update_data_from_webservice()
notificar_mantenciones_pendientes()
    
