from django.http import Http404
from django.shortcuts import redirect, render
from .models import *
from django.views.generic import ListView
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'index.html')

#Curso
class CursoList(ListView):
    model = Curso

def getCurso(request, idCurso):
    try:
        curso = Curso.objects.get(pk=idCurso)
    except Curso.DoesNotExist:
        raise Http404("Curso não existe")
    return render(request, 'cursos/index.html', {'curso': curso})

def inserirCurso(request):
    return render(request, 'cursos/inserir.html')

def salvarCurso(request):
    curso = Curso()
    curso.nome = request.POST['nome']
    curso.save()
    return HttpResponseRedirect('/cursos')

def excluirCurso(request, idCurso):
    Curso.objects.filter(id=idCurso).delete()
    return HttpResponseRedirect('/cursos')

def disciplinasCurso(request, idCurso):
    cursoDisciplinas = CursoDisciplina.objects.filter(curso=idCurso)
    disciplinas = []
    for cursoDisciplina in cursoDisciplinas.all():
        disciplina = Disciplina.objects.get(id=cursoDisciplina.disciplina.id)
        disciplinas.append(disciplina)
    curso = Curso.objects.get(id=idCurso)
    return render(request, 'cursos/disciplinas.html', {'curso': curso, 'disciplinas': disciplinas})

def excluirDisciplinasCurso(request, idCurso, idDisciplina):
    CursoDisciplina.objects.filter(curso=idCurso, disciplina=idDisciplina).delete()
    return HttpResponseRedirect('/cursos/'+str(idCurso)+'/disciplinas')

def adicionarDisciplinasCurso(request, idCurso):
    curso = Curso.objects.get(id=idCurso)
    disciplinas = Disciplina.objects.all()
    return render(request, 'cursos/adicionar-disciplinas.html', {'curso': curso, 'disciplinas': disciplinas})

def salvarDisciplinaCurso(request, idCurso):
    cursoDisciplina = CursoDisciplina()
    curso = Curso.objects.get(pk=idCurso)
    cursoDisciplina.curso = curso
    disciplina = Disciplina.objects.get(pk=request.POST['idDisciplina'])
    cursoDisciplina.disciplina = disciplina
    cursoDisciplina.save(force_insert=True)
    return HttpResponseRedirect('/cursos/'+str(idCurso)+'/disciplinas')

def alunosCurso(request, idCurso):
    curso = Curso.objects.get(pk=idCurso)
    alunos = Aluno.objects.filter(curso=idCurso)
    return render(request, 'cursos/alunos.html', {'curso': curso, 'alunos': alunos})

#Disciplina
class DisciplinaList(ListView):
    model = Disciplina

def getDisciplina(request, idDisciplina):
    try:
        disciplina = Disciplina.objects.get(pk=idDisciplina)
    except Disciplina.DoesNotExist:
        raise Http404("Disciplina não existe")
    return render(request, 'disciplinas/index.html', {'disciplina': disciplina})

def inserirDisciplina(request):
    return render(request, 'disciplinas/inserir.html')

def salvarDisciplina(request):
    disciplina = Disciplina()
    disciplina.nome = request.POST['nome']
    disciplina.save()
    return HttpResponseRedirect('/disciplinas')

def excluirDisciplina(request, idDisciplina):
    Disciplina.objects.filter(id=idDisciplina).delete()
    return HttpResponseRedirect('/disciplinas')


#Aluno
class AlunoList(ListView):
    model = Aluno

def getAluno(request, idAluno):
    try:
        aluno = Aluno.objects.get(pk=idAluno)
    except Aluno.DoesNotExist:
        raise Http404("Aluno não existe")
    return render(request, 'alunos/index.html', {'aluno': aluno})

def inserirAluno(request):
    cursos = Curso.objects.all()
    return render(request, 'alunos/inserir.html', {'cursos': cursos})

def salvarAluno(request):
    aluno = Aluno()
    aluno.nome = request.POST['nome']
    aluno.curso = Curso.objects.get(pk=request.POST['idCurso'])
    aluno.save()
    return HttpResponseRedirect('/alunos')

def excluirAluno(request, idAluno):
    Aluno.objects.filter(id=idAluno).delete()
    return HttpResponseRedirect('/alunos')

def alunosDisciplina(request, idAluno):
    alunoDisciplinas = AlunoDisciplina.objects.filter(aluno=idAluno)
    aluno = Aluno.objects.get(id=idAluno)
    return render(request, 'alunos/disciplinas.html', {'aluno': aluno, 'alunoDisciplinas': alunoDisciplinas})

def excluirAlunoDisciplina(request, idAluno, idDisciplina):
    AlunoDisciplina.objects.filter(aluno=idAluno, disciplina=idDisciplina).delete()
    return HttpResponseRedirect('/alunos/'+str(idAluno)+'/disciplinas')

def adicionarAlunoDisciplina(request, idAluno):
    aluno = Aluno.objects.get(pk=idAluno)
    disciplinas = Disciplina.objects.all()
    situacoes = {0: 'Em Curso', 1: 'Aprovado', 2: 'Reprovado', 3: 'Trancado'}
    return render(request, 'alunos/adicionar-disciplinas.html', {'aluno': aluno, 'disciplinas': disciplinas, 'situacoes': situacoes})

def salvarDisciplina(request, idAluno):
    alunoDisciplina = AlunoDisciplina()
    aluno = Aluno.objects.get(pk=idAluno)
    alunoDisciplina.aluno = aluno
    disciplina = Disciplina.objects.get(pk=request.POST['idDisciplina'])
    alunoDisciplina.disciplina = disciplina
    alunoDisciplina.semestre = request.POST['semestre']
    alunoDisciplina.situacao = request.POST['situacao']
    alunoDisciplina.save(force_insert=True)
    return HttpResponseRedirect('/alunos/'+str(idAluno)+'/disciplinas')
