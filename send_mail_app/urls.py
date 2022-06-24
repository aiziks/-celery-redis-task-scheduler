
from django.contrib import admin
from django.urls import path
from .views import  send_mail_to_all 

urlpatterns = [
    path('sendmail/',  send_mail_to_all, name="sendmail" ),

]
