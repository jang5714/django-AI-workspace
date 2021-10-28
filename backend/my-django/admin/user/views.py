from django.contrib.auth import authenticate
from django.http import JsonResponse
from icecream import ic
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from admin.user.models import User
from admin.user.serializer import UserSerializer


@api_view(['GET','POST','PUT'])
@parser_classes([JSONParser])
def users(request):
    if request.method == 'GET': # list
        all_users = User.objects.all()
        serializer = UserSerializer(all_users, many=True)
        return JsonResponse(data=serializer, safe = False)
    elif request.method == 'POST': # join
        new_user = request.data['body']
        ic(new_user)
        serializer = UserSerializer(data=new_user['user'])
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'result' : f'Welcome, {serializer.data.get("name")}'}, status=201)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT': # modify

        return None


# @api_view(['GET','POST']) # remove
# @parser_classes([JSONParser])
# def users(request, id):
#     pass


@api_view(['POST'])
@parser_classes([JSONParser])
def login(request):
   if request.method == 'POST':
       User.username = request.POST['username']
       User.password = request.POST['password'
       ln = authenticate(username = User.username, password= User.password)
       if ln is not None;
         login(request, ln)
