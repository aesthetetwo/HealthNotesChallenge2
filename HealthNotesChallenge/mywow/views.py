
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

from .forms import SignInForm

# Create your views here.
def mywow(request):
    if request.method == 'GET':
        form = SignInForm()
        template = loader.get_template('mywow.html')
        context = {'SignIn': form}
        return HttpResponse(template.render(context, request))

def page1(request):
    return HttpResponse("Hello, World!")
