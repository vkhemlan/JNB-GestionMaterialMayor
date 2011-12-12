import logging
from django.conf import settings
from xml.dom.minidom import parseString
from django.core.mail import send_mail
import urllib2
from django.template import loader
from django.template.context import Context
import re

def log(message):
    logger = logging.getLogger(settings.PROJECT_MODULE)
    logger.info(message)

def notificar_mantenciones_pendientes():
    from interface.models.mantencion_programada import MantencionProgramada
    from interface.models import UserProfile

    mantenciones_pendientes = MantencionProgramada.get_pendientes()

    if not mantenciones_pendientes:
        return

    for usuario in UserProfile.get_usuarios_operaciones():
        usuario.enviar_recordatorio_mantenciones_pendientes()

    ids_cuerpos_con_mantenciones_pendientes = set()

    for mantencion_pendiente in mantenciones_pendientes:
        if mantencion_pendiente.material_mayor.cuerpo:
            ids_cuerpos_con_mantenciones_pendientes.add(mantencion_pendiente.material_mayor.cuerpo.webservice_id)

    encargados_raw_data = request_webservice('/services/usuarios/encargados_de_material_mayor/')
    encargados_raw_data_list = encargados_raw_data.childNodes

    encargados_material_mayor_por_notificar = []

    for raw_encargado in encargados_raw_data_list:
        cuerpo_id = int(get_xml_node_attribute(raw_encargado, 'cuerpo', 'id'))
        if cuerpo_id in ids_cuerpos_con_mantenciones_pendientes:
            encargados_material_mayor_por_notificar.append([raw_encargado, cuerpo_id])

    for encargado_material_mayor, cuerpo_id in encargados_material_mayor_por_notificar:
        webservice_url = '/services/usuario/%s/correos/' % (get_xml_node_contents(encargado_material_mayor, 'id'),)
        correos_raw_data = request_webservice(webservice_url)

        for correo_raw_data in correos_raw_data.childNodes:
            email = get_xml_node_contents(correo_raw_data, 'username')

            first_name = get_xml_node_contents(encargado_material_mayor, 'nombre')
            apellido = get_xml_node_contents(encargado_material_mayor, 'apellidoPaterno')

            full_name = first_name + ' ' + apellido

            t = loader.get_template('mails/resumen_mantenciones_pendientes_cuerpo.html')
            c = Context({'usuario': full_name, 'SITE_URL': settings.SITE_URL})

            if settings.DEBUG:
                email = 'vkhemlan@gmail.com'
                
            send_mail('Mantenciones pendientes de material mayor', t.render(c), settings.EMAIL_HOST_USER, [email])

def update_data_from_webservice():
    from models import Region, Provincia, Comuna, Cuerpo, Compania
    for layer in [Region, Provincia, Comuna, Cuerpo, Compania]:
        layer.update_from_webservice()

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
    """
    Method that, given an XML object and one of the root's child name, 
    returns its contents
    """
    return xml.getElementsByTagName(node_name)[0].childNodes[0].nodeValue

def get_xml_node_attribute(xml, node_name, attribute_name):
    return xml.getElementsByTagName(node_name)[0].attributes.get(attribute_name).value
    
def get_xml_node_children(xml, node_name):
    return xml.getElementsByTagName(node_name)
    
def convert_camelcase_to_lowercase(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    
def intersect(a, b):
     return bool(set(a) & set(b))
     
def remove_deleted_fields_from_data(data, prefix):
    total_forms = int(data['%s-TOTAL_FORMS' % prefix])
    
    return_data = {}
    insertion_index = 0
    new_initial_count = 0
    
    for i in range(total_forms):
        base_pattern = '%s-%d' % (prefix, i)
        if '%s-DELETE' % base_pattern not in data:
            for key, value in data.items():
                if base_pattern in key:
                    new_key = re.sub(r'^(%s-)\d+(-.+)$' % prefix, r'\1%d\2', key) % insertion_index
                    return_data[new_key] = value
                    if key == '%s-id' % base_pattern and value:
                        new_initial_count += 1
            insertion_index += 1
                        
    return_data['%s-TOTAL_FORMS' % prefix] = insertion_index
    return_data['%s-MAX_NUM_FORMS' % prefix] = data['%s-MAX_NUM_FORMS' % prefix]
    return_data['%s-INITIAL_FORMS' % prefix] = new_initial_count
    return return_data
