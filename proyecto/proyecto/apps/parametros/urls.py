from rest_framework import routers
from .viewsets import *

router = routers.SimpleRouter()
router.register('pais',PaisViewSet)
router.register('provincia',ProvinciaViewSet)
router.register('localidad',LocalidadViewSet)
router.register('barrio',BarrioViewSet)
router.register('domicilio',DomicilioViewSet)

urlpatterns = router.urls