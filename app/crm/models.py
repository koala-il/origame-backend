from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=150, blank=False, null=False)
