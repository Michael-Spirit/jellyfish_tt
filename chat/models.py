from django.db import models

from django.contrib.auth.models import User


class Message(models.Model):
    user = models.ForeignKey(User)
    text = models.TextField()
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}" \
               f"{self.text}" \
               f"{self.time}"
