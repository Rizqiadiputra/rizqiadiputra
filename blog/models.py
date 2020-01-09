from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

#class = object
#Post = nama model
#models.Model = Post adalah django model, Post akan disimpan di database
#penulis, judul etc = kolom pada Model Post
#CharField = string yang dibatasi jumlahnya
#TextField = string yang panjang (tidak dibatasi jumlahnya)
#DateTimeField = tanggal dan waktu
#ForeignKey = link ke model lain (kunci tamu)
class Post(models.Model):
    penulis = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    judul = models.CharField(max_length=200)
    isi = models.TextField()
    tgl_buat = models.DateTimeField(default=timezone.now)
    tgl_terbit = models.DateTimeField(blank=True, null=True)

    #def = fungsi atau method
    #terbit = nama sebuah method
    def terbit(self):
        self.tgl_terbit = timezone.now()
        self.save()

    #saat memanggil __str__, kita akan mendapatkan judul
    def __str__(self):
        return self.judul