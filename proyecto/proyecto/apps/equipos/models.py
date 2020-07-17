from django.db import models
from datetime import date
from simple_history.models import HistoricalRecords
from apps.clientes.models import Cliente

class Estado(models.Model):
    id =  models.AutoField(primary_key = True)
    estado= models.CharField('Estado (*)',max_length=200, blank = False, null=False)
    borrado = models.BooleanField('borrado',default=False)

class Equipo(models.Model):
    id =  models.AutoField(primary_key = True)
    marca = models.CharField('Marca (*)',max_length=200,blank=False,null=False)
    modelo = models.CharField('Modelo (*)', max_length=200, blank=False,null=False)
    fechaGarantia=models.DateField('Fecha de Garantia (*)', auto_now=False, auto_now_add=False)
    numSerie = models.CharField('Numero de Serie (*)', max_length=200, blank=False,null=False)
    nota = models.CharField('Nota', max_length=200, blank=True,null=True)
    cliente = models.ManyToManyField(Cliente)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    borrado = models.BooleanField('borrado',default=False)
    history = HistoricalRecords()
