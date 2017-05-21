from rest_framework import routers
from .views import UserViewSet, EntryVewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'entries', EntryVewSet)