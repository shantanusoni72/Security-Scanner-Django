from django.contrib import admin
from django.urls import path, include
from portscan import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.scanning,name='scanning')
]
