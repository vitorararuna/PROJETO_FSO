from django.contrib import admin

from api_app.models import Turma
from api_app.models import Person
from api_app.models import Student
from api_app.models import Admin

# Register your models here.
admin.site.register(Turma)
admin.site.register(Person)
admin.site.register(Student)
admin.site.register(Admin)