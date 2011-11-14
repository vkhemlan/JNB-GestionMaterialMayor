# coding: utf-8

from django.db import models

class Rol(models.Model):
    nombre = models.CharField(max_length = 255)
    
    @classmethod
    def OPERACIONES(cls):
        return cls.objects.get(nombre='Operaciones')
        
    @classmethod
    def ADQUISICIONES(cls):
        return cls.objects.get(nombre='Adquisiciones')
    
    @classmethod
    def JURIDICA(cls):
        return cls.objects.get(nombre='Juridica')

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']
        app_label = 'interface'
        verbose_name = u'Rol'
        verbose_name_plural = u'Roles'
