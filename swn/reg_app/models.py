from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import re

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        users = User.objects.all()
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First name must be at least two characters.'
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last name must be at least two characters.'  
        if len(postData['password']) < 8:
            errors['password_length'] = 'Password must be at least 8 characters.'
        if postData['password'] != postData['pw_confirm']:
            errors['password_mismatch'] = 'Password and Confirm Password do not match.'
        # if datetime.strptime(postData['birthdate'], "%Y-%m-%d")  > datetime.now():
            # errors['birthdate'] = 'Birth date cannot be a future date.'
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        if not email_regex.match(postData['email']):
            errors['email'] = 'Invalid email address format.'
        for user in users:
            if postData['email'] == user.email:
                errors['uniqueemail'] = 'This email is already registered.'
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=90)
    # birthdate = models.DateTimeField()
    objects = UserManager()