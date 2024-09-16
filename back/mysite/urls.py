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
from blog.models import Person, Student, Turma, Admin
from django.views.decorators.csrf import csrf_exempt
# Define a view diretamente no arquivo urls.py
def aluno_login(request):
    admin = Admin.objects.get(CPF='admin')
    prazo = admin.open
    cpf = request.GET.get('cpf', None)
    turmas = Turma.objects.all()
    flag = True
    for turma in turmas:
        if turma.vagas != 0:
            flag = False

    if flag:
        return JsonResponse({'error': 'servidor cheio por favor aguarde'}, status=405)
    if not cpf:
        return JsonResponse({'error': 'CPF é obrigatório'}, status=400)

    try:
        student = Student.objects.get(CPF=cpf)
    except Student.DoesNotExist:
        return JsonResponse({'error': 'Aluno não encontrado'}, status=407)
    if prazo == 'False':
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

    turmas = Turma.objects.all()
    for turma in turmas:
        reservas = turma.reservas.split(',')
        if student.CPF in reservas:
            return JsonResponse({'error': 'Aluno já reservou uma vaga'}, status=406)
    
    for turma in turmas:
        reservas = turma.reservas.split(',')
        if turma.vagas > 0:
            turma.vagas -= 1
            reservas.append(student.CPF)
        turma.reservas = ','.join(reservas)
        turma.save()

    printa()

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
            admin = Admin.objects.get(CPF='admin')
            cpf = data.get('cpf')
            turma_id = data.get('turma_id')

            if not cpf:
                return JsonResponse({'error': 'CPF é obrigatório'}, status=400)

            if not turma_id:
                return JsonResponse({'error': 'Turma é obrigatória'}, status=401)
        
            student = Student.objects.get(CPF=cpf)
            

            turma = Turma.objects.get(id=turma_id)
           
            if student.matriculado:
                return JsonResponse({'error': 'Matrícula já realizada'}, status=402)

            if turma.vagas == 0:
                if student.CPF not in turma.reservas:
                    return JsonResponse({'error': 'Turma sem vagas'}, status=403)    
                
            count = int(admin.count)
            print (turma.name,turma.reservas)
            reservas = turma.reservas.split(',')
            if student.CPF in reservas:
                student.turma = turma
                student.matriculado = True
                student.save()
                turma.max_size -= 1
                turma.save()
                if turma.max_size == 0:
                    count -= 1
                    admin.count = str(count)
                    admin.save()
                    if count == 0:
                        aux1 = Turma.objects.all()
                        for aux2 in aux1:
                            if aux2.max_size != 0:
                                aux2.vagas -= 1
                                aux2.save()
                                
                turmas = Turma.objects.all()
                x = 0
                for aux in turmas:
                    printa()
                    x += 1
                    print(turma.name)
                    print(x)
                    reservaAux = aux.reservas.split(',')
                    if student.CPF in reservaAux:
                        reservaAux.remove(student.CPF)
                        print(turma_id != str(aux.id))
                        if turma_id != str(aux.id):
                            aux.vagas += 1
                    aux.reservas = ','.join(reservaAux)
                    aux.save()
                
                

                        
                return JsonResponse({'message': 'Matrícula realizada com sucesso'}, status=200)
            return JsonResponse({'message': 'Falha na matrícula'}, status=405)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Dados inválidos'}, status=406)
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=407)

def relatorio(request):
    if request.method == 'GET':
        turmas = list(Turma.objects.values())
        students = list(Student.objects.values())
        retorno = {}

        for turma in turmas:
            lista = []
            if turma['matutino']:
                string = 'Matutino'
            if turma['vespertino']:
                string = 'Vespertino'
            retorno[turma['name']] = [turma['id'], turma['trilha'], string]
            for student in students:
                if student['turma_id'] == turma['id']:
                    lista.append(student)
            retorno[turma['name']].append(lista)

        return JsonResponse(retorno, safe=False, status=200)
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)

def printa():
    turmas = Turma.objects.all()
    print('------------------------------------------')
    for turma in turmas:
        print(turma.vagas, turma.name, turma.reservas)
    print('------------------------------------------')
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

            students = list(Student.objects.values())

            for studante in students:
                if studante['CPF'] == cpf:
                    return JsonResponse({'error': 'CPF já cadastrado'}, status=409)

            student.save()

            return JsonResponse({'message': 'Aluno cadastrado com sucesso'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Dados inválidos'}, status=400)
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)

def cadastrados(request):
    students = list(Student.objects.values())
    #students = [student for student in students if student['matriculado']]
    return JsonResponse(students, safe=False, status=200)

def timeOut(request):
    cpf = request.GET.get('cpf', None)
    if not cpf:
        return JsonResponse({'error': 'CPF é obrigatório'}, status=400)

    try:
        student = Student.objects.get(CPF=cpf)
    except Student.DoesNotExist:
        return JsonResponse({'error': 'Aluno não encontrado'}, status=404)

    turmas = Turma.objects.all()

    for turma in turmas:
        print(turma.vagas, turma.name, turma.reservas)
        reservas = turma.reservas.split(',')
        if cpf in reservas:
            turma.vagas += 1
            reservas.remove(student.CPF)
            turma.save()
        turma.reservas = ','.join(reservas)
        turma.save()
    for turma in turmas:
        print(turma.vagas, turma.name, turma.reservas)

    return JsonResponse({'message': 'LogOut do aluno com sucesso'}, status=200)
def prazoEncerrado(request):
    admin = Admin.objects.get(CPF='admin')
    admin.open = 'False'
    return JsonResponse({'message': 'Prazo encerrado'}, status=200)
def abrirPrazo(request):
    admin = Admin.objects.get(CPF='admin')
    admin.open = 'True'
    qtdTurmas = Turma.objects.all().count()
    print(qtdTurmas)
    qtdStudents = Student.objects.all().count()
    print(qtdStudents)
    alunos = Student.objects.all()
    for aluno in alunos:
        aluno.matriculado = False
        aluno.turma = None
        aluno.save()

    max = qtdStudents//qtdTurmas
    max = max + 1
    resto = qtdStudents % qtdTurmas
    admin.count = str(resto)
    admin.save()
    turmas = Turma.objects.all()
    for turma in turmas:
        turma.vagas = max
        turma.max_size = max
        turma.reservas = ''
        turma.save()
    return JsonResponse({'message': 'Prazo aberto'}, status=200)

def reservas(request):
    cpf = request.GET.get('cpf', None)
    if not cpf:
        return JsonResponse({'error': 'CPF é obrigatório'}, status=400)

    try:
        student = Student.objects.get(CPF=cpf)
    except Student.DoesNotExist:
        return JsonResponse({'error': 'Aluno não encontrado'}, status=404)

    turmas = Turma.objects.all()
    retorno = []
    for turma in turmas:
        reservas = turma.reservas.split(',')
        if student.CPF in reservas:
            retorno.append(turma.name)

    return JsonResponse(retorno, safe=False, status=200)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('adm/cadastrados', cadastrados, name='cadastrados'),
    path('aluno/login', aluno_login, name='aluno_login'),
    path('turnos', turnos , name='turnos'),
    path('matutino/turmas', turmasMatutino , name='turnos'),
    path('vespertino/turmas', turmasVespertino , name='turnos'),
    path('aluno/realizar_matricula',matricula, name='matricula'),
    path('adm/relatorio',relatorio, name='relatorio'),
    path('escola/cadastrar_cpf',cadastrar_cpf, name='cadastrar_cpf'),
    path('aluno/timeOut',timeOut, name='logOut'),
    path('adm/prazo_encerrado',prazoEncerrado, name='prazo_encerrado'),
    path('adm/abrir_prazo',abrirPrazo, name='abrir_prazo'),
    path('aluno/reservas',reservas, name='reservas'),
]
