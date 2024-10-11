from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

class Employee (models.Model):
    shopid = models.ForeignKey('shop.Shop', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    privilege = models.ForeignKey('privileges.Privilege', on_delete=models.SET_NULL, null=True, related_name='employees')
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Check if the password is already hashed   
        if not self.password.startswith('pbkdf2_'): 
            self.password = make_password(self.password)
        super(Employee, self).save(*args, **kwargs)
