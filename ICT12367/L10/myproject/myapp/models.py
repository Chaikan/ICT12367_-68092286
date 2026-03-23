from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)  # 👈 เพิ่ม default
    date = models.DateField(auto_now_add=True, null=True)  # 👈 เพิ่ม null=True

    def __str__(self):
        return self.name + ", "+str(self.age)