from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'dashboard/home.html')
# def home(request):
#     return HttpResponse("Hello world!")

# from django.shortcuts import render

# def welcome(request):
#     return render(request, 'dashboard/welcome.html')