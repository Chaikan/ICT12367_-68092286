from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('form/', views.form, name='form'),
    
    # เพิ่ม 2 บรรทัดนี้เพื่อให้คลิกแก้ไขและลบจากหน้า index ได้
    path('edit/<int:person_id>/', views.edit, name='edit'),
    path('delete/<int:person_id>/', views.delete, name='delete'),
]