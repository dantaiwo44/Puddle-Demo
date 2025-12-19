
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

 


urlpatterns = [
    path('', include(('core.urls', 'core'), namespace='core')),
    path('items/', include(('items.urls', 'items'), namespace='items')),
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('inbox/', include('conversation.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
