from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    username = serializers.CharField(max_length=20, validators=[UniqueValidator(queryset=User.objects.all(), message = "username already taken.")])
    email =  serializers.CharField(max_length=127, validators=[UniqueValidator(queryset=User.objects.all(), message = "email already registered.")])
    password = serializers.CharField(max_length=50, write_only=True)
    first_name = serializers.CharField(max_length=50,)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(allow_null=True, default=None)
    is_employee = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(read_only=True)
    
       
    def create(self, validated_data:dict):
        if validated_data.get("is_employee", None):
            user = User.objects.create_superuser(**validated_data)
        else:
            user = User.objects.create_user(**validated_data)
        return user