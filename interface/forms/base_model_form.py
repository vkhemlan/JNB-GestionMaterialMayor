# coding: utf-8

from django.forms import ModelForm
from django.template import loader, Context
from django.core.urlresolvers import reverse
from django.conf import settings

class BaseModelForm(ModelForm):
    """
    Clase que envuelve a ModelForm agregando nuevas funcionalidades para formularios
    extensos que se basan en modelos, por ejemplo para obtener de forma directa un "rango
    de campos" del formulario en vez de accederlos uno por uno.
    """

    def __init__(self, *args, **kwargs):
        """
        El constructor es sobreescrito para recibir obligatoriamente un parámetro "user" correspondiente al usuario
        actualmente ingresado al sistema. Este parámetro es necesario porque la representación del formulario
        depende de los permisos que tenga el usuario basado en su rol o cargo.
        """
        self.user = kwargs['user']
        del kwargs['user']
        
        super(BaseModelForm, self).__init__(*args, **kwargs)


    def _field_range(self, start_field_name, end_field_name):
        """
        Método que retorna un listado de campos del formulario desde "start_field_name" hasta "end_field_name"
        basándose en el orden establecido en el formulario propiamente tal.

        Si start_field_name no existe entre los campos del formulario, el método retorna una lista vacía
        Si end_field_name no existe entre los campos del formulario, el método retorna todos los campos desde
        start_field_name hasta el final, a menos que start_field_name no exista.

        El método es útil para representar un "slice" de los campos de un formulario como HTML.
        """
        fields = self.fields.items()
        return_fields = []
        
        indexing = False
        
        for idx, field in enumerate(fields):
            if field[0] == start_field_name:
                indexing = True
                
            if indexing:
                return_fields.append(field[0])
                
            if field[0] == end_field_name:
                indexing = False
                
        return [self[field] for field in return_fields]
        
    def _render_fields_as_list(self, fields, blacklist=None):
        """
        Método que retorna un HTML que representa una parte del formulario definida por los campos recibidos como
        argumentos. Si el usuario tiene los permisos necesarios el formulario incluirá botones para agregar nuevas
        opciones a los combobox usando el admin de Django a menos que esos campos estén en el argumento "blacklist"
        """
        if not blacklist: blacklist = []
        template = loader.get_template('tags/field_list.html')
        errors = self._combine_fields_errors(fields)
        
        for field in fields:
            if field.field.__class__.__name__ == 'ModelChoiceField' and field.name not in blacklist and self.user.is_staff:
                field.admin_url = reverse('admin:interface_%s_add' % (field.field.queryset.model.__name__.lower()))
            else:
                field.admin_url = None

        c = Context({
            'fields': fields,
            'errors': errors,
            'STATIC_URL': settings.STATIC_URL
        })

        return template.render(c)

    def _combine_fields_errors(self, fields):
        """
        Método que combina los posibles errores en un conjunto de campos del formularios en un solo arreglo.
        Útil para cuando uno representa una "tabla" de campos y no tiene espacio para mostrar los errores sobre
        sus respectivas celdas, por lo que conviene mostrar los errores juntos en la cabecera de la tabla.
        """
        errors = []
        for field in fields:
            errors.extend(field.errors)
        return errors
