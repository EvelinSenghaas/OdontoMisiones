from django.db import models
from simple_history.models import HistoricalRecords


class Provincia(models.Model):
    id=models.AutoField(primary_key=True)
    provincia=models.CharField('Provincia', max_length=50,blank=False,null=False)
    borrado = models.BooleanField('borrado',default=False)
    history = HistoricalRecords()
    def __str__(self):
        return self.provincia

class Localidad(models.Model):
    id = models.AutoField(primary_key = True)
    localidad=models.CharField('Localidad', max_length=50,blank=False,null=False)
    provincia=models.ForeignKey(Provincia,on_delete=models.PROTECT)
    borrado = models.BooleanField('borrado',default=False)
    history = HistoricalRecords()
    def __str__(self):
        return self.localidad

class Barrio(models.Model):
    id= models.AutoField(primary_key = True)
    barrio=models.CharField('Barrio', max_length=50,blank=False,null=False)
    localidad=models.ForeignKey(Localidad, on_delete=models.PROTECT)
    borrado = models.BooleanField('borrado',default=False)
    history = HistoricalRecords()
    def __str__(self):
        return self.barrio

class Domicilio(models.Model):
    id = models.AutoField(primary_key=True)
    calle=models.CharField('Calle', max_length=100,blank=False,null=False)
    nro=models.CharField('Numero', max_length=50,blank=False,null=False)
    mz = models.CharField('Manzana', max_length=50,null=True,blank=True)
    departamento=models.CharField('Departamento', max_length=50,null=True,blank=True)
    piso=models.CharField('Piso', max_length=50,null=True,blank=True)
    barrio=models.ForeignKey(Barrio, on_delete=models.PROTECT)
    borrado = models.BooleanField('borrado',default=False)
    
    def __str__(self):
        return 'calle '+self.calle+'  nro '