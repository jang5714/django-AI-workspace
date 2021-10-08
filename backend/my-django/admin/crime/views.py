from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from admin.crime.models import CrimeCctvModel


@api_view(['GET'])
@parser_classes([JSONParser])
def create_crime_model(request):
    CrimeCctvModel().create_crime_model()
    return JsonResponse({'crime':'create model Success'})

def create_police_position(request):
    CrimeCctvModel().create_police_position()
    return JsonResponse({'crime':'create Police Success'})

def create_cctv_model(request):
    CrimeCctvModel().create_cctv_model()
    return JsonResponse({'crime':'create cctv Success'})

def create_population_model(request):
    CrimeCctvModel().create_population_model()
    return JsonResponse({'crime':'create population Success'})

def merge_cctv_pop(request):
    CrimeCctvModel().merge_cctv_pop()
    return JsonResponse({'crime':'merge Success'})

def sum_crime(request):
    CrimeCctvModel().sum_crime()
    return JsonResponse({'crime':'sum Success'})