import logging
from django.conf import settings
from xml.dom.minidom import parseString
import urllib2

def log(message):
    logger = logging.getLogger(settings.PROJECT_MODULE)
    logger.info(message)

def request_webservice(service_location, data=None):
    request = urllib2.Request(
        url='%s%s' % (settings.JNB_WEBSERVICES_URL, service_location,), 
        data=data, 
        headers={
            'Content-Type': 'application/x-www-form-urlencoded', 
            'Accept':'application/xml'})
    f = urllib2.urlopen(request)
    xml_data = parseString(f.read())
    return xml_data.childNodes[0]
    
def get_xml_node_contents(xml, node_name):
    '''
    Method that, given an XML object and one of the root's child name, 
    returns its contents
    '''
    return xml.getElementsByTagName(node_name)[0].childNodes[0].nodeValue
