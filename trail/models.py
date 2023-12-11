from django.db import models

#create table Employee(col1 dt,col2 dt)


class Employee(models.Model):
    ename = models.CharField(max_length=255)
    esal = models.IntegerField()
    eaddr = models.CharField(max_length=255)


'''
python manage.py makemigrations
python manage.py migrate
'''