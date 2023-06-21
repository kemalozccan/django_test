from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Anasayfa")

def hakkimizda(request):
    return HttpResponse("Hakkımızda")

def iletisim(request):
    return HttpResponse("İletisim Bilgileri")