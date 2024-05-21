from django.urls import path
from . import views

urlpatterns = [
    path('', views.lesson_list, name='lesson_list'),
    path('upload/<int:id>/', views.upload_file, name='upload'),
    path('scores/<int:id>/', views.view_scores, name='scores'),
]