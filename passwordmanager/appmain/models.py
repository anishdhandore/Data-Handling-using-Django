from django.db import models

# Create your models here.
class Password(models.Model):
    account = models.CharField(max_length = 100, null=True)
    username = models.CharField(max_length = 100, default="anonymous")
    password = models.CharField(max_length = 100)

    def __str__(self):
        return self.username