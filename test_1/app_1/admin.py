from django.contrib import admin
from app_1.models import *

# Register your models here.

admin.site.register(State)
admin.site.register(District)
admin.site.register(Village)
admin.site.register(User)

# @admin.register(State)
# class StateAdmin(admin.ModelAdmin):
#     list_display = ["id","s_name"]

# @admin.register(District)
# class DistricAdmin(admin.ModelAdmin):
#     list_display = ["id","state_name","d_name"]

# @admin.register(Village)
# class VillageAdmin(admin.ModelAdmin):
#     list_display = ["id","dis_name","v_name"]

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ["id","user_name","roll","email","state","district","Village"]