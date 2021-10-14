from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from admin.crime.models import Crime

import matplotlib.pyplot as plt
@api_view(['GET'])
@parser_classes([JSONParser])
def create_crime_model(request):
    Crime().create_crime_model()
    return JsonResponse({'crime':'create model Success'})

def create_police_position(request):
    Crime().create_police_position()
    return JsonResponse({'crime':'create Police Success'})

def create_cctv_model(request):
    Crime().create_cctv_model()
    return JsonResponse({'crime':'create cctv Success'})

def create_population_model(request):
    Crime().create_population_model()
    return JsonResponse({'crime':'create population Success'})

def merge_cctv_pop(request):
    Crime().merge_cctv_pop()
    return JsonResponse({'crime':'merge Success'})

def sum_crime(request):
    Crime().sum_crime()
    return JsonResponse({'crime':'sum Success'})

def process(request):
    Crime().process()
    return JsonResponse({'crime':'process'})