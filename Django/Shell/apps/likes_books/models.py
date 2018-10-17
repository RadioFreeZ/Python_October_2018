from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField()
    create_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return f'\nID = {self.id}, NAME = {self.first_name}, EMAIL = {self.email}'

class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=1000)
    liked_users = models.ManyToManyField(User, related_name="liked_books")
    uploader = models.ForeignKey(User,related_name = "uploaded_books")
    create_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return f'\nID = {self.id}, NAME = {self.name} UPLOADER = {self.uploader.first_name}'
