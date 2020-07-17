from rest_framework import routers
from .viewsets import *

router = routers.SimpleRouter()
router.register('clientes',ClienteViewSet)

urlpatterns = router.urls