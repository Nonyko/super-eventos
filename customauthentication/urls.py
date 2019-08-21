from django.conf.urls import url, include
from . import views
from django.urls import path, re_path
app_name = 'autenticacao'
urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('thanks/', views.thanks, name='thanks')
]