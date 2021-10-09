from django.http import JsonResponse

from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from admin.housing.models import HousingService
from icecream import ic

from admin.jarviis.models import Jarviis


@api_view(['GET'])
@parser_classes([JSONParser])
def create_jarviis_model(request):
    Jarviis().create_jarviis_model()
    return JsonResponse({'result': 'jarviis Info SUCCESS'})

def create_message_model(request):
    Jarviis().create_message_model()
    return JsonResponse({'result': 'jarviis message SUCCESS'})

