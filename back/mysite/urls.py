"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from blog.models import Person, Student

# Define a view diretamente no arquivo urls.py
def aluno_login(request):
    prazo_encerrado = False
    matricula_realizada = False
    matricula_numero = "123456"

    cpf = request.GET.get('cpf', None)
    if not cpf:
        return JsonResponse({'error': 'CPF é obrigatório'}, status=400)

    persons = list(Person.objects.values()) 
    student = list(Student.objects.values()) 

    if prazo_encerrado:
        return JsonResponse({'error': 'Prazo encerrado'}, status=400)

    if matricula_realizada:
        return JsonResponse(
            {'message': 'Matrícula já realizada', 'matricula': matricula_numero},
            status=409
        )

    return JsonResponse(student, safe=False, status=200)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aluno/login', aluno_login, name='aluno_login'),
]
