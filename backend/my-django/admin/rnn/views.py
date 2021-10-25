from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from admin.rnn.models import MyRNN

import matplotlib.pyplot as plt

@api_view(['GET'])
@parser_classes([JSONParser])
def ram_price(request):
    MyRNN().ram_price()
    return JsonResponse({'ram_price': 'Success'})

@api_view(['GET'])
@parser_classes([JSONParser])
def kia_predict(request):
    MyRNN().kia_predict()
    return JsonResponse({'kia_predict': 'Success'})
