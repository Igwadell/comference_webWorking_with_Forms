from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static  import static

urlpatterns = [
    path('events/', include('events.urls')),
    path('speakers', include('speakers.urls')),
    path('admin/', admin.site.urls),
    # Add more URL patterns for other queries
] + static(settings.MEDIA_URL,  document_root= settings.MEDIA_ROOT)
