from app.views import index, user, generate_vcard
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('<str:client_nickname>', user, name='user'),
    path('<str:client_nickname>/vcard', generate_vcard, name='vcard')
]

