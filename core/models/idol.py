from django.db import models


class Idol(models.Model):
    name = models.CharField(unique=True, max_length=255, primary_key=True)
    display_name = models.CharField(max_length=255)