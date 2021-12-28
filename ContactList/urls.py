from django.contrib import admin
from django.urls import path, include
from .utils.rounting import get_app_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include(get_app_urls('authentication'))),
    path('api/v1/', include(get_app_urls('contacts'))),
]
