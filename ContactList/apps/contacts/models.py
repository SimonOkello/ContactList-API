from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    country_code = models.CharField(max_length=6)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return str(self.first_name)
