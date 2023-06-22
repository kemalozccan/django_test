from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
# Create your views here.

data = {
    "programlama" : "Programlama kategorisine ait kurslar",
    "web-gelistirme" : "Web geliştirme kategorisine ait kurslar",
    "mobil" : "Mobil uygulama kategorisine ait kurslar",
}


def index(request):
    return render(request,'courses/index.html')

def kurslar(request):
    category_list = list(data.keys())
    list_items = ""
    for category in category_list:
        redirect_url = reverse('courses_by_category',args=[category])
        list_items += f"<li><a href='{redirect_url}'>{category}</a></li>"

    html = f"<h1>Kurs Listesi : </h1><br><ul>{list_items}</ul>"
    return HttpResponse(html)

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
        text = data[category_name];
        return HttpResponse(text)
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