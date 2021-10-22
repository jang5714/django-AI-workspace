from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from admin.myCV2.models import MyCV2
import matplotlib.pyplot as plt

@api_view(['GET'])
@parser_classes([JSONParser])
def lena(request):
    MyCV2().lena()
    return JsonResponse({'lena': 'Success'})


@api_view(['GET'])
@parser_classes([JSONParser])
def girl(request):
    MyCV2().girl()
    return JsonResponse({'girl': 'Success'})

@api_view(['GET'])
@parser_classes([JSONParser])
def face_detect(request):
    MyCV2().face_detect()
    return JsonResponse({'face_detect': 'Success'})

@api_view(['GET'])
@parser_classes([JSONParser])
def cat_mosaic(request):
    MyCV2().cat_mosaic()
    return JsonResponse({'cat_mosaic': 'Success'})

@api_view(['GET'])
@parser_classes([JSONParser])
def face_mosaic(request):
    MyCV2().face_mosaic()
    return JsonResponse({'face_mosaic': 'Success'})

