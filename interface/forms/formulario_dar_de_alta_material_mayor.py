from django.forms import ModelForm
from interface.models import MaterialMayor

class FormularioDarDeAltaMaterialMayor(ModelForm):
	class Meta:
		model = MaterialMayor
		fields = ('tipo_vehiculo', 'marca_chasis', 'modelo_chasis', 
			'numero_chasis', 'numero_motor', 'placa_patente', 'ano_vehiculo',
			'color')