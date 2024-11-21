from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    Categoria, Producto, PersonalizacionProducto,
    Inventario, Opinion, MetodoPago, Pedido,
    DetallePedido, Pago
)

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)

    class Meta:
        model = Producto
        fields = '__all__'


class PersonalizacionProductoSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField()
    producto = ProductoSerializer(read_only=True)

    class Meta:
        model = PersonalizacionProducto
        fields = '__all__'


class InventarioSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)

    class Meta:
        model = Inventario
        fields = '__all__'


class OpinionSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField()
    producto = ProductoSerializer(read_only=True)

    class Meta:
        model = Opinion
        fields = '__all__'


class MetodoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoPago
        fields = '__all__'


class PedidoSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField()

    class Meta:
        model = Pedido
        fields = '__all__'


class DetallePedidoSerializer(serializers.ModelSerializer):
    pedido = PedidoSerializer(read_only=True)
    producto = ProductoSerializer(read_only=True)

    class Meta:
        model = DetallePedido
        fields = '__all__'


class PagoSerializer(serializers.ModelSerializer):
    pedido = PedidoSerializer(read_only=True)
    metodo_pago = MetodoPagoSerializer(read_only=True)

    class Meta:
        model = Pago
        fields = '__all__'
