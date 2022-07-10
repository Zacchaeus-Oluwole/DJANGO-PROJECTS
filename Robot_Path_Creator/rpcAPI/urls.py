from rest_framework.routers import SimpleRouter
from .views import DestinationViewSet, PathViewSet

router = SimpleRouter()

router.register('destination', DestinationViewSet, basename= 'destination')
router.register('path', PathViewSet, basename='path')

urlpatterns = router.urls

