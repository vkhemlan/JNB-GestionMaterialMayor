from django.db import models
from django.db.models.signals import post_save  
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import loader, Context
from interface.utils import log, request_webservice, get_xml_node_contents, get_xml_node_children, get_xml_node_attribute
from django.conf import settings
from interface.utils import intersect

class UserProfile(models.Model):  
    user = models.OneToOneField(User)  
    webservice_id = models.IntegerField(blank=True, null=True)
    rol = models.ForeignKey('Rol', blank=True, null=True)
    cargos = models.ManyToManyField('Cargo', blank=True, null=True)
    cuerpo = models.ForeignKey('Cuerpo', blank=True, null=True)
    
    def is_comandante(self):
        return settings.CARGOS_CUERPO['Comandante'] in [cargo.webservice_id for cargo in self.cargos.all()]
        
    def is_staff_cuerpo(self):
        # Si el usuario tiene un rol significa que trabaja en la JNB
        if self.rol:
            return False
            
        cargo_ids = [cargo.webservice_id for cargo in self.cargos.all()]
        
        # Para que el usuario sea considerado staff de cuerpo alguno de sus cargos
        # tiene que estar en el listado de cargos con permisos en el sistema.
        return intersect(cargo_ids, settings.CARGOS_CUERPO.values())
        
    def is_staff_jnbc(self):
        return bool(self.rol)

    def __str__(self):  
          return '%s\'s profile' % self.user
          
    def generate_menu(self):
        c = Context()
        if self.rol:
            t = loader.get_template('menus/%s.html' % (self.rol.nombre.lower()))
        elif self.is_comandante():
            t = loader.get_template('menus/comandante.html')
        else:
            t = loader.get_template('menus/default.html')
        return t.render(c)
        
    def send_new_dada_de_alta_email(self, material_mayor):
        t = loader.get_template('mails/new_dada_de_alta.html')
        c = Context({'material_mayor': material_mayor, 'usuario': self.user, 'SITE_URL': settings.SITE_URL})
        self.user.email_user('Nuevo material mayor dado de alta', t.render(c))
            
    def update(self, username, xml_data):
        from . import Cargo, Cuerpo
    
        log('Actualizando datos de usuario: %s' % (unicode(self.user)))
        
        self.user.first_name = get_xml_node_contents(
            xml_data, 'nombre')
        self.user.last_name = get_xml_node_contents(
            xml_data, 'apellidoPaterno')
        self.username = username
            
        self.user.save()
        log("Updated user full name: '%s'" % self.user.get_full_name())
            
        self.webservice_id = int(get_xml_node_contents(
            xml_data, 'id'))
            
        cuerpo_id = get_xml_node_attribute(xml_data, 'cuerpo', 'id')
        self.cuerpo = Cuerpo.objects.get(webservice_id=cuerpo_id)
        
        self.save()        
        
        url = '/services/usuario/%d/cargos/' % self.webservice_id
        xml_data = request_webservice(url)
        
        self.cargos.clear()
        
        for cargo_element in get_xml_node_children(xml_data, 'cargo'):
            webservice_id = int(get_xml_node_contents(cargo_element, 'id'))
            nombre = get_xml_node_contents(cargo_element, 'nombre')
            
            try:    
                cargo = Cargo.objects.get(webservice_id=webservice_id)
            except Cargo.DoesNotExist:
                cargo = Cargo()
                cargo.webservice_id = webservice_id
                
            cargo.nombre = nombre
            cargo.save()
            
            self.cargos.add(cargo)
            
        self.save()
        

    class Meta:
        app_label = 'interface'

def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user = instance)  

post_save.connect(create_user_profile, sender = User) 
