from django.contrib import admin
from django.urls import path, include
from hostdiscovery import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.hostdiscovery,name='hostdiscovery')
]
