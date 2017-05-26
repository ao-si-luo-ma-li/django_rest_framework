from rest_framework import routers
from .views import UserViewSet, EntryVewSet

router = routers.DefaultRouter()
router.register(r'entries', EntryVewSet)
router.register(r'users', UserViewSet)
