
from django.urls import path
from . import views



urlpatterns = [
    path('',views.index),
    path('list',views.kurslar),
    path('<kurs_adi>', views.details),
    path("category/<int:category_id>", views.getCoursesByCategoryId),
    path("category/<str:category_name>", views.getCoursesByCategory, name="courses_by_category"),
]