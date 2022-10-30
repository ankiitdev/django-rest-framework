from rest_framework import serializers
from .models import Drink
from django.contrib.auth import get_user_model

User = get_user_model()

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', "name", 'description']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()     
    
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)
    # password2 = serializers.CharField(required=True, write_only=True)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            # 'password2',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            # 'password2': {'write_only': True},
        }

    def create(self, validated_data):
        username = validated_data.get('username')    
        email = validated_data.get('email')    
        password = validated_data.get('password')    
        # password1 = validated_data.get('password')    
        # password2 = validated_data.get('password2')

        # if password1 == password2:
        #     user = User(username=username, email=email)
        #     user.set_password(password1)
        #     user.save()
        #     return user
        # else:
        #     raise serializers.ValidationError({
        #         'error': 'Passwords don\'t match'
        #     })
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        return user    