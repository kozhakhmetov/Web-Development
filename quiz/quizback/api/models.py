from django.db import models


from django.contrib.auth.models import User
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=100, default='')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return "NAME:" + str(self.name)