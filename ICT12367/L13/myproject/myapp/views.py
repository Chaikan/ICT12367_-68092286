from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import Person
from django.db.models import Q

# 🔥 หน้าแรก + ค้นหา
def index(request):
    query = request.GET.get('q')

    if query:
        q_filter = Q(name__icontains=query)

        # ถ้าเป็นตัวเลข → ค้นหาอายุ
        if query.isdigit():
            q_filter |= Q(age=int(query))

        all_person = Person.objects.filter(q_filter).distinct()
    else:
        all_person = Person.objects.all()

    return render(request, "index.html", {"all_person": all_person})


# 🔥 หน้า About
def about(request):
    return render(request, "about.html")


# 🔥 ฟอร์มเพิ่มข้อมูล
def form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')

        Person.objects.create(
            name=name,
            age=age
        )

        return redirect('/')  # กลับหน้า index

    return render(request, "form.html")


# 🔥 แก้ไขข้อมูล
def edit(request, person_id):
    person = get_object_or_404(Person, id=person_id)

    if request.method == "POST":
        person.name = request.POST.get('name')
        person.age = request.POST.get('age')
        person.save()
        return redirect('/')

    return render(request, 'edit.html', {'person': person})


# 🔥 ลบข้อมูล
def delete(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    person.delete()
    return redirect("/")