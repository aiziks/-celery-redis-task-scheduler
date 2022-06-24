# -celery-redis-task-scheduler   Python(Django)

1. Install app requirements packages using 'pip install -r requirements.txt'

2. Install redis server via 'https://github.com/tporadowski/redis/releases'

3. Make migrations using 'py manage.py makemigrations'

4. Migrate using 'py manage.py migrate'

5. Start django server 'py manage.py runserver'

6. Start redis server ;for windows(--pool=solo option) :'celery -A django_celery_project.celery worker --pool=solo -l info'

7. Start celery worker using 'celery -A django_celery_project beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler'

