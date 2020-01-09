from django.contrib import admin
#import model Post
from .models import Post
# Register your models here.

#agar model visible di halaman admin, kita daftarkan model
admin.site.register(Post)