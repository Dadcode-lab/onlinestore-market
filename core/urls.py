from django.urls import path

from . import views

app_name = 'core'

urlpatternss = [
    path('', views.index, name='index'),
]