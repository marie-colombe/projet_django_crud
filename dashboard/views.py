from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "html/dashboard.html")

def connect_view(request):
    return render(request, 'html/connect.html')
