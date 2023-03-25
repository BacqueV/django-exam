from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'categories', views.CategoryViewSet, basename='category')
router.register(r'product', views.ProductViewSet, basename='product')
router.register(r'orders', views.OrderViewSet, basename='order')
router.register(r'order_items', views.OrderItemViewSet, basename='order_items')


urlpatterns = [
    path('', include(router.urls)),
]
