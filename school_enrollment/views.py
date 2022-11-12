from rest_framework import viewsets, generics
from rest_framework.response import Response
from school_enrollment.models import Aluno, Curso, Matricula, Disciplina
from school_enrollment.serializer import AlunoSerializer, AlunoSerializerV2, CursoSerializer, CursoSerializerV2, MatriculaSerializer, ListaMatriculasSerializer, ListaAlunosMatriculadosSerializer, DisciplinaSerializer


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return AlunoSerializerV2
        else:
            return AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return CursoSerializerV2
        return CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    """Listando todas as matrículas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class DisciplinasViewSet(viewsets.ModelViewSet):
    """Listando todas as disciplinas"""
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer


class ListaCursoDisciplinas(generics.ListAPIView):
    """Listando todas disciplinas em um curso"""

    def get_queryset(self):
        return Disciplina.objects.filter(curso=self.kwargs['pk'])
    serializer_class = DisciplinaSerializer


class ListaAlunoMatriculas(generics.ListAPIView):
    """Listando as matrículas de um aluno ou aluna"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasSerializer


class ListaAlunosMatriculados(generics.ListAPIView):
    """Listando alunos e alunas matriculados em um curso"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer
