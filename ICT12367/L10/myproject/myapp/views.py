from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Person

# Create your views here.
def index(request):
    # ดึงข้อมูลทั้งหมดจากโมเดล Person
    all_person = Person.objects.all()
    return render(request, "index.html", {"all_person": all_person})

def about(request):
    # ส่งข้อมูลไปยัง template
    return render(request, "about.html")

def form(request):
    return render(request, "form.html")