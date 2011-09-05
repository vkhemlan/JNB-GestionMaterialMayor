import urllib2
from django.contrib.auth.models import User
from xml.dom.minidom import parseString

class JnbAuthenticationBackend:
    supports_object_permissions = False
    supports_anonymous_user = False

    def authenticate(self, username=None, password=None):
        request_body = u'username=%s&password=%s' % (username, password)
        request = urllib2.Request(url='http://localhost:8080/JnbWebServices/services/login/', 
            data=request_body, 
            headers={'Content-Type': 'application/x-www-form-urlencoded', 'Accept':'application/xml'})
        f = urllib2.urlopen(request)
        xml_data = parseString(f.read()).childNodes[0]

        user_id = int(get_xml_node_contents(xml_data, 'id'))
        if not user_id:
            return None
        user = User.objects.create_user(username, email=username, password=password)
        user.first_name = get_xml_node_contents(xml_data, 'nombre')
        user.last_name = get_xml_node_contents(xml_data, 'apellidoPaterno')
        user.save()
        
        return user

    @staticmethod
    def get_xml_node_contents(xml_data, node_name):
        '''
        Method that, given an XML object and one of the root's child name, returns its contents
        '''
        return xml_data.getElementsByTagName(node_name)[0].childNodes[0].nodeValue
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None