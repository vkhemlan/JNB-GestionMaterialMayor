from django.db import models
from django.db.models.signals import post_save  
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import loader, Context
from interface.utils import log, request_webservice, get_xml_node_contents, get_xml_node_children, get_xml_node_attribute
from django.conf import settings
from interface.utils import intersect
from . import Rol

class UserProfile(models.Model):  
    user = models.OneToOneField(User)  
    webservice_id = models.IntegerField(blank=True, null=True)
    rol = models.ForeignKey('Rol', blank=True, null=True)
    cargos = models.ManyToManyField('Cargo', blank=True, null=True)
    cuerpo = models.ForeignKey('Cuerpo', blank=True, null=True)

    @classmethod
    def get_usuarios_operaciones(cls):
        return UserProfile.objects.filter(rol=Rol.OPERACIONES())

    def enviar_recordatorio_mantenciones_pendientes(self):
        t = loader.get_template('mails/resumen_mantenciones_pendientes.html')
        c = Context({'usuario': self.user, 'SITE_URL': settings.SITE_URL})
        self.user.email_user('Mantenciones pendientes de material mayor', t.render(c))
    
    def is_comandante(self):
        return settings.CARGOS_CUERPO['Comandante'] in [cargo.webservice_id for cargo in self.cargos.all()]

    def is_inspector_de_material_mayor(self):
        return settings.CARGOS_CUERPO['Inspector de Material Mayor'] in [cargo.webservice_id for cargo in self.cargos.all()]
        
    def is_staff_cuerpo(self):
        # Si el usuario tiene un rol significa que trabaja en la JNB
        if self.rol:
            return False
            
        cargo_ids = [cargo.webservice_id for cargo in self.cargos.all()]
        
        # Para que el usuario sea considerado staff de cuerpo alguno de sus cargos
        # tiene que estar en el listado de cargos con permisos en el sistema.
        return intersect(cargo_ids, settings.CARGOS_CUERPO.values())

    def puede_asignar_solicitud_de_primera_inscripcion(self):
        if self.user.is_superuser:
            return True
        if self.rol == Rol.OPERACIONES():
            return True
        return False
        
    def puede_validar_material_mayor(self):
        if self.user.is_superuser:
            return True
        if self.rol == Rol.OPERACIONES():
            return True
        return False

    def puede_asignar_certificado_de_anotaciones_vigentes(self):
        if self.user.is_superuser:
            return True
        if self.rol == Rol.OPERACIONES():
            return True
        return False
        
    def is_staff_jnbc(self):
        return bool(self.rol)
        
    def puede_asignar_patente(self):
        if self.user.is_superuser:
            return True
        if self.rol == Rol.OPERACIONES():
            return True
        if self.is_comandante():
            return True
        return False
        
    def puede_asignar_pauta_de_mantenimiento_de_carrosado(self):
        if self.user.is_superuser:
            return True
        if self.rol == Rol.OPERACIONES():
            return True
        return False
        
    def puede_eliminar_material_mayor(self):
        if self.user.is_superuser:
            return True
        if self.rol == Rol.OPERACIONES():
            return True
        return False
        
    def puede_cambiar_numero_chasis_material_mayor(self):
        if self.user.is_superuser:
            return True
        if self.rol == Rol.OPERACIONES():
            return True
        return False
        
    def puede_cambiar_numero_motor_material_mayor(self):
        if self.user.is_superuser:
            return True
        if self.rol == Rol.OPERACIONES():
            return True
        return False

    def puede_dar_de_baja_material_mayor(self):
        if self.user.is_superuser:
            return True
        if self.rol == Rol.OPERACIONES():
            return True
        return False
        
    def __str__(self):  
          return '%s\'s profile' % self.user
          
    def generate_menu(self):
        c = Context()
        if self.rol:
            t = loader.get_template('menus/%s.html' % (self.rol.nombre.lower()))
        elif self.is_comandante():
            t = loader.get_template('menus/comandante.html')
        elif self.is_inspector_de_material_mayor():
            t = loader.get_template('menus/inspector_de_material_mayor.html')
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
        
    def may_access_material_mayor(self, material_mayor):
        # Si el usuario es administrador
        if self.user.is_superuser:
            return True
        # Si el usuario trabaja en la JNBC
        if self.is_staff_jnbc():
            return True
        # Si el usuario trabaja en un cuerpo y el material mayor esta actualmente asignado a ese cuerpo
        if self.is_staff_cuerpo() and self.cuerpo == material_mayor.cuerpo:
            return True
        # Si el usuario trabaja en un cuerpo y el material aun no ha sido asignado, pero que el cuerpo del usuario
        # es el destinatario original del material
        if self.is_staff_cuerpo() and not material_mayor.cuerpo and material_mayor.adquisicion.cuerpo_destinatario == self.cuerpo:
            return True
        return False

    class Meta:
        app_label = 'interface'


def create_user_profile(sender, instance, created, **kwargs):
    if created:  
       profile, created = UserProfile.objects.get_or_create(user = instance)  

post_save.connect(create_user_profile, sender = User) 
