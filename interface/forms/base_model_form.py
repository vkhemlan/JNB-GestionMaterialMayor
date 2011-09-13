from django.forms import ModelForm
from django.template import loader, Context

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
        
    def _render_fields_as_list(self, fields):
        template = loader.get_template('tags/field_list.html')
        errors = self._combine_fields_errors(fields)

        c = Context({
            'fields': fields,
            'errors': errors,
        })

        return template.render(c)

    def _combine_fields_errors(self, fields):
        errors = []
        for field in fields:
            errors.extend(field.errors)
        return errors