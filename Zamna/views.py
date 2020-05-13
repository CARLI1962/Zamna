from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'user.html')

def basket(request):
    return render(request, 'basket.html')
