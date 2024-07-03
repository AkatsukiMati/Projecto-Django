from django.db import models
from django.utils import timezone

class Admin(models.Model):
    nombre = models.CharField(primary_key=True, max_length=10)
    apaterno = models.CharField(max_length=20)
    amaterno = models.CharField(max_length=20)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=45)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apaterno}"

class Producto(models.Model):
    marca = models.CharField(max_length=150)
    modelo = models.CharField(max_length=150)
    descripcion = models.TextField()
    image = models.ImageField(upload_to='images/', default=None)  

    def __str__(self):
        return f"{self.marca} {self.modelo}"


class Producto2(models.Model):
    marca = models.CharField(max_length=150)
    modelo = models.CharField(max_length=150)
    descripcion = models.TextField()
    image = models.ImageField(upload_to='images/', default=None)  

    def __str__(self):
        return f"{self.marca} {self.modelo}"


class Producto3(models.Model):
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"Imagen: {self.image.url}"
