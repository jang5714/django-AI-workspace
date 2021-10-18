from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from admin.calculator.models import Crawling

import matplotlib.pyplot as plt

@api_view(['GET'])
@parser_classes([JSONParser])
def calculator(request):
    Crawling().calculator()
    return JsonResponse({'crawling': 'calculator Success'})
