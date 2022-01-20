
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import SignInForm
from .models import Practitioner


# Create your views here.

def mywow(request):
    if request.method == 'GET':
        form = SignInForm(request.GET)
        if form.is_valid():
            post=request.GET
            form.save()
            return redirect('page1') 
        template = loader.get_template('mywow.html')
        context = {'SignIn': form}
        return HttpResponse(template.render(context, request))

def page1(request):
    # return HttpResponse("page1")
    # dictionary for initial data with
    # field names as keys
    context ={}
    # add the dictionary during initialization
    context["dataset"] = Practitioner.objects.all()
    return render(request, "page1template.html", context)



