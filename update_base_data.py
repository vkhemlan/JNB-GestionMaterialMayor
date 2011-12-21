import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from interface.utils import update_data_from_webservice

update_data_from_webservice()
    
