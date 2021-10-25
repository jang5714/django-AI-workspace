from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from admin.myNLP.models import Imdb, NaverMoive

import matplotlib.pyplot as plt

@api_view(['GET'])
@parser_classes([JSONParser])
def imdb_process(request):
    Imdb().imdb_process()
    return JsonResponse({'Iris imdb_process': 'Success'})

@api_view(['GET'])
@parser_classes([JSONParser])
def naver_process(request):
    NaverMoive().naver_process()
    return JsonResponse({'Iris naver_process': 'Success'})