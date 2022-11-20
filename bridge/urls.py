from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('bridge_home.urls')),
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('photos/', include('photos.urls')),
    path('tasks/', include('base.urls') ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)