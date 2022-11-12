from django.contrib import admin
from django.urls import path, include
from school_enrollment.views import AlunosViewSet, CursosViewSet, MatriculaViewSet, DisciplinasViewSet, ListaAlunoMatriculas, ListaAlunosMatriculados, ListaCursoDisciplinas
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('disciplinas', DisciplinasViewSet, basename='Disciplinas')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('cursos/<int:pk>/disciplinas/', ListaCursoDisciplinas.as_view()),
    path('alunos/<int:pk>/matriculas/', ListaAlunoMatriculas.as_view()),
    path('cursos/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
