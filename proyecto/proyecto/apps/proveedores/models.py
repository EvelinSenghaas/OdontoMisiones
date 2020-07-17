from django.db import models
from datetime import date
from simple_history.models import HistoricalRecords
from apps.clientes.models import Cliente
from apps.servicios.models import Servicio
from apps.parametros.models import Domicilio


class Proveedor(models.Model):
    id =  models.AutoField(primary_key = True)
    nombre=models.CharField('Nombre (*)',max_length=200,blank = False, null = False)
    empresa = models.CharField('Empresa (*)',max_length=200,blank = False, null = True)
    domicilio=models.ForeignKey(Domicilio, on_delete=models.PROTECT)
    telefono = models.IntegerField('Telefono', default=False, blank=False, null=False)
    email=models.EmailField('e-mail', max_length=100,null=True,blank=True)
    contacto = models.CharField('Nombre de Contacto (*)',max_length=200,blank = False, null = False)
    nota = models.CharField('Nota ',max_length=200,blank = True, null = True)
    borrado = models.BooleanField('borrado',default=False)
    history = HistoricalRecords()
