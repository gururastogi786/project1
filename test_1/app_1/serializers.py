from rest_framework import serializers
from app_1.models import *

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = "__all__"

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = "__all__"

class VillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Village
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"