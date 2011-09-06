import logging
from django.conf import settings

def log(message):
	logger = logging.getLogger(settings.PROJECT_MODULE)
	logger.info(message)
