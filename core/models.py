from django.db import models

class Dogovor(models.Model):
    text = models.TextField()
    fio_cilent = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    