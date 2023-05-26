from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from api.antlr.main import *

@api_view(['POST'])
def analisys(request):
    data = request.data['input']
    
    tokens = processInput(data)
    
    return Response({ 'tokens': tokens }, status=status.HTTP_200_OK)