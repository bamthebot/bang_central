from django.db import models
from django.contrib.auth.models import User


class TwitchUser(models.Model):
    twitch_id = models.IntegerField()
    twitch_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=500)

    access_token = models.CharField(max_length=200)
    refresh_token = models.CharField(max_length=200)
    expiration_date = models.DateField()
    scope = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.twitch_name


class Bang(models.Model):
    command = models.CharField(max_length=500)
    response = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.command

    def clean(self):
        if "!" in self.command[0]:
            self.response = self.response[1:]
