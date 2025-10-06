from django.urls import path,include
from rest_framework.routers import Route, DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'Language', LanguageView)
router.register(r'Content', ContentView)
router.register(r'ContentText', ContentTextView)
router.register(r'ContentFile', ContentFileView)
router.register(r'ContentImage', ContentImageView)
router.register(r'ContentVideo', ContentVideoView)


urlpatterns = [
    path('PageModel/', PageView.as_view(), name='page_list_create'),
    path('PageModel/<int:lang_id>/', PageView.as_view(), name='page_detail'),
    path('', include(router.urls))
]