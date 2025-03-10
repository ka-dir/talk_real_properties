
from django.contrib import admin
from django.urls import path, include
# for images to seen from user uploaded content
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('users/', include('users.urls')),
]
# set url for images uploaded
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
