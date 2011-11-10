# coding: utf-8

from . import EventoHojaVidaMaterialMayor

class EjecucionOperacionMantencionProgramada(EventoHojaVidaMaterialMayor):

    def quick_details(self):
        return u'Mantención programada: %s' % unicode(self.operacionmantencionprogramada)
        
    def breadcrumb_details(self):
        return unicode(self.operacionmantencionprogramada)
        
    def title_details(self):
        return u'Mantención programada: %s' % unicode(self.operacionmantencionprogramada)

    class Meta:
        app_label = 'interface'
        verbose_name = u'Ejecución de mantención programada'
        verbose_name_plural = u'Ejecuciones de mantención programada'
