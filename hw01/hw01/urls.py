from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('amin/', admin.site.urls),
    path('', include('hw01app.urls')),
]
