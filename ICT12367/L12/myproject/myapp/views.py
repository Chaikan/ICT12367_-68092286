from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import Person

# หน้าแสดงรายการข้อมูลทั้งหมด
def index(request):
    all_person = Person.objects.all()
    return render(request, "index.html", {"all_person": all_person})

# หน้าแสดงข้อมูล About
def about(request):
    return render(request, "about.html")

# หน้าฟอร์มสำหรับเพิ่มข้อมูลใหม่ (ถ้ามี)
def form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')

        # 🔥 บันทึกข้อมูลลง DB
        Person.objects.create(
            name=name,
            age=age
        )

        return redirect('/')  # กลับไปหน้าตาราง

    return render(request, "form.html")

# ฟังก์ชันแก้ไขข้อมูล (Update)
def edit(request, person_id):
    # ใช้ get_object_or_404 เพื่อป้องกัน Error ถ้าไม่พบ ID ในฐานข้อมูล
    person = get_object_or_404(Person, id=person_id)
    
    if request.method == "POST":
        # รับค่าจาก input name="name" และ name="age" ใน edit.html
        person.name = request.POST.get('name')
        person.age = request.POST.get('age')
        person.save() # บันทึกลงฐานข้อมูล
        return redirect('/') # เมื่อบันทึกเสร็จให้กลับไปหน้าแรก
    
    # ถ้าไม่ใช่ POST (คือการกดเข้ามาดูหน้าฟอร์มครั้งแรก) ให้ส่งข้อมูล person ไปที่ Template
    return render(request, 'edit.html', {'person': person})

# ฟังก์ชันลบข้อมูล (Delete)
def delete(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    person.delete()
    return redirect("/")