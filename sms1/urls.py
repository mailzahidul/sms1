"""sms1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.homefolder, name='homefolder')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='homefolder')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings  # new
from django.conf.urls.static import static  # new
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('result/', include('result.urls')),
    path('student/', include('student.urls')),
    path('teachers/', include('teachers.urls')),
    path('', views.home, name="home"),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
