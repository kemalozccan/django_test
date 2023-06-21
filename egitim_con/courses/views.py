from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
# Create your views here.

data = {
    "programlama" : "Programlama kategorisine ait kurslar",
    "web-gelistirme" : "Web geliştirme kategorisine ait kurslar",
    "mobil" : "Mobil uygulama kategorisine ait kurslar",
}




def kurslar(request):
    return HttpResponse("Kurslar")

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
        redirect_text = category_list[category_id - 1]
        return redirect("/kurs/category/" + redirect_text)
    except:
        return HttpResponseNotFound("Yanlış Kategori Seçimi....")