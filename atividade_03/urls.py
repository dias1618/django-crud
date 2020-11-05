from django.urls import path

from academico.views import *


urlpatterns = [
    path('', index),
    path('cursos/', CursoList.as_view()),
    path('cursos/<int:idCurso>', getCurso),
    path('cursos/inserir', inserirCurso),
    path('cursos/salvar', salvarCurso),
    path('cursos/<int:idCurso>/excluir', excluirCurso),
    path('cursos/<int:idCurso>/disciplinas', disciplinasCurso),
    path('cursos/<int:idCurso>/disciplinas/<int:idDisciplina>/excluir', excluirDisciplinasCurso),
    path('cursos/<int:idCurso>/disciplinas/adicionar', adicionarDisciplinasCurso),
    path('cursos/<int:idCurso>/disciplinas/salvar', salvarDisciplinaCurso),
    path('cursos/<int:idCurso>/alunos', alunosCurso),
    
    path('disciplinas/', DisciplinaList.as_view()),
    path('disciplinas/<int:idDisciplina>', getDisciplina),
    path('disciplinas/inserir', inserirDisciplina),
    path('disciplinas/salvar', salvarDisciplina),
    path('disciplinas/<int:idDisciplina>/excluir', excluirDisciplina),
    
    path('alunos/', AlunoList.as_view()),
    path('alunos/<int:idAluno>', getAluno),
    path('alunos/inserir', inserirAluno),
    path('alunos/salvar', salvarAluno),
    path('alunos/<int:idAluno>/excluir', excluirAluno),
    path('alunos/<int:idAluno>/disciplinas', alunosDisciplina),
    path('alunos/<int:idAluno>/disciplinas/<int:idDisciplina>/excluir', excluirAlunoDisciplina),
    path('alunos/<int:idAluno>/disciplinas/adicionar', adicionarAlunoDisciplina),
    path('alunos/<int:idAluno>/disciplinas/salvarDisciplina', salvarDisciplina),
    
]
