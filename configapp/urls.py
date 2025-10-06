from django.urls import path,include
from rest_framework.routers import Route, DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'Language', LanguageView)


urlpatterns = [
    path('', include(router.urls))
]