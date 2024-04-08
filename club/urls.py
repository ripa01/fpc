from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import *

urlpatterns =  [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('about/', about_view, name='about'),
    path('news/', NewsListView.as_view(), name='news'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_details'),
    path('news/new/', NewsCreateView.as_view(), name='news_create'),
    
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
