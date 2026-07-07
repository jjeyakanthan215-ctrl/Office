"""URL configuration for EscTrix project."""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Custom admin site configuration
admin.site.site_header = 'EscTrix Administration'
admin.site.site_title = 'EscTrix Admin'
admin.site.index_title = 'Dashboard'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
