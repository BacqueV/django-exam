from rest_framework.viewsets import ModelViewSet

# models & serializers
from . import serializers
from . import models

# permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

# filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class CategoryViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filter_fields = ['name', 'slug']
    search_fields = ['name', 'slug']
    ordering_fields = ['name', 'slug']


class ProductViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filter_fields = ['category', 'name', 'price']
    search_fields = ['category', 'name', 'price']
    ordering_fields = ['category', 'name', 'price']


class OrderViewSet(ModelViewSet):
    permission_classes = (IsAdminUser, )

    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filter_fields = ['client', 'shipping', 'is_paid', 'total_price']
    search_fields = ['client', 'shipping', 'is_paid', 'total_price']
    ordering_fields = ['client', 'shipping', 'is_paid', 'total_price']


class OrderItemViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]

    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer
