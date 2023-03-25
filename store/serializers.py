from rest_framework.serializers import ModelSerializer
from . import models


class CategorySerializer(ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'
        read_only_fields = ('id', )


class ProductSerializer(ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
        read_only_fields = ('id', )


class OrderSerializer(ModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'
        read_only_fields = ('id', )


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = models.OrderItem
        fields = '__all__'
        read_only_fields = ('id', )
