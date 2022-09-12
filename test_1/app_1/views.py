from urllib import response
from django.shortcuts import render, HttpResponseRedirect
from rest_framework.views import APIView
from app_1.models import *
from app_1.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import User
from django.views.generic.base import TemplateView, RedirectView
from django.views import View
from rest_framework import generics
import requests
# Create your views here.


# ----------------------------------------------------------------------------------------------

class ListState(APIView):
    def get(self, request):
        try:
            sta = State.objects.all()
            serializer = StateSerializer(sta, many=True)
            return Response({"status_code": status.HTTP_200_OK,"data":serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status_code": status.HTTP_404_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)


class ListDistrict(APIView):
    def get(self, request):
        try:
            dis = District.objects.all()
            serializer = DistrictSerializer(dis, many=True)
            return Response({"status_code": status.HTTP_200_OK,"data":serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status_code": status.HTTP_404_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)


   

class ListVillage(APIView):
    def get(self, request):
        try:
            dis = Village.objects.all()
            serializer = VillageSerializer(dis, many=True)
            return Response({"status_code": status.HTTP_200_OK,"data":serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status_code": status.HTTP_404_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)

class ListUser(APIView):
    def get(self, request):
        try:
            dis = User.objects.all()
            serializer = UserSerializer(dis, many=True)
            return Response({"status_code": status.HTTP_200_OK,"data":serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status_code": status.HTTP_404_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
            

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User
    serializer_class = UserSerializer


def home(request):
    response = requests.get("http://127.0.0.1:8000/api/user/")
    data = response.json()
    print("1")
    return render(request,'home.html',{'data':data})


