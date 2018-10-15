from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length = 255)
    state = models.CharField(max_length = 2)
    city = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'\nID = {self.id}, NAME = {self.name}, CITY = {self.city}, STATE = {self.state}'
class Ninja (models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    dojo = models.ForeignKey(Dojo,related_name = "ninjas")
    def __str__(self):
        return f'\nID = {self.id}, FIRST_NAME = {self.first_name}, LAST_NAME = {self.last_name}, DOJO = {self.dojo_id}'
