"""project6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', diary_main, name='diary_main'),
    path('diary/', diary_list, name='diary_list'),
    path('diary/<int:pk>/', diary_detail, name='diary_detail'),
    path('diary/create/', diary_create, name='diary_create'),
    path('diary/<int:pk>/update', diary_update, name='diary_update'),
    path('diary/<int:pk>/delete', diary_delete, name='diary_delete'),
]
