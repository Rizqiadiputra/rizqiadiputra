from django.shortcuts import render

# from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse("Kamu di Index")

def home(request):
    return render(request,'cv/index.html',{})

def about(request):
    return render(request, 'cv/about.html',{})

def services(request):
    return render(request,'cv/services.html',{})

def portfolio(request):
    return render(request,'blog/daftar_post.html',{})