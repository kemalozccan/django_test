
from django.urls import path
from . import views



urlpatterns = [
    
    path('list',views.kurslar),
    path('details', views.details),
    path("<category>", views.getCoursesByCategory),
    
]