from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from datetime import date, datetime
from .models import Course
# Create your views here.

data = {
    "programlama" : "Programlama kategorisine ait kurslar",
    "web-gelistirme" : "Web geliştirme kategorisine ait kurslar",
    "mobil-uygulamalar" : "Mobil uygulama kategorisine ait kurslar",
}

db = {
    'courses' : [
        {
            'title'         : 'JavaScript kursu',
            'description'   : 'JavaScript kurs açıklaması',
            'imageUrl'      : "javascripts.png",
            'slug'          : 'JavaScript-kursu',
            'date'          : datetime.now(),
            "isActive"      : True,
            "isUpdated"     : True
        },
        {
            'title'         : 'Python kursu',
            'description'   : 'Python kurs açıklaması',
            'imageUrl'      : "mobil.jpg",
            'slug'          : 'Python-kursu',
            'date'          : date(2022,9,10),
            "isActive"      : False,
            "isUpdated"     : False
        },
        {
            'title'         : 'Web geliştirme kursu',
            'description'   : 'Web geliştirme kurs açıklaması',
            'imageUrl'      : "web.png",
            'slug'          : 'Web-geliştirme-kursu',
            'date'          : date(2022,8,10),
            "isActive"      : True,
            "isUpdated"     : False
        }
    ],
    "categories" : [
        {"id"   : 1, "name"     : "programlama",        "slug"  : "programlama"},
        {"id"   : 2, "name"     : "web geliştirme",     "slug"  : "web-gelistirme"}, 
        {"id"   : 3, "name"     : "mobil",              "slug"  : "mobil-uygulamalar"}, 

        ]
}

def index(request):
    kurslar = Course.objects.all()
    kategoriler = db["categories"]    
    return render(request,'courses/index.html', {
        'categories'    : kategoriler,
        "courses"       : kurslar
    })

def details(request, kurs_adi):
    return HttpResponse(f"{kurs_adi} kursu detay sayfası")

# def getCoursesByCategory(request, category_name):
#     if (category_name=="programlama"):
#         text="programlama kategorisine ait kurslar"
#     elif (category_name == "web-gelistirme"):
#         text="web geliştirme ait kurslar"
#     else:
#         text="yanlış kategori seçimi"
#     return HttpResponse(text)

# Yukarıdaki if bloğu yerine; data adında bir dictionary oluşturduk. bu sayede kalabalık kod satırından aşağıdaki şekilde kurtulmuş olduk.abs

def getCoursesByCategory(request, category_name):
    try:
        category_text = data[category_name];
        return render(request, 'courses/kurslar.html', {
            'category' : category_name,
            'category_text' : category_text
        })
    except:
        return HttpResponseNotFound("Yanlış Kategori Seçimi")


def getCoursesByCategoryId(request, category_id):
    # "/kurs/category/" 'den sonra gelecek 1,2,3 sayılarına data dictionary deki value değerlerine karşılık gelen response'ları döndürür. 1,2,3 dışında herhangi bir sayı girilirse hata verilir. Ancak if bloğu ile hatanın önüne geçmiş oluruz. Ya da try-except ile hatayı önleriz.
    try:
        category_list = list(data.keys())
        # if (category_id>len(category_list)):
        #     return HttpResponseNotFound("Yanlış kategori Seçimi.")
        category_name = category_list[category_id - 1]
        redirect_url = reverse('courses_by_category',args=[category_name])
        return redirect(redirect_url)
    except:
        return HttpResponseNotFound("Yanlış Kategori Seçimi....")