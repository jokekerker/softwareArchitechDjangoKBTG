from enum import Enum

from django.db import models
from django_enum_choices.fields import EnumChoiceField


# Create your models here.
class LoanProfile(models.Model):
    STATUS_PROFILE = (
        ('wait', 'Waiting'),
        ('approve', 'Approved'),
        ('reject', 'Rejected'),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    scroll = models.IntegerField()
    amount_request = models.BigIntegerField()
    amount_approve = models.BigIntegerField()
    date_create = models.DateTimeField('date create')
    status = models.CharField(
        max_length=50,
        choices=STATUS_PROFILE
    )
