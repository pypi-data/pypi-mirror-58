from enum import Enum

from django.db import models


class Institute(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Account(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.PROTECT)
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.name} ({self.institute.name})'


class Transaction(models.Model):
    class CURRENCY(Enum):
        dm = (0, 'DM')
        euro = (1, 'EUR')
        dollar = (2, 'USD')

        @classmethod
        def get_value(cls, member):
            return cls[member].value[0]

    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    date = models.DateField()
    amount = models.FloatField()
    currency = models.IntegerField(choices=[x.value for x in CURRENCY],
                                   default=CURRENCY.get_value('euro'))
    purpose = models.CharField(max_length=128, blank=True, default="")
