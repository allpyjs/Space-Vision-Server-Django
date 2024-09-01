from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as JwtTokenObtainPairSerializer
from .models import EIAData, CrudeOil


class TokenObtainPairSerializer(JwtTokenObtainPairSerializer):
    username_field = get_user_model().USERNAME_FIELD


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password')


class PasswordSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class CrudeOilSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrudeOil
        fields = '__all__'


class EIADataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EIAData
        fields = '__all__'
