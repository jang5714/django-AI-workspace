from rest_framework import serializers
from .models import UserVo as user

class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    name = serializers.CharField()
    email = serializers.CharField()
    birth = serializers.CharField()
    address = serializers.CharField()
    class Meta:
        model = user
        fileds = '__all__'

    def create(self, valided_data):
        return user.objects.create(**valided_data)

    def update(self, instence, valided_data):
        user.objects.filter(pk=instence.username).update(**valided_data)