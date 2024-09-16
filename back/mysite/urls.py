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
import os
import threading 
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
#from blog.models import Person, Student, Turma, Admin
from django.views.decorators.csrf import csrf_exempt
# Define a view diretamente no arquivo urls.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

file_lock = threading.Lock()

def readArqv(file):
    file_path = os.path.join(BASE_DIR, file)
    lista = []
     # Acquire the lock before accessing the file
    with file_lock:
        with open(file_path, 'r') as f:
            for line in f:
                lista.append(line.split(','))
    return lista

def getArqv(file, key):
    file_path = os.path.join(BASE_DIR, file)
    lista = []
    with file_lock:
        with open(file_path, 'r') as f:
            for line in f:
                lista.append(line.split(','))
    for elem in lista:
        if elem[0] == key:
            return elem
    return None

def writeArqv(file, lista):
    file_path = os.path.join(BASE_DIR, file)
    with file_lock:
        with open(file_path, 'w') as f:
            f.write(','.join(lista))
    return

def saveArqv(file, busca):
    file_path = os.path.join(BASE_DIR, file)
    string = ''
    resultado = []
    lista = []
    with file_lock:
        with open(file_path, 'r') as f:
            for line in f:
                lista = line.split(',')
                if lista[0] == busca[0]:
                    lista = busca
                resultado.append(','.join(lista))
                string = string + ','.join(lista)

        with open(file_path, 'w') as f:
            f.write(string)
    return

def appendArqv(file, busca):
    file_path = os.path.join(BASE_DIR, file)
    with file_lock:
        with open(file_path, 'a') as f:
            f.write(','.join(busca))
            f.write('\n')
    return


def aluno_login(request):
    #admin = Admin.objects.get(CPF='admin')
    admin = readArqv("adm.txt")
    prazo = admin[0][0]
    cpf = request.GET.get('cpf', None)

    turmas = readArqv("turmas.txt")
    flag = True
    for turma in turmas:
        if int(turma[6]) != 0: #vagas
            flag = False

    if flag:
        return JsonResponse({'error': 'servidor cheio por favor aguarde'}, status=405)
    if not cpf:
        return JsonResponse({'error': 'CPF é obrigatório'}, status=400)

    
    student = getArqv("alunos.txt", cpf)
    if student == None:
        return JsonResponse({'error': 'Aluno não encontrado'}, status=407)
    if prazo == 'False':
        return JsonResponse({'error': 'Prazo encerrado'}, status=405)

   
    if student[2] == 'True':
        aux = getArqv("turmas.txt", student[3])
        return JsonResponse({'message': 'Matrícula já realizada','turma:': aux[1],"trilha":aux[4], "is_matutino": aux[2]},status=200)
    

     # Serializar a instância do modelo Studen

    student_data = {
        'name': student[1],
        'CPF': student[0],
        'matriculado': student[2],
        # Adicione outros campos conforme necessário
    }

    turmas = readArqv("turmas.txt")
    for turma in turmas:
        reservas = turma[7].split('.')
        if student[0] in reservas:
            return JsonResponse({'error': 'Aluno já reservou uma vaga'}, status=406)
    
    for turma in turmas:
        reservas = turma[7].split('.')
        if int(turma[6]) > 0:   #vagas
            turma[6] = str(int(turma[6]) - 1)
            reservas.append(student[0])
        turma[7] = '.'.join(reservas)
        saveArqv("turmas.txt", turma)

    #printa()

    return JsonResponse(student_data, safe=False, status=200)

def turnos(request):
    turmas = readArqv("turmas.txt")
    vagasMatutino = 0
    vagasVespertino = 0
    for turma in turmas:
        if turma[2]=='True':
            vagasMatutino += int(turma[6])
        if turma[3]=='True':
            vagasVespertino += int(turma[6])

    turnos = [
        {'id': 1, 'name': 'Manhã', 'vagas': vagasMatutino},
        {'id': 2, 'name': 'Tarde', 'vagas': vagasVespertino},
    ]
    return JsonResponse(turnos, safe=False, status=200)

def turmasMatutino(request):
    turmas = readArqv("turmas.txt")
    aux = []
    for turma in turmas:
        if turma[2] == 'True':
            aux.append(turma)

    return JsonResponse(aux, safe=False, status=200)

def turmasVespertino(request):
    turmas = readArqv("turmas.txt")
    aux = []
    for turma in turmas:
        if turma[3] == 'True':
            aux.append(turma)

    return JsonResponse(aux, safe=False, status=200)



@csrf_exempt
def matricula(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            admin = readArqv("adm.txt")
            cpf = data.get('cpf')
            turma_id = data.get('turma_id')

            if not cpf:
                return JsonResponse({'error': 'CPF é obrigatório'}, status=400)

            if not turma_id:
                return JsonResponse({'error': 'Turma é obrigatória'}, status=401)
        
            student = getArqv("alunos.txt", cpf)
            

            turma = getArqv("turmas.txt", turma_id)
           
            if student[2] == 'True':
                return JsonResponse({'error': 'Matrícula já realizada'}, status=402)

            if int(turma[6]) <= 0:
                if student[0] not in turma[7].split('.'):
                    return JsonResponse({'error': 'Turma sem vagas'}, status=403)    
                
            count = int(admin[0][1])
            reservas = turma[7].split('.')
            if student[0] in reservas:
                student[3] = turma[0]
                student[2] = "True"
                saveArqv("alunos.txt", student)
                turma[5] = str(int(turma[5]) - 1)
                saveArqv("turmas.txt", turma)
                if turma[5] == "0":
                    count -= 1
                    admin[0][1] = str(count)
                    writeArqv("adm.txt", admin[0])
                    if count == 0:
                        aux1 = readArqv("turmas.txt")
                        for aux2 in aux1:
                            if int(aux2[5]) > 0:
                                aux2[6] = str(int(aux2[6]) - 1)
                                saveArqv("turmas.txt", aux2)
                                
                turmas = readArqv("turmas.txt")
                for aux in turmas:
                    reservaAux = aux[7].split('.')
                    if student[0] in reservaAux:
                        reservaAux.remove(student[0])
                        if turma_id != str(aux[0]):
                            aux[6] = str(int(aux[6])+1)
                    aux[7] = '.'.join(reservaAux)
                    saveArqv("turmas.txt", aux)
                
                

                        
                return JsonResponse({'message': 'Matrícula realizada com sucesso'}, status=200)
            return JsonResponse({'message': 'Falha na matrícula'}, status=405)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Dados inválidos'}, status=406)
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=407)

def relatorio(request):
    if request.method == 'GET':
        turmas =  readArqv("turmas.txt")
        students = readArqv("alunos.txt")
        retorno = {}

        for turma in turmas:
            lista = []
            if turma[2] == 'True':
                string = 'Matutino'
            if turma[3] == 'True':
                string = 'Vespertino'
            retorno[turma[1]] = [turma[0], turma[4], string]
            for student in students:
                if student[3] == turma[0]:
                    lista.append(student)
            retorno[turma[1]].append(lista)

        return JsonResponse(retorno, safe=False, status=200)
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)

def printa():
    turmas = readArqv("turmas.txt")
    print('------------------------------------------')
    for turma in turmas:
        print(turma[6], turma[1], turma[7])
    print('------------------------------------------')
@csrf_exempt
def cadastrar_cpf(request):
    if request.method == 'POST':
        try:
            if not request.body:
                return JsonResponse({'error': 'Corpo da requisição vazio'}, status=400)
            
            
            data = json.loads(request.body)

            cpf = data.get('cpf')
            name = data.get('name')

            if not cpf:
                return JsonResponse({'error': 'CPF é obrigatório'}, status=400)

            if not name:
                return JsonResponse({'error': 'Nome é obrigatório'}, status=400)
            
            student = [cpf,name, 'False', 'None', ' ']

            students = readArqv('alunos.txt')

            for studante in students:
                if studante[0] == cpf:
                    return JsonResponse({'error': 'CPF já cadastrado'}, status=200)

            appendArqv("alunos.txt", student)

            return JsonResponse({'message': 'Aluno cadastrado com sucesso'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Dados inválidos'}, status=400)
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)

def cadastrados(request):
    students = readArqv("alunos.txt")
    #students = [student for student in students if student['matriculado']]
    return JsonResponse(students, safe=False, status=200)

def timeOut(request):
    cpf = request.GET.get('cpf', None)
    if not cpf:
        return JsonResponse({'error': 'CPF é obrigatório'}, status=400)

    
    student = getArqv("alunos.txt", cpf)
    if student == None:
        return JsonResponse({'error': 'Aluno não encontrado'}, status=404)

    turmas = readArqv("turmas.txt")

    for turma in turmas:
        reservas = turma[7].split('.')
        if cpf in reservas:
            turma[6] = str(int(turma[6]) + 1)
            reservas.remove(student[0])
        turma[7] = '.'.join(reservas)
        saveArqv("turmas.txt", turma)

    return JsonResponse({'message': 'LogOut do aluno com sucesso'}, status=200)
def prazoEncerrado(request):
    admin = readArqv("adm.txt")
    admin[0][0] = 'False'
    writeArqv("adm.txt", admin[0])
    return JsonResponse({'message': 'Prazo encerrado'}, status=200)

def abrirPrazo(request):
    admin = readArqv("adm.txt")
    admin[0][0] = 'True'
    alunos = readArqv("alunos.txt")
    turmas = readArqv("turmas.txt")
    qtdTurmas = len(turmas)
    qtdStudents = len(alunos)
    for aluno in alunos:
        aluno[2] = "False"
        aluno[3] = "None"
        saveArqv("alunos.txt", aluno)

    max = qtdStudents//qtdTurmas
    max = max + 1
    resto = qtdStudents % qtdTurmas
    admin[0][1] = str(resto)
    writeArqv("adm.txt", admin[0])
    for turma in turmas:
        turma[6] = str(max)
        turma[5] = str(max)
        turma[7] = ''
        saveArqv("turmas.txt", turma)
    return JsonResponse({'message': 'Prazo aberto'}, status=200)

def reservas(request):
    cpf = request.GET.get('cpf', None)
    if not cpf:
        return JsonResponse({'error': 'CPF é obrigatório'}, status=400)


    student = getArqv("alunos.txt", cpf)
    if student == []:
        return JsonResponse({'error': 'Aluno não encontrado'}, status=404)

    turmas = readArqv("turmas.txt")
    retorno = []
    for turma in turmas:
        reservas = turma[7].split('.')
        if student[0] in reservas:
            retorno.append(turma[1])

    return JsonResponse(retorno, safe=False, status=200)

def restantes(request):
    admin = readArqv("adm.txt")
    turmas = readArqv("turmas.txt")
    count = int(admin[0][1])
    retorno = []
    for turma in turmas:
        if count <= 0:
            retorno.append((turma[1],int(turma[5])-1))
        else:
            retorno.append((turma[1],int(turma[5])))

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
    path('aluno/matriculas_restantes',restantes, name='restantes'),
]
