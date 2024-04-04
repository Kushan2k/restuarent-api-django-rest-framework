
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view,APIView
from rest_framework.viewsets import ViewSet
from rest_framework import status

@api_view(['GET'])
def Home(req:Request):

  return Response({"msg":"hello world!"},status=status.HTTP_200_OK)

class NewHome(ViewSet):
  pass
