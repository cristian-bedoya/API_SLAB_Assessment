from django.db import models

# Create your models here.
class UserApp(models.Model):
    id_user = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

class Project(models.Model):
    id_project = models.AutoField(primary_key=True)
    name_project = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField(null=True)
    status_project = models.CharField(max_length= 20, default='En proceso', blank=True)

class Task(models.Model):
    id_task = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, null=True )
    finish_date = models.DateTimeField(null=True)
    status_project = models.CharField(max_length= 20, default='En proceso', blank=True)
