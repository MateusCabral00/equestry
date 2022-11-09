from school_enrollment.models import Aluno, Curso, Matricula
from rest_framework import serializers


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento', 'foto_do_aluno']


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['codigo_curso', 'descricao', 'nivel']


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []


class ListaMatriculasSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()


class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')

    class Meta:
        model = Matricula
        fields = ['aluno_nome']


class AlunoSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'


class CursoSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'
