from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from user.models import UserVo
from user.serializer import UserSerializer


@api_view(['GET','POST'])
@parser_classes([JSONParser])
def users(request):
    if request.method == 'GET':
        all_users = UserVo.objects.all()
        serializer = UserSerializer(all_users, many=True)
        return JsonResponse(data = serializer, safe=False)
    elif request.method == 'POST':
        new_user = request.data['body']
        print(new_user)
        serializer = UserSerializer(data= new_user)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'request' : f'Welcom, {serializer.data.get("name")}'}, status=201)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQEST)

