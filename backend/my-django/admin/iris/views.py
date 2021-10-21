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
