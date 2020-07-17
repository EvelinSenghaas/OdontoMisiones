from django.db import models
from datetime import date
from simple_history.models import HistoricalRecords
from apps.equipos.models import Estado
from apps.clientes.models import Cliente
from apps.servicios.models import Servicio
from apps.proveedores.models import Proveedor


class Insumo(models.Model):
    id =  models.AutoField(primary_key = True)
    marca = models.CharField('Marca (*)',max_length=200, blank=False,null=False)
    modelo = models.CharField('Modelo (*)', max_length=200, blank=False,null=False)
    fechaGarantia=models.DateField('Fecha de Garantia (*)', auto_now=False, auto_now_add=False)
    numSerie = models.CharField('Numero de Serie (*)', max_length=200, blank=False,null=False)
    precio = models.DecimalField('Precio (*)', max_digits=19, decimal_places=2)
    disponibilidad = models.IntegerField('Disponibilidad ')
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    nota = models.CharField('Nota', max_length=200, blank=True,null=True)
    borrado = models.BooleanField('borrado',default=False)
    history = HistoricalRecords()

class DetalleCompra(models.Model):
    id = models.AutoField(primary_key = True)
    cant = models.IntegerField('Cantidad (*) ')
    precio = models.DecimalField('Precio (*)',max_digits=19, decimal_places=2) #esto es autocalculable
    insumo = models.ForeignKey(Insumo, on_delete=models.PROTECT)


class Compra(models.Model):
    id = models.AutoField(primary_key = True)
    fecha = models.DateField('Fecha (*)',auto_now=True, auto_now_add=False)
    total = models.DecimalField('Total (*)',max_digits=19, decimal_places=2)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    detalle = models.ForeignKey(DetalleCompra, on_delete=models.PROTECT) #una compra tiene un detalle y un detalle pertenece a una compra

class DetalleVenta(models.Model):
    id = models.AutoField(primary_key = True)
    cant = models.IntegerField('Cantidad (*) ')
    precio = models.DecimalField('Precio (*)',max_digits=19, decimal_places=2) #esto es autocalculable
    insumo = models.ForeignKey(Insumo, on_delete=models.PROTECT)
    servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT)


class Venta(models.Model):
    id = models.AutoField(primary_key = True)
    fecha = models.DateField('Fecha (*)',auto_now=True, auto_now_add=False)
    total = models.DecimalField('Total (*)',max_digits=19, decimal_places=2)
    pago = models.BooleanField('Pago (*)',default=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    detalle = models.ForeignKey(DetalleVenta, on_delete=models.PROTECT) #una venta tiene un detalle y un detalle pertenece a una venta
