from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from admin.iris.models import Iris

import matplotlib.pyplot as plt

@api_view(['GET'])
@parser_classes([JSONParser])
def base(request):
    Iris().base()
    return JsonResponse({'Iris Base': 'Success'})

@api_view(['GET'])
@parser_classes([JSONParser])
def advanced(request):
    Iris().advanced()
    return JsonResponse({'Iris advanced': 'Success'})

@api_view(['GET'])
@parser_classes([JSONParser])
def iris_by_tf(request):
    Iris().iris_by_tf()
    return JsonResponse({'Iris by_tf': 'Success'})