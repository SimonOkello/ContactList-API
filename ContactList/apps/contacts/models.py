from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=100)
    phone_number = PhoneNumberField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return str(self.first_name)
