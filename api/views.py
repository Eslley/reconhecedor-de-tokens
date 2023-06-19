from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from api.antlr.main import *
from api.parser.SQLParser import SQLParser
from api.serializers import InputSerializer

import re

@api_view(['POST'])
def analisys(request):
    serializer = InputSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        rules, recognizedTokens, nonRecognizedTokens = processInput(data['input'])

        response = {
            'ruleNames': rules,
            'tokens': {
                'recognizedTokens': recognizedTokens,
                'nonRecognizedTokens': nonRecognizedTokens
            }
        }

        return Response(response , status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def parser(request):
    serializer = InputSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        input = data['input']
        input = input.lower().replace('/r', '')

        tokens = []

        count_lines = 1
        lines = input.split('\n')
        for line in lines:
            tokens_line = re.split(r'([ ();=,])', line)

            for token in tokens_line:
                tokens.append({'line': count_lines, 'token': token})

            count_lines += 1

        tokens = list(filter(lambda token: token['token'] not in ['', " ","\n"], tokens))

        try:
            mp = SQLParser(tokens)
            mp.ini()

            response = {
                'success': True,
            }
        except ValueError as e:
            response = {
                'success': False,
                'errorInfo': e.args, 
            }

        return Response(response , status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)