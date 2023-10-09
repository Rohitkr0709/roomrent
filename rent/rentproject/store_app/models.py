from django.db import models
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=255, default='Your Default Value Here')
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=20)
    message = models.TextField()


    def __str__(self):
        return self.name


