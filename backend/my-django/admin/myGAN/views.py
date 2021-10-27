from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from admin.myGAN.models import AutoencodersGANs

import matplotlib.pyplot as plt

@api_view(['GET'])
@parser_classes([JSONParser])
def process(request):
    AutoencodersGANs().process()
    return JsonResponse({'Auto process': 'Success'})