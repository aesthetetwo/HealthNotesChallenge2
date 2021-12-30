from django.shortcuts import render

from .forms import SignInForm

# Create your views here.
def mywow(request):
    if request.method == 'GET':
#        form = Sign_In_Form(request)
        return render(request, 'mywow.html')#, {'form': form})
