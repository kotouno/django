from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path(r'polls/', include('polls.urls')),
    path(r'admin/', admin.site.urls),
]
