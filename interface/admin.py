import models
from django.contrib import admin

admin.site.register(models.TipoVehiculoMaterialMayor)
admin.site.register(models.MarcaChasisMaterialMayor)
admin.site.register(models.ModeloChasisMaterialMayor)
admin.site.register(models.MarcaCarrosadoMaterialMayor)
admin.site.register(models.MarcaCajaCambioMaterialMayor)
admin.site.register(models.ModeloCajaCambioMaterialMayor)
admin.site.register(models.ColorMaterialMayor)
admin.site.register(models.CondicionMaterialMayor)
admin.site.register(models.MaterialMayor)
admin.site.register(models.TipoCombustibleMaterialMayor)
admin.site.register(models.TipoCajaCambioMaterialMayor)
admin.site.register(models.MarcaBombaMaterialMayor)
admin.site.register(models.ModeloBombaMaterialMayor)
admin.site.register(models.Pais)
admin.site.register(models.AdquisicionMaterialMayor)
admin.site.register(models.AdquisicionCompraMaterialMayor)
admin.site.register(models.AdquisicionDonacionMaterialMayor)
admin.site.register(models.ModoAdquisicionMaterialMayor)
admin.site.register(models.Region)
admin.site.register(models.Provincia)
admin.site.register(models.Comuna)
admin.site.register(models.Cuerpo)
admin.site.register(models.Compania)
admin.site.register(models.EventoHojaVidaMaterialMayor)
admin.site.register(models.TipoEventoHojaVidaMaterialMayor)
admin.site.register(models.AsignacionCuerpoMaterialMayor)
admin.site.register(models.AsignacionCompaniaMaterialMayor)
admin.site.register(models.AsignacionPatenteMaterialMayor)
admin.site.register(models.UserProfile)
admin.site.register(models.Rol)
admin.site.register(models.Cargo)

admin.site.register(models.FamiliaUsoMaterialMayor)

class UsoMaterialMayorAdmin(admin.ModelAdmin):
    exclude = ('is_others_option',)
    
admin.site.register(models.UsoMaterialMayor, UsoMaterialMayorAdmin)

admin.site.register(models.FrecuenciaOperacion)
admin.site.register(models.PautaMantencion)
admin.site.register(models.PautaMantencionChasis)
admin.site.register(models.PautaMantencionCarrosado)
admin.site.register(models.OperacionMantencion)
admin.site.register(models.CambioPautaMantencionCarrosadoMaterialMayor)
admin.site.register(models.CambioNumeroChasisMaterialMayor)
admin.site.register(models.CambioNumeroMotorMaterialMayor)
