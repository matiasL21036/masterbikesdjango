from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
            return self.nombre
        

class producto(models.Model):
        nombre = models.CharField(max_length=50)
        precio = models.IntegerField()
        descripcion = models.TextField()
        nuevo = models.BooleanField()
        Marca = models.ForeignKey(Marca, on_delete= models.PROTECT)
        fecha_fabricacion = models.DateField()
        imagen = models.ImageField(upload_to="productos", null=True)
        def __str__(self):
            return self.nombre
        

class arrendar(models.Model):
      nombre = models.CharField(max_length=50)
      correo = models.EmailField()
      producto = models.ForeignKey(producto, on_delete= models.PROTECT)
      cantidad = models.IntegerField()
      def __str__(self):
            return self.nombre


class Usuario(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)


class Mecanico(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=100)
    experiencia = models.PositiveIntegerField()
    telefono = models.CharField(max_length=15 ,unique=True)
    disponibilidad = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


tipo_consulta = [
    [1, 'reparacion'],
    [2, 'mantencion']
]

class OrdenReparacion(models.Model):
    mecanico = models.ForeignKey(Mecanico, on_delete=models.PROTECT)
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE , null=False )
    bicicleta_nombre = models.CharField(max_length=100)
    descripcion_problema = models.TextField()
    fecha = models.DateTimeField(default = timezone.now)
    tipo = models.IntegerField( choices=tipo_consulta)

    def __str__(self):
        return f"Orden de reparación #{self.id}"

