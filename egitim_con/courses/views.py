from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def kurslar(request):
    return HttpResponse("Kurslar")

def details(request):
    return HttpResponse("Kurs detay sayfası")

def getCoursesByCategory(request, category):
    return HttpResponse(f"{category} Kategorisindeki kurs listesi")