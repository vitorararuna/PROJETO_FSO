from django.contrib import admin
from .models import Person
from .models import Student
from .models import Admin
from .models import Turma
# Register your models here.

admin.site.register(Person)
admin.site.register(Student)
admin.site.register(Admin)
admin.site.register(Turma)