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
    path('news/<int:pk>/update/', NewsUpdateView.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),


    path('notice/', NoticeListView.as_view(), name='notice'),
    path('notice/<int:pk>/', NoticeDetailView.as_view(), name='notice_details'),
    path('notice/notice/', NoticeCreateView.as_view(), name='notice_create'),
    path('notice/<int:pk>/update/', NoticeUpdateView.as_view(), name='notice_update'),
    path('notice/<int:pk>/delete/', NoticeDeleteView.as_view(), name='notice_delete'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
