"""todoList URL Configuration

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
from list import views
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('doc/', get_schema_view(
        title="ToDo-List Challenge",
        description="Api challenge Invera"
    ), name='doc'),
    path('todoList/', views.list_todo, name="home"), 
    path('deleteTodoList/<int:lista_id>/', views.lista_delete, name="delete"), 
    path('updateTodoList/<int:lista_id>/', views.update_lista, name="update"),
    path('updateStatus/<int:lista_id>/', views.status_completed, name="status"), 
    path('getByParameter/<str:date>/', views.filter_lista_by, name="parameter"), 
    path('getByParameter/<str:date>/<str:description>/', views.filter_lista_by, name="parameters"), 
]
