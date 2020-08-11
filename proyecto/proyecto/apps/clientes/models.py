from django.db import models
from simple_history.models import HistoricalRecords
from apps.parametros.models import Domicilio

class Cliente(models.Model):
    id =  models.AutoField(primary_key = True)
    nombre=models.CharField('Nombre (*)',max_length=200,blank = False, null = False)
    apellido = models.CharField('Descripcion (*)',max_length=200,blank = False, null = True)
    domicilio=models.ForeignKey(Domicilio, on_delete=models.PROTECT)
    telefono = models.CharField('Telefono', max_length=200, blank=False, null=False)
    email=models.EmailField('e-mail', max_length=100,null=True,blank=True)
    nota = models.CharField('Nota ',max_length=200,blank = True, null = True)
    borrado = models.BooleanField('borrado',default=False)
    history = HistoricalRecords()

    def __str__(self):
        return self.nombre 

class EstadoCrediticio(models.Model):
    #no le pongo una relacion porque se me hace que faltan datos, y todavia no vamos a usar esto *(tenemos que debatir)
    id= models.AutoField(primary_key = True)
    credito = models.BooleanField('Credito ', default = False)
    adeuda = models.BooleanField('Credito ', default = False)
    deuda = models.DecimalField('Deuda', max_digits=19, decimal_places=2)
    