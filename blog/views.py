from django.shortcuts import render

# Create your views here.
def daftar_post(request):
    return render(request, 'blog/daftar_post.html',{})