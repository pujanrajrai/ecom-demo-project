from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('<str:username>', views.send_messages, name='send_message'),
]
