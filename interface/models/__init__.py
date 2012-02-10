from .frecuencia_operacion import FrecuenciaOperacion
from .pauta_mantencion import PautaMantencion
from .pauta_mantencion_chasis import PautaMantencionChasis
from .pauta_mantencion_carrosado import PautaMantencionCarrosado
from .familia_uso_material_mayor import FamiliaUsoMaterialMayor
from .uso_material_mayor import UsoMaterialMayor
from .tipo_vehiculo_material_mayor import TipoVehiculoMaterialMayor
from .marca_chasis_material_mayor import MarcaChasisMaterialMayor
from .color_material_mayor import ColorMaterialMayor
from .material_mayor import MaterialMayor
from .modelo_chasis_material_mayor import ModeloChasisMaterialMayor
from .marca_carrosado_material_mayor import MarcaCarrosadoMaterialMayor
from .condicion_material_mayor import CondicionMaterialMayor
from .marca_caja_cambio_material_mayor import MarcaCajaCambioMaterialMayor
from .modelo_caja_cambio_material_mayor import ModeloCajaCambioMaterialMayor
from .tipo_caja_cambio_material_mayor import TipoCajaCambioMaterialMayor
from .tipo_combustible_material_mayor import TipoCombustibleMaterialMayor
from .marca_bomba_material_mayor import MarcaBombaMaterialMayor
from .modelo_bomba_material_mayor import ModeloBombaMaterialMayor
from .pais import Pais
from .adquisicion_material_mayor import AdquisicionMaterialMayor
from .adquisicion_compra_material_mayor import AdquisicionCompraMaterialMayor
from .adquisicion_donacion_material_mayor import AdquisicionDonacionMaterialMayor
from .modo_adquisicion_material_mayor import ModoAdquisicionMaterialMayor
from .region import Region
from .provincia import Provincia
from .comuna import Comuna
from .cuerpo import Cuerpo
from .compania import Compania
from .tipo_evento_hoja_vida_material_mayor import TipoEventoHojaVidaMaterialMayor
from .evento_hoja_vida_material_mayor import EventoHojaVidaMaterialMayor
from .asignacion_cuerpo_material_mayor import AsignacionCuerpoMaterialMayor
from .asignacion_compania_material_mayor import AsignacionCompaniaMaterialMayor
from .rol import Rol
from .cargo import Cargo
from .user_profile import UserProfile
from .asignacion_patente_material_mayor import AsignacionPatenteMaterialMayor
from .cambio_pauta_mantencion_carrosado_material_mayor import CambioPautaMantencionCarrosadoMaterialMayor
from .cambio_numero_chasis_material_mayor import CambioNumeroChasisMaterialMayor
from .cambio_numero_motor_material_mayor import CambioNumeroMotorMaterialMayor
from .cambio_certificado_anotaciones_vigentes import CambioCertificadoAnotacionesVigentes
from .asignacion_solicitud_primera_inscripcion import AsignacionSolicitudPrimeraInscripcion
from .operacion_mantencion_pauta import OperacionMantencionPauta
from .mantencion_programada import MantencionProgramada
from .operacion_mantencion_programada import OperacionMantencionProgramada
from .ejecucion_operacion_mantencion_programada import EjecucionOperacionMantencionProgramada
from .archivo_mantencion_programada import ArchivoMantencionProgramada
from .motivo_dada_de_baja import MotivoDadaDeBaja
from .dada_de_baja_material_mayor import DadaDeBajaMaterialMayor
from .cambio_denominacion import CambioDenominacion

__all__ = [
    'TipoVehiculoMaterialMayor',
    'MarcaChasisMaterialMayor',
    'ColorMaterialMayor',
    'MaterialMayor',
    'ModeloChasisMaterialMayor',
    'MarcaCarrosadoMaterialMayor',
    'CondicionMaterialMayor',
    'MarcaCajaCambioMaterialMayor',
    'ModeloCajaCambioMaterialMayor',
    'TipoCajaCambioMaterialMayor',
    'TipoCombustibleMaterialMayor',
    'MarcaBombaMaterialMayor',
    'ModeloBombaMaterialMayor',
    'Pais',
    'AdquisicionMaterialMayor',
    'AdquisicionCompraMaterialMayor',
    'ModoAdquisicionMaterialMayor',
    'AdquisicionDonacionMaterialMayor',
    'Region',
    'Provincia',
    'Comuna',
    'Cuerpo',
    'Compania',
    'TipoEventoHojaVidaMaterialMayor',
    'EventoHojaVidaMaterialMayor',
    'AsignacionCuerpoMaterialMayor',
    'UserProfile',
    'Rol',
    'Cargo',
    'FamiliaUsoMaterialMayor',
    'UsoMaterialMayor',
    'AsignacionCompaniaMaterialMayor',
    'AsignacionPatenteMaterialMayor',
    'FrecuenciaOperacion',
    'PautaMantencion',
    'PautaMantencionChasis',
    'PautaMantencionCarrosado',
    'CambioPautaMantencionCarrosadoMaterialMayor',
    'CambioNumeroChasisMaterialMayor',
    'CambioNumeroMotorMaterialMayor',
    'CambioCertificadoAnotacionesVigentes',
    'AsignacionSolicitudPrimeraInscripcion',
    'OperacionMantencionPauta',
    'MantencionProgramada',
    'OperacionMantencionProgramada',
    'EjecucionOperacionMantencionProgramada',
    'ArchivoMantencionProgramada',
    'MotivoDadaDeBaja',
    'DadaDeBajaMaterialMayor',
    'CambioDenominacion'
]
