"""Test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf.urls import url
from django.shortcuts import render
# 上传文件
from django.conf import settings
from django.conf.urls.static import static

def home(request):
    return render(request, 'home.html')
    
urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', home),
    url(r'^accounts/', include('users.urls', namespace="users")),
    url(r'^file/', include('file_upload.urls', namespace="file_upload")),
    url(r'^picture/', include('pic_upload.urls', namespace='pic_upload')),
    url(r'^requestdemo/', include('request_demo.urls', namespace='requestdemo')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # 给media文件夹里每个文件创建独立url资源

