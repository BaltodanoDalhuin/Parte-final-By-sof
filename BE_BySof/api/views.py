from rest_framework import generics
from .models import (
    Categoria, Producto, PersonalizacionProducto,
    Inventario, Opinion, MetodoPago, Pedido,
    DetallePedido, Pago
)
from .serializers import (
    CategoriaSerializer, ProductoSerializer, PersonalizacionProductoSerializer,
    InventarioSerializer, OpinionSerializer, MetodoPagoSerializer,
    PedidoSerializer, DetallePedidoSerializer, PagoSerializer
)

class CategoriaListView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ProductoListView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetailView(generics.DestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class PersonalizacionProductoListView(generics.ListCreateAPIView):
    queryset = PersonalizacionProducto.objects.all()
    serializer_class = PersonalizacionProductoSerializer

class PersonalizacionProductoDetailView(generics.DestroyAPIView):
    queryset = PersonalizacionProducto.objects.all()
    serializer_class = PersonalizacionProductoSerializer


class InventarioListView(generics.ListCreateAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer


class InventarioDetailView(generics.DestroyAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer


class OpinionListView(generics.ListCreateAPIView):
    queryset = Opinion.objects.all()
    serializer_class = OpinionSerializer

class OpinionDetailView(generics.DestroyAPIView):
    queryset = Opinion.objects.all()
    serializer_class = OpinionSerializer


class MetodoPagoListView(generics.ListCreateAPIView):
    queryset = MetodoPago.objects.all()
    serializer_class = MetodoPagoSerializer

class MetodoPagoDetailView(generics.DestroyAPIView):
    queryset = MetodoPago.objects.all()
    serializer_class = MetodoPagoSerializer



class PedidoListView(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class PedidoDetailView(generics.DestroyAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer



class DetallePedidoListView(generics.ListCreateAPIView):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer


class DetallePedidoDetailView(generics.DestroyAPIView):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer


class PagoListView(generics.ListCreateAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

class PagoDetailView(generics.DestroyAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer