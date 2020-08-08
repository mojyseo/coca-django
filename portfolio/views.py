from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login



def signupuser(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'portfolio/home.html')
    context['form'] = form
    return render(request, 'portfolio/signupuser.html', context)



def home(request):
    return render(request, 'portfolio/home.html')



def about(request):
    return render(request, 'portfolio/about.html')


def connect(request):
    return render(request, 'portfolio/connect.html')