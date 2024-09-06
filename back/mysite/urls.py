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
import json
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from blog.models import Person, Student, Turma
from django.views.decorators.csrf import csrf_exempt
# Define a view diretamente no arquivo urls.py
def aluno_login(request):
    prazo_encerrado = False

    cpf = request.GET.get('cpf', None)
    if not cpf:
        return JsonResponse({'error': 'CPF é obrigatório'}, status=400)

    try:
        student = Student.objects.get(CPF=cpf)
    except Student.DoesNotExist:
        return JsonResponse({'error': 'Aluno não encontrado'}, status=404)
    if prazo_encerrado:
        return JsonResponse({'error': 'Prazo encerrado'}, status=405)

    if student.matriculado:
        return JsonResponse({'message': 'Matrícula já realizada','turma:': student.turma.name,"trilha":student.turma.trilha},status=200)
    
     # Serializar a instância do modelo Studen

    student_data = {
        'name': student.name,
        'CPF': student.CPF,
        'matriculado': student.matriculado,
        'entry_time': student.entry_time,
        'time_limit': student.time_limit,
        # Adicione outros campos conforme necessário
    }

    return JsonResponse(student_data, safe=False, status=200)

def turnos(request):
    turmas = list(Turma.objects.values())
    vagasMatutino = 0
    vagasVespertino = 0
    for turma in turmas:
        if turma['matutino']:
            vagasMatutino += turma['vagas']
        if turma['vespertino']:
            vagasVespertino += turma['vagas']

    turnos = [
        {'id': 1, 'name': 'Manhã', 'vagas': vagasMatutino},
        {'id': 2, 'name': 'Tarde', 'vagas': vagasVespertino},
    ]
    return JsonResponse(turnos, safe=False, status=200)

def turmasMatutino(request):
    turmas = list(Turma.objects.values())
    aux = []
    for turma in turmas:
        if turma['matutino']:
            aux.append(turma)

    return JsonResponse(aux, safe=False, status=200)

def turmasVespertino(request):
    turmas = list(Turma.objects.values())
    aux = []
    for turma in turmas:
        if turma['vespertino']:
            aux.append(turma)

    return JsonResponse(aux, safe=False, status=200)



@csrf_exempt
def matricula(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            cpf = data.get('cpf')
            turma_id = data.get('turma_id')

            if not cpf:
                return JsonResponse({'error': 'CPF é obrigatório'}, status=400)

            if not turma_id:
                return JsonResponse({'error': 'Turma é obrigatória'}, status=400)
        
            student = Student.objects.get(CPF=cpf)
            turma = Turma.objects.get(id=turma_id)

            if student.matriculado:
                return JsonResponse({'error': 'Matrícula já realizada'}, status=400)

            if turma.vagas == 0:
                return JsonResponse({'error': 'Turma sem vagas'}, status=400)

            student.turma = turma
            student.matriculado = True
            student.save()

            turma.vagas -= 1
            turma.save()
            return JsonResponse({'message': 'Matrícula realizada com sucesso'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Dados inválidos'}, status=400)
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)

def relatorio(request):
    if request.method == 'GET':
        turmas = list(Turma.objects.values())
        students = list(Student.objects.values())
        retorno = {}

        for turma in turmas:
            lista = []
            retorno[turma['name']] = [turma['id'], turma['trilha']]
            for student in students:
                if student['turma_id'] == turma['id']:
                    lista.append(student)
            retorno[turma['name']].append(lista)

        return JsonResponse(retorno, safe=False, status=200)
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)

@csrf_exempt
def cadastrar_cpf(request):
    if request.method == 'POST':
        try:
            if not request.body:
                return JsonResponse({'error': 'Corpo da requisição vazio'}, status=400)
            
            print('abacate')
            data = json.loads(request.body)

            cpf = data.get('cpf')
            name = data.get('name')

            if not cpf:
                return JsonResponse({'error': 'CPF é obrigatório'}, status=400)

            if not name:
                return JsonResponse({'error': 'Nome é obrigatório'}, status=400)
            
            student = Student(CPF=cpf, name=name)

            # students = list(Student.objects.values())

            # for student in students:
            #     if student['CPF'] == cpf:
            #         return JsonResponse({'error': 'CPF já cadastrado'}, status=409)

            student.save()

            return JsonResponse({'message': 'Aluno cadastrado com sucesso'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Dados inválidos'}, status=400)
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aluno/login', aluno_login, name='aluno_login'),
    path('turnos', turnos , name='turnos'),
    path('matutino/turmas', turmasMatutino , name='turnos'),
    path('vespertino/turmas', turmasVespertino , name='turnos'),
    path('aluno/realizar_matricula',matricula, name='matricula'),
    path('adm/relatorio',relatorio, name='relatorio'),
    path('escola/cadastrar_cpf',cadastrar_cpf, name='cadastrar_cpf'),
]
