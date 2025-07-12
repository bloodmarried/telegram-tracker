from django.db import models
from django.contrib.auth.models import User
# Create your models here.
    

class Reviews(models.Model):
    user_id = models.IntegerField(unique = True)
    picture = models.CharField()
    viewers = models.IntegerField(default = 0)
    reputation = models.IntegerField(default = 0)
    date = models.DateTimeField()
    username = models.OneToOneField(User, on_delete=models.CASCADE, to_field="username")
    
    def __str__(self):
        return str(self.viewers)