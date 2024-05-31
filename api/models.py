from django.db import models


# Create your models here.
class Employee (models.Model):

    name = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    lastname = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )

    service_time = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

    remuneration = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False
    )

    object = models.Manager()

