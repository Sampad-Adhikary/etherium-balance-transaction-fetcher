"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# from django import views
from django.contrib import admin
from django.urls import path
from myapp.views import home
from myapp.views import fetch_ethereum
from myapp.views import result
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('', home, name='home'),
    path('', fetch_ethereum, name='fetch_ethereum'),
    path('fetch-ethereum/', fetch_ethereum, name='fetch_ethereum'),
    path('result/', result, name='result'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)