
from django.shortcuts import render , redirect
from django.template import loader

from portfolio.forms import ProjectRequest, UserRegistrationForm
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from .forms import ProjectRequest


@login_required
# Create your views here
def home(request):
    portfolios = Portfolio.objects.all()
    s = Service.objects.all()
    team_members = TeamMember.objects.all()
    context = {'portfolios': portfolios, 'services': s, 'team_members': team_members }
 
    if request.user.is_authenticated:
     
         username = request.user.username
         context['username']=username
    
    return render (request,'base.html', context )





def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Bienvenue {username}, Votre compte a été créé avec succès !')
            return redirect('/login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
def logout(request):
    messages.info(request,"you have succefully logged out")
    return redirect("login")



def project_request(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        email = request.POST.get('email')
        tel = request.POST.get('phone')
        projet = ProjectRequestModel.objects.create(name=name,description=description,email=email,phone=tel)
    return render(request, 'ProjetRequest.html')
