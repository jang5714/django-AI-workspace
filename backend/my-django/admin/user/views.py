from django.contrib.auth import authenticate
from django.http import JsonResponse
from icecream import ic
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from admin.user.models import User
from admin.user.serializer import UserSerializer


@api_view(['GET','POST','PUT'])
@parser_classes([JSONParser]) # requestbody 느낌
def users(request):
    if request.method == 'GET': # list
        print('list 들어옴')
        all_users = User.objects.all()
        serializer = UserSerializer(all_users, many=True)
        return JsonResponse(data=serializer.data, safe=False)
    elif request.method == 'POST': # join
        joinUser = request.data['body']
        ic(request.data)
        serializer = UserSerializer(data=joinUser['user'])
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'result' : f'Welcome, {serializer.data.get("name")}'}, status=201)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT': # modify
        return None

@api_view(['GET']) # remove
@parser_classes([JSONParser]) # requestbody 느낌
def detail(request):
     print('*' * 100)
     id = request.data
     ic(id)
     dbUser = User.objects.get(pk=id['username'])
     ic(dbUser)
     userSreializer = UserSerializer(dbUser, many=False)
     return JsonResponse(data=userSreializer.data, safe=False)


@api_view(['GET','POST']) # remove
def remove(request, id):
    pass


@api_view(['POST'])
@parser_classes([JSONParser])
def login(request):
   print('밖에 잇음')
   try :
       print('try 들어옴')
       logindata = request.data
       dbUser = User.objects.get(pk= logindata['username'])
       if logindata['password'] == dbUser.password:
           userSreializer = UserSerializer(dbUser, many=False)
           return JsonResponse(data=userSreializer.data, safe=False)
       else:
           print('******** 비밀번호 오류')
           return JsonResponse(data={'result': 'PASSWORD-FAIL'}, status=201)
   except User.DoesNotExist:
       print('*' * 50)
       print('******** Username 오류')
       return JsonResponse(data={'result': 'USERNAME-FAIL'}, status=201)

