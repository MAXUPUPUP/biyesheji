from django.urls import path

from . import views

urlpatterns = [
    # path('code/', views.code, name='code'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('indexa/', views.indexa, name='indexa'),
    # path('logout/', views.logout, name='logout'),
]