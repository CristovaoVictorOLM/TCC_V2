from django.db import models

# Create your models here.


class Login(models.Model):
    usuario = models.EmailField()


    def __str__(self):
        return self.usuario