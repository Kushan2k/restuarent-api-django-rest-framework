
from rest_framework import generics
from . import serializers
from . import models
from rest_framework import pagination
from rest_framework import filters
from rest_framework import authentication
from rest_framework import request
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication


class MenuItems(generics.ListCreateAPIView):

  serializer_class=serializers.MenuItemSerializer
  queryset=models.MenuItem.objects.select_related('category').all()
  pagination_class=pagination.PageNumberPagination
  
  filter_backends=[filters.SearchFilter]
  filterset_fields = ['price']
  search_fields = ['title']

  
class MenuItemsPathUpdate(generics.RetrieveUpdateDestroyAPIView):
  serializer_class=serializers.MenuItemSerializer
  queryset=models.MenuItem.objects.all()
  authentication_classes=[authentication.TokenAuthentication]


@api_view(['GET'])

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def me(request:request.Request):

  return Response(request.user,status=status.HTTP_302_FOUND)

  
