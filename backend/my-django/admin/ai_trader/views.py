from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from admin.ai_trader.models import AITrader

import matplotlib.pyplot as plt

@api_view(['GET'])
@parser_classes([JSONParser])
def process(request):
    AITrader().process()
    return JsonResponse({'process': 'Success'})