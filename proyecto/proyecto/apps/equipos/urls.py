from rest_framework import routers
from .viewsets import *

router = routers.SimpleRouter()
router.register('estados',EstadoViewSet)
router.register('equipos',EquipoViewSet)

urlpatterns = router.urls