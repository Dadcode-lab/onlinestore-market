from django.urls import path

from . import views

app_name = 'conversation'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('<int:pk>/', views.detail, name='detail'), 
    path('new/<int:item_pk>/', views.new_conversation, name='new'),
    path('conversation/', views.make_phone_call, name='make_call'),
    path('conversation/', views.voice_response, name='voice_response')
]