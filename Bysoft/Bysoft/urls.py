from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/categorias/', include('aplicacion.urls.categorias')),
    path('api/productos/', include('aplicacion.urls.productos')),
    path('api/personalizaciones/', include('aplicacion.urls.personalizaciones')),
    path('api/inventarios/', include('aplicacion.urls.inventarios')),
    path('api/opiniones/', include('aplicacion.urls.opiniones')),
    path('api/metodos-pago/', include('aplicacion.urls.metodos_pago')),
    path('api/pedidos/', include('aplicacion.urls.pedidos')),
    path('api/detalles-pedido/', include('aplicacion.urls.detalles_pedido')),
    path('api/pagos/', include('aplicacion.urls.pagos')),
]
