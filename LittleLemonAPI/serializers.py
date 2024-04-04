from rest_framework import serializers
from .models import Cart,Category,MenuItem,OderItem,Order

class CategorySerializer(serializers.ModelSerializer):

  class Meta:
    model=Category


class CartSerializer(serializers.ModelSerializer):

  class Meta:
    model=Cart

class MenuItemSerializer(serializers.ModelSerializer):

  class Meta:
    model=MenuItem

class OrderItemSerializer(serializers.ModelSerializer):

  class Meta:
    model=OderItem

class OrderSerializer(serializers.ModelSerializer):
  class Meta:
    model=Order
