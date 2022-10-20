from rest_framework.routers import DefaultRouter

from .views import ParseView

router = DefaultRouter()

router.register(r'', ParseView, basename='recipes_list')

user_patterns = [
                ] + router.urls

urlpatterns = user_patterns