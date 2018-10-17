
from __future__ import unicode_literals
from django.db import models
from django.core.validators import validate_email
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 1:
            errors["first_name"] = "First name cannot be empty!"
        if len(postData['last_name']) < 1:
            errors["last_name"] = "Last name cannot be empty!"
        if len(postData['email']) < 1:
            errors["email"] = "Email cannot be empty!"
        try:
            validate_email(email)
        except validate_email.ValidationError:
            errors["email"] = "Email must be valid!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
