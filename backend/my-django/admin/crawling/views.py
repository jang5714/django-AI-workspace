from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from admin.crawling.models import Crawling

import matplotlib.pyplot as plt

@api_view(['GET'])
@parser_classes([JSONParser])
def process(request):
    Crawling().process()
    return JsonResponse({'crawling': 'process Success'})

