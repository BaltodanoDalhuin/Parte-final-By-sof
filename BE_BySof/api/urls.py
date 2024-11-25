from django.urls import path
from .views import (
    CategoriaListView, CategoriaDetailView,
    ProductoListView, ProductoDetailView,
    PersonalizacionProductoListView, PersonalizacionProductoDetailView,
    InventarioListView, InventarioDetailView,
    OpinionListView, OpinionDetailView,
    MetodoPagoListView, MetodoPagoDetailView,
    PedidoListView, PedidoDetailView,
    DetallePedidoListView, DetallePedidoDetailView,
    PagoListView, PagoDetailView,
)

urlpatterns = [
    path('categorias/', CategoriaListView.as_view(), name='categoria-list'),
    path('categorias/<int:pk>/', CategoriaDetailView.as_view(), name='categoria-detail'),
    path('productos/', ProductoListView.as_view(), name='producto-list'),
    path('productos/<int:pk>/', ProductoDetailView.as_view(), name='producto-detail'),
    path('personalizaciones/', PersonalizacionProductoListView.as_view(), name='personalizacion-list'),
    path('personalizaciones/<int:pk>/', PersonalizacionProductoDetailView.as_view(), name='personalizacion-detail'),
    path('inventarios/', InventarioListView.as_view(), name='inventario-list'),
    path('inventarios/<int:pk>/', InventarioDetailView.as_view(), name='inventario-detail'),
    path('opiniones/', OpinionListView.as_view(), name='opinion-list'),
    path('opiniones/<int:pk>/', OpinionDetailView.as_view(), name='opinion-detail'),
    path('metodos-pago/', MetodoPagoListView.as_view(), name='metodo-pago-list'),
    path('metodos-pago/<int:pk>/', MetodoPagoDetailView.as_view(), name='metodo-pago-detail'),
    path('pedidos/', PedidoListView.as_view(), name='pedido-list'),
    path('pedidos/<int:pk>/', PedidoDetailView.as_view(), name='pedido-detail'),
    path('detalles-pedido/', DetallePedidoListView.as_view(), name='detalle-pedido-list'),
    path('detalles-pedido/<int:pk>/', DetallePedidoDetailView.as_view(), name='detalle-pedido-detail'),
    path('pagos/', PagoListView.as_view(), name='pago-list'),
    path('pagos/<int:pk>/', PagoDetailView.as_view(), name='pago-detail'),
]
