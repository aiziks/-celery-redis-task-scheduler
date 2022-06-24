from django.conf import settings
from django.contrib.auth import get_user_model

from celery import shared_task
from django.core.mail import send_mail
from django_celery_project import settings
from django.utils import timezone
from datetime import timedelta


@shared_task(bind=True)
def send_mail_func(self):
    
    for i in range(10):
        print('I am sending mail')
    users = get_user_model().objects.all()
    # timezone.localtime(users.date_time) + timedelta(days=2)
    for user in users:
        mail_subject = "Hi! Celery Testing"
        message = "If you like my video please click the like button"
        to_email = "isaacadedayo1@gmail.com"
        send_mail(
            subject=mail_subject , message=message , from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        
        )



    return "Done"

@shared_task(bind=True)
def add(self , a,b):
    # operations
    print(a+b)
    return "Done"


