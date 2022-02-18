from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import *
from .models import *


# Django is based on MVT (Model View Template) architecture.
# Views are a key component of this architecture.
# Views are function based in this case.
#
# Create your views here.

# Function with Logic for Home Page
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

# Function with Logic for Portal Page
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

# Function for After Portal Page
def postportal(request):
    if request.method == 'GET':
        context = {}
        template = loader.get_template('postportaltemplate.html')
        return HttpResponse(template.render(context, request))

# Function for Practitioners page (aka page1)
def page1(request):
    # return HttpResponse("page1")
    # dictionary for initial data with
    # field names as keys
    context ={}
    # add the dictionary during initialization
    context["dataset"] = Practitioner.objects.all()
    return render(request, "page1template.html", context)

# Function allowing deletions to Practitioners page to enable full CRUD    
def deletepractitioner(request, part_id = None):
    context = {}
    object = Practitioner.objects.get( practitioner_id=part_id )
    object.delete()
    return redirect('page1') 
    #return render(request, "page1template.html", context)    

# Function for Conditions Page
def conditions(request):
    # return HttpResponse("conditions")
    # dictionary for initial data with
    # field names as keys
    context ={}
    # add the dictionary during initialization
    context["dataset"] = Conditions.objects.all()
    return render(request, "conditionstemplate.html", context)

# Function allowing deletions Conditions to enable full CRUD    
def deleteconditions(request, part_id = None):
    context = {}
    object = Conditions.objects.get( conditions_id=part_id )
    object.delete()
    return redirect('conditions') 
    #return render(request, "conditionstemplate.html", context)

# Function for Treatments Page
def treatments(request):
    # return HttpResponse("treatments")
    # dictionary for initial data with
    # field names as keys
    context ={}
    # add the dictionary during initialization
    context["dataset"] = Treatments.objects.all()
    return render(request, "treatmentstemplate.html", context)

# Function allowing deletions Treatments to enable full CRUD    
def deletetreatments(request, part_id = None):
    context = {}
    object = Treatments.objects.get( treatments_id=part_id )
    object.delete()
    return redirect('treatments') 
    #return render(request, "treatmentstemplate.html", context)

# Function Allowing Posts
def posts(request):
    # return HttpResponse("treatments")
    # dictionary for initial data with
    # field names as keys
    context ={}
    # add the dictionary during initialization
    context["dataset"] = Posts.objects.all()
    return render(request, "poststemplate.html", context)

# Function Allowing Deletions Posts to enable full CRUD    
def deletepost(request,part_id =None):
    context = {}
    object = Posts.objects.get(post_id=part_id)
    object.delete()
    return redirect('posts') 
    #return render(request, "poststemplate.html", context)

# Function with Logic Allowing Update of Posts to enable full CRUD  
def updatepost(request,part_id =None):
    if request.method == 'GET' or request.method == 'POST':
    
        if part_id:
            obj_to_edit = Posts.objects.get(post_id=part_id)
            form = MakePostForm(instance=obj_to_edit)
        else:
            obj_to_edit = None
            form = MakePostForm()
            
        if id: #update
            form = MakePostForm(request.POST, instance=obj_to_edit)
        else: #create
            form = MakePostForm(request.POST)

        if form.is_valid():
            request.session['PostsPost'] = request.POST
            #object = Posts.objects.get(post_id=part_id)
            #object.delete()
            form.save()
            return redirect('posts') 
        template = loader.get_template('changeposttemplate.html')
        context = {'Post': form}
        return HttpResponse(template.render(context, request))




