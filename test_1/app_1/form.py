# from django.core import validators
# from django import forms
# from .models import User

# class UserRegistration(forms.ModelForm):
#  class Meta:
#   model = User
#   fields = ['user_name', 'email', 'roll','state', 'district', 'Village']
#   widgets = {
#    'user_name': forms.TextInput(attrs={'class':'form-control'}),
#    'email': forms.EmailInput(attrs={'class':'form-control'}),
#    'roll': forms.IntegerField(render_value=True, attrs={'class':'form-control'}),
#    'state': forms.TextInput(attrs={'class':'form-control'}),
#    'district': forms.TextInput(attrs={'class':'form-control'}),
#    'Village': forms.TextInput(attrs={'class':'form-control'}),
#   }