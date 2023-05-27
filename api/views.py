from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from api.antlr.main import *
from api.serializers import InputSerializer

@api_view(['POST'])
def analisys(request):
    serializer = InputSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        tokens = processInput(data['input'])
        return Response({'tokens': tokens}, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)