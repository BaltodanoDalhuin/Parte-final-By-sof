from rest_framework.generics import ListAPIView, RetrieveAPIView
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

class CategoriaListView(ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetailView(RetrieveAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ProductoListView(ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetailView(RetrieveAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class PersonalizacionProductoListView(ListAPIView):
    queryset = PersonalizacionProducto.objects.all()
    serializer_class = PersonalizacionProductoSerializer

class PersonalizacionProductoDetailView(RetrieveAPIView):
    queryset = PersonalizacionProducto.objects.all()
    serializer_class = PersonalizacionProductoSerializer


class InventarioListView(ListAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer


class InventarioDetailView(RetrieveAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer


class OpinionListView(ListAPIView):
    queryset = Opinion.objects.all()
    serializer_class = OpinionSerializer

class OpinionDetailView(RetrieveAPIView):
    queryset = Opinion.objects.all()
    serializer_class = OpinionSerializer


class MetodoPagoListView(ListAPIView):
    queryset = MetodoPago.objects.all()
    serializer_class = MetodoPagoSerializer

class MetodoPagoDetailView(RetrieveAPIView):
    queryset = MetodoPago.objects.all()
    serializer_class = MetodoPagoSerializer



class PedidoListView(ListAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class PedidoDetailView(RetrieveAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer



class DetallePedidoListView(ListAPIView):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer


class DetallePedidoDetailView(RetrieveAPIView):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer


class PagoListView(ListAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

class PagoDetailView(RetrieveAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
