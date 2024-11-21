from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre_categoria

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen_url = models.URLField()
    fecha_creacion = models.DateField()
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_producto

class PersonalizacionProducto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    detalle_personalizacion = models.CharField(max_length=255)
    opciones = models.TextField()

    def __str__(self):
        return f"{self.tipo_personalizacion} - {self.producto.nombre_producto}"

class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_disponible = models.IntegerField()
    fecha_actualizacion = models.DateField()

class Opinion(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    calificacion = models.IntegerField()
    comentario = models.TextField()
    fecha_opinion = models.DateField()

class MetodoPago(models.Model):
    nombre_metodo = models.CharField(max_length=255)
    detalles = models.TextField()

class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_pedido = models.DateField()
    estado = models.CharField(max_length=50)
    total = models.FloatField()


class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    personalizacion = models.TextField()
    precio = models.FloatField()


class Pago(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    monto = models.FloatField()
    fecha_pago = models.DateField()
