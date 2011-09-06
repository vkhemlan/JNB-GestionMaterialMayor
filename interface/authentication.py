import urllib2
from django.contrib.auth.models import User
from xml.dom.minidom import parseString
from django.conf import settings
from interface.utils import log

class JnbAuthenticationBackend:
    supports_object_permissions = False
    supports_anonymous_user = False

    def authenticate(self, username=None, password=None):
        
        log("Login in user '%s' with password '%s'" % 
            (username, password))
        request_body = u'username=%s&password=%s' % (username, password)
        request = urllib2.Request(
            url='%s/services/login/' % settings.JNB_WEBSERVICES_URL, 
            data=request_body, 
            headers={
                'Content-Type': 'application/x-www-form-urlencoded', 
                'Accept':'application/xml'})
        f = urllib2.urlopen(request)
        xml_data = parseString(f.read()).childNodes[0]

        user_id = int(JnbAuthenticationBackend.get_xml_node_contents(xml_data, 
            'id'))
        if not user_id:
            log("Username / password of the user do not match")
            return None
        
        '''
        Maximum username length in django is 30
        We assume these are enough characters to identify a user
        '''
        if len(username) > 30:
            log("Username haas more than 30 characters, triming \
                for Django auth system support")
        django_username = username[:30]

        try:
            log("Checking if the user has logged in before")
            user = User.objects.get(username=django_username)
            log("The user has logged in before, using existing entry")
        except User.DoesNotExist:
            '''
            The username is an email
            password as None means that the default auth system will never
            authenticate this user and will rely on ours (which is what we want)
            '''
            log("The user has never logged in before, creating \
                proxy user inside the system")
            user = User.objects.create_user(django_username, 
                email=username, password=None)

        user.first_name = JnbAuthenticationBackend.get_xml_node_contents(
            xml_data, 'nombre')
        user.last_name = JnbAuthenticationBackend.get_xml_node_contents(
            xml_data, 'apellidoPaterno')
        log("Updated user full name: '%s'" % user.get_full_name())
        user.save()
        
        return user

    @staticmethod
    def get_xml_node_contents(xml, node_name):
        '''
        Method that, given an XML object and one of the root's child name, 
        returns its contents
        '''
        return xml.getElementsByTagName(node_name)[0].childNodes[0].nodeValue
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None