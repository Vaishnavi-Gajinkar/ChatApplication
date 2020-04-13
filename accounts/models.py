from django.db import models

# Create your models here.
class register(models.Model):
    username=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    password1=models.CharField(max_length=20)
    password2=models.CharField(max_length=20)

    def __str__(self):
        return self.username
