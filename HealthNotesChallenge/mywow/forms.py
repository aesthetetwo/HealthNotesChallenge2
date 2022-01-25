from django import forms
from django.forms import widgets
#from .models import Tag
from .models import *

class MakePostForm(forms.ModelForm):
  class Meta:
    model = Posts
    fields = '__all__'
    
class SignInForm(forms.ModelForm):
  class Meta:
    model = Practitioner
    fields = '__all__'
    #first_name = forms.CharField(max_length=255)
    #last_name = forms.CharField(max_length=255)
    #occupation = forms.CharField(max_length=255)
    #degree = forms.CharField(max_length=255)
    #email = forms.CharField(max_length=255) 
    #phone = forms.CharField(max_length=255)

class ConditionsForm(forms.ModelForm):
  class Meta:
    model = Conditions
    fields = '__all__'
    
class TreatmentsForm(forms.ModelForm):
  class Meta:
    model = Treatments
    fields = '__all__'  

