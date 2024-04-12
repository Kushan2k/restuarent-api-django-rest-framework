from rest_framework import serializers
from .models import Cart,Category,MenuItem,OderItem,Order

class CategorySerializer(serializers.ModelSerializer):

  class Meta:
    model=Category
    fields=['title','id','slug']

class MenuItemSerializer(serializers.ModelSerializer):

  category=CategorySerializer(read_only=True)
  class Meta:
    depth=1
    model=MenuItem
    fields=['title','price','featured','category','id']
class CartSerializer(serializers.ModelSerializer):
  user=serializers.StringRelatedField(read_only=True)
  menuitem=MenuItemSerializer(many=True,read_only=True)

  class Meta:
    model=Cart
    depth=1
    fields=['user','menuitem','quantity','unit_price','price','id']



class OrderSerializer(serializers.ModelSerializer):
  order=serializers.StringRelatedField(read_only=True)
  delivery_crew=serializers.StringRelatedField(read_only=True,many=True)
  class Meta:
    model=OderItem
    depth=1
    fields=['user','delivery_crew','status','total','date','id']

class OrderItemSerializer(serializers.ModelSerializer):
  order=OrderSerializer(read_only=True)
  menuitem=MenuItemSerializer(read_only=True)
  class Meta:
    model=Order
    depth=1
    fields=['order','menuitem','quantity','unit_price','id']
