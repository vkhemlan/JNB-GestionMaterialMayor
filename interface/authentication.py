# coding: utf-8

import urllib2
from functools import wraps
from django.core.urlresolvers import reverse
from utils import log
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from interface.models import UserProfile, MaterialMayor
from interface.utils import log, request_webservice, get_xml_node_contents, intersect

class authorize_material_mayor_access(object):
    def __init__(self, requiere_validacion_operaciones):
        self.requiere_validacion_operaciones = requiere_validacion_operaciones

    def __call__(self, func):
        @wraps(func)
        def wrap(request, *args, **kwargs):
            material_mayor = MaterialMayor.objects.get(pk=kwargs['material_mayor'])
            if not request.user.get_profile().may_access_material_mayor(material_mayor):
                request.flash['error'] = u'Error de acceso'
                return redirect('index')
            if self.requiere_validacion_operaciones and not material_mayor.validado_por_operaciones:
                request.flash['error'] = u'El material aún no ha sido validado por la JNBC'
                url = reverse('interface.views.editar_material_mayor', args=[material_mayor.id])
                return redirect(url)
            else:
                kwargs['material_mayor'] = material_mayor
                return func(request, *args, **kwargs)

        return wrap
        
# Check if user has the role required to the decorated view
class authorize(object):
    def __init__(self, roles=(), cargos=()):
        self.roles = roles
        self.cargos = cargos

    def __call__(self, func):
        @wraps(func)
        def wrap(request, *args, **kwargs):
            # If it is the superuser, allow everything
            if request.user.is_superuser:
                return func(request, *args, **kwargs)    
        
            # If user isn't authenticated
            if not request.user.is_authenticated():
                log(u'Usuario no autenticado intentó acceder al sistema')
                request.flash['notice'] = u'Por favor inicie sesión primero'
                return redirect('login')
                
            user_cargo_ids = [cargo.webservice_id for cargo in request.user.get_profile().cargos.all()]
                
            # If the user role is not in allowed roles, deny
            if not request.user.get_profile().rol in self.roles and not intersect(user_cargo_ids, self.cargos):
                log(u'Usuario autenticado intentó acceder a sección no permitida del sistema')
                request.flash['error'] = u'Error de acceso'
                return redirect('index')

            return func(request, *args, **kwargs)

        return wrap

class JnbAuthenticationBackend:
    supports_object_permissions = False
    supports_anonymous_user = False

    def authenticate(self, username=None, password=None):
        
        log("Login in user '%s' with password '%s'" % 
            (username, password))

        request_body = u'username=%s&password=%s' % (username, password)

        xml_data = request_webservice('/services/login/', request_body)
        user_id = int(get_xml_node_contents(xml_data, 
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
            user = UserProfile.objects.get(webservice_id=user_id).user
            log("The user has logged in before, using existing entry")
        except UserProfile.DoesNotExist:
            '''
            The username is an email
            password as None means that the default auth system will never
            authenticate this user and will rely on ours (which is what we want)
            '''
            log("The user has never logged in before, creating \
                proxy user inside the system")
            user = User.objects.create_user(django_username, 
                email=username, password=None)
        
        user.get_profile().update(django_username, xml_data)
        
        return user
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
