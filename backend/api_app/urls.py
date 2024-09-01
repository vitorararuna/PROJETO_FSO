from django.urls import path, include
from rest_framework import routers
from api_app.views import TurmaViewSet
from api_app.views import PersonViewSet
from api_app.views import StudentViewSet
from api_app.views import AdminViewSet

router = routers.DefaultRouter()
router.register(r'turma', TurmaViewSet)
router.register(r'person', PersonViewSet)
router.register(r'student', StudentViewSet)
router.register(r'Administrador', AdminViewSet)


urlpatterns = [
    path('',include(router.urls)),
]