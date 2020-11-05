from django.db import models


class Aluno(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    curso = models.ForeignKey('Curso', models.DO_NOTHING, db_column='idCurso', blank=True, null=True) 

    class Meta:
        managed = False
        db_table = 'aluno'


class AlunoDisciplina(models.Model):
    aluno = models.ForeignKey('Aluno', models.DO_NOTHING, db_column='idAluno', primary_key=True) 
    disciplina = models.ForeignKey('Disciplina', models.DO_NOTHING, db_column='idDisciplina') 
    semestre = models.CharField(max_length=6)
    situacao = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aluno_disciplina'
        unique_together = (('aluno', 'disciplina', 'semestre'),)


class Curso(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'curso'


class Disciplina(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disciplina'

class CursoDisciplina(models.Model):
    curso = models.ForeignKey('Curso', models.DO_NOTHING, db_column='idCurso', primary_key=True)
    disciplina = models.ForeignKey('Disciplina', models.DO_NOTHING, db_column='idDisciplina')

    class Meta:
        managed = False
        db_table = 'curso_disciplina'
        unique_together = (('curso', 'disciplina'),)
