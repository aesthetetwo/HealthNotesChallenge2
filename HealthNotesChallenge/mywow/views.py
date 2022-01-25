from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import *
from .models import *


# Django is based on MVT (Model View Template) architecture.
# Views are a key component of this architecture.
# Views are function based.
#
# Create your views here.


def mywow(request):
    if request.method == 'GET' or request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            post=request.POST
            request.session['practitioner'] = post
            form.save()
            return redirect('portal') 
        template = loader.get_template('mywow.html')
        context = {'SignIn': form}
        return HttpResponse(template.render(context, request))

def portal(request):
    if request.method == 'GET' or request.method == 'POST':
        conditionsform = ConditionsForm(request.POST)
        treatmentsform = TreatmentsForm(request.POST)
        makepostform = MakePostForm(request.POST)
        if conditionsform.is_valid():
            request.session['ConditionsPost'] = request.POST
            conditionsform.save()
            return redirect('portal') 
        if treatmentsform.is_valid():
            request.session['TreatmentsPost'] = request.POST
            treatmentsform.save()
            return redirect('portal') 
        if makepostform.is_valid():
            request.session['PostsPost'] = request.POST
            makepostform.save()
            return redirect('postportal') 
        
        template = loader.get_template('portaltemplate.html')
        context = {'Conditions': conditionsform, 'Treatments': treatmentsform, 'Post': makepostform}
        return HttpResponse(template.render(context, request))

def postportal(request):
    if request.method == 'GET':
        context = {}
        template = loader.get_template('postportaltemplate.html')
        return HttpResponse(template.render(context, request))

def page1(request):
    # return HttpResponse("page1")
    # dictionary for initial data with
    # field names as keys
    context ={}
    # add the dictionary during initialization
    context["dataset"] = Practitioner.objects.all()
    return render(request, "page1template.html", context)

def conditions(request):
    # return HttpResponse("conditions")
    # dictionary for initial data with
    # field names as keys
    context ={}
    # add the dictionary during initialization
    context["dataset"] = Conditions.objects.all()
    return render(request, "conditionstemplate.html", context)

def treatments(request):
    # return HttpResponse("treatments")
    # dictionary for initial data with
    # field names as keys
    context ={}
    # add the dictionary during initialization
    context["dataset"] = Treatments.objects.all()
    return render(request, "treatmentstemplate.html", context)

def posts(request):
    # return HttpResponse("treatments")
    # dictionary for initial data with
    # field names as keys
    context ={}
    # add the dictionary during initialization
    context["dataset"] = Posts.objects.all()
    return render(request, "poststemplate.html", context)