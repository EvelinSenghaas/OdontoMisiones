from django.db import models
from datetime import date
from simple_history.models import HistoricalRecords
from apps.equipos.models import Equipo

class TipoServicio(models.Model):
    id =  models.AutoField(primary_key = True)
    tipo = models.CharField('Tipo de Servicio (*)', max_length=200, blank=False, null=False)

class NivelUrgencia(models.Model):
    id =  models.AutoField(primary_key = True)
    nivel = models.CharField('Nivel de Urgencia (*)', max_length=200, blank=False, null=False)

class EstadoServicio(models.Model):
    id =  models.AutoField(primary_key = True)
    estado = models.CharField('Estado (*)', max_length=200, blank=False, null=False)

class Servicio(models.Model):
    id =  models.AutoField(primary_key = True)
    pago = models.BooleanField('Pagó (*)',default=False)
    fechaRecepcion = models.DateField('Fecha de Recepcion (*)',auto_now=True, auto_now_add=False)
    fechaEntrega = models.DateField('Fecha de Entrega (*)',auto_now=False, auto_now_add=False)
    manoDeObra = models.DecimalField('Mano de Obra (*)', max_digits=19,decimal_places=2)
    importeFinal = models.DecimalField('Importe Final',max_digits=19, decimal_places=2)
    equipo=models.ForeignKey(Equipo, on_delete=models.PROTECT)
    estado=models.ForeignKey(EstadoServicio, on_delete=models.PROTECT)
    nivelUrgencia=models.ForeignKey(NivelUrgencia, on_delete=models.PROTECT)
    tipo=models.ForeignKey(TipoServicio, on_delete=models.PROTECT)
    history = HistoricalRecords()




