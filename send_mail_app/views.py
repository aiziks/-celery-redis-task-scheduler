from django.http import HttpResponse
from send_mail_app.tasks import send_mail_func
import json

def send_mail_to_all(request):
    send_mail_func.delay()

    return HttpResponse('Mail Sent')


