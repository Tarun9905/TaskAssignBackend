from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100,unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=128)  # Use hashed password storage

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.CharField(max_length=50)
    status = models.CharField(max_length=50,default="TO DO",blank=True)
    assigned_user = models.CharField(max_length=100, default="NA",blank=True)

    def __str__(self):
        return self.title

