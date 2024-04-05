from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import *

urlpatterns =  [
    path('', home_view, name='home'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
