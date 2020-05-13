from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def home(request):
    user = request.user
    if user.is_authenticated:
        return HttpResponseRedirect(reverse('profile'))
    return render(request, 'home.html')

def profile(request):
    if user.is_authenticated:
        return render(request, 'user.html')

def basket(request):
    return render(request, 'basket.html')

