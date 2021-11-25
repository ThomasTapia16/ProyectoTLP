from django.db import models

from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField 

class Cliente(models.Model): 

    rut = models.CharField(max_length = 10 ,primary_key = True)
    correo = models.CharField(max_length = 100)
    nombre = models.CharField(max_length = 50)
    deuda = models.IntegerField(default = 0)
    telefono = models.CharField(max_length = 9)
    def __str__(self):
        return self.nombre

class Funcionario(models.Model):

    rut = models.CharField(max_length = 10, primary_key = True)
    usuario = models.CharField(max_length = 20)
    contrasena = models.CharField(max_length = 20)
    def __str__(self):
        return self.usuario

    
class Tarjeta(models.Model):

    numero_tarj = models.IntegerField(primary_key = True)
    rut_propietario = models.ForeignKey(Cliente, name = "dueño",on_delete = CASCADE)

class Servicio(models.Model):

    num_servicio = models.IntegerField(primary_key = True)
    fecha_reserva_servicio = models.DateTimeField()
    fecha_inicio_servicio = models.DateTimeField()
    rut_cliente = models.ForeignKey(Cliente, name = "cliente",on_delete = CASCADE)
    rut_funcionario = models.ForeignKey(Funcionario, name = "funcionario",on_delete = CASCADE)

class Pago(models.Model):

    id_pago = models.BigIntegerField(primary_key = True)
    fecha_pago = models.DateField()
    hora_pago = models.TimeField()
    rut_cliente = models.ForeignKey(Cliente, name = "cliente",on_delete = CASCADE)
    rut_funcionario = models.ForeignKey(Funcionario, name = "funcionario",on_delete = CASCADE)



class Elemento(models.Model):

    id_elemento = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length = 50)
    marca = models.CharField(max_length = 15)
    fecha_ingreso = models.DateField()
    fecha_retiro = models.DateField()
    #recordar ojo
    funcionario = models.ForeignKey(Funcionario, on_delete = CASCADE)

class Detalle(models.Model):

    id_detalle = models.IntegerField(primary_key = True)
    fecha_hora_entrega = models.DateTimeField()
    fecha_hora_entrega_real = models.DateTimeField()
    servicio = models.ForeignKey(Servicio,on_delete = CASCADE)
    elementos = models.ManyToManyField(
        Elemento,
        through = 'DetalleElemento',
        through_fields = ('detalle', 'elemento')
    )
class Incidente(models.Model):

    id_incidente = models.IntegerField(primary_key = True)
    fecha_incidente = models.DateTimeField()
    observacion = models.TextField(max_length = 10000)
    servicio = models.ForeignKey(Servicio,on_delete = CASCADE)
    detalle = models.ForeignKey(Detalle,on_delete = CASCADE)

class DetalleElemento(models.Model):

    detalle = models.ForeignKey(Detalle, on_delete = CASCADE)
    elemento = models.ForeignKey(Elemento, on_delete= CASCADE)


