from django.forms import ModelForm
from django.template import loader, Context
from django.core.urlresolvers import reverse
from django.conf import settings

class BaseModelForm(ModelForm):
    # Get a range of fields (ordered) between the given field names   
    def _field_range(self, start_field_name, end_field_name):
        fields = self.fields.items()
        return_fields = []
        
        indexing = False;
        
        for idx, field in enumerate(fields):
            if field[0] == start_field_name:
                indexing = True
                
            if indexing:
                return_fields.append(field[0])
                
            if field[0] == end_field_name:
                indexing = False
                
        return [self[field] for field in return_fields]
        
    def _render_fields_as_list(self, fields, blacklist=[]):
        template = loader.get_template('tags/field_list.html')
        errors = self._combine_fields_errors(fields)
        
        for field in fields:
            if field.field.__class__.__name__ == 'ModelChoiceField' and field.name not in blacklist:
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
        errors = []
        for field in fields:
            errors.extend(field.errors)
        return errors
