from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(User):
    jid = models.EmailField(verbose_name='Jabber')
    skype_id = models.CharField(max_length=50, verbose_name='Skype')
    birthday = models.DateField(verbose_name='Date of birth')
    bio = models.TextField(verbose_name='Bio')
    other = models.TextField(verbose_name='Other contacts')


class Request(models.Model):
    data = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-datetime']
