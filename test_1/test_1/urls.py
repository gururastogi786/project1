from django.contrib import admin
from django.urls import path
from app_1.views import *
from app_1 import views
from app_1.views import UserList,UserDetail
# from app_1.views import views

urlpatterns = [

    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path("state/", ListState.as_view()),
    path("district/", ListDistrict.as_view()),
    path("village/", ListVillage.as_view()),
    path("user/", ListUser.as_view()),
    path('api/user/', UserList.as_view()),
    path('api/user/<int:pk>',UserDetail.as_view()),
    

]