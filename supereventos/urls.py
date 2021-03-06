"""supereventos URL Configuration

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
from django.urls import path, re_path, include
from core.views import home, eventos, evento, criarevento, editarevento
#autenticacao

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('accounts/', include('customauthentication.urls', namespace='autenticacao')),
    path('eventos/', eventos, name="eventos"),
    re_path('evento/(?P<id>\d+)/$',
                        evento, name='evento'),
    path('eventos/criar', criarevento, name="criarevento"),
    re_path('eventos/editar/(?P<id>\d+)/$', editarevento, name="editarevento"),

]
