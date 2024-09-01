from django.shortcuts import render
from rest_framework import viewsets
from api_app.models import Turma
from api_app.models import Person
from api_app.models import Student
from api_app.models import Admin
from api_app.serializers import TurmaSerializer
from api_app.serializers import PersonSerializer
from api_app.serializers import StudentSerializer
from api_app.serializers import AdminSerializer
# Create your views here.

class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

    