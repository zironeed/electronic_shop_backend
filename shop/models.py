from django.db import models
from django.db.models import Q

NULLABLE = {'null': True, 'blank': True}


class Types(models.TextChoices):
    factory = 'Factory'
    retail = 'Retail'
    individual = 'Individual'


class Seller(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Seller name')
    type = models.CharField(choices=Types.choices, verbose_name='Seller type')
    provider = models.ForeignKey('self', on_delete=models.CASCADE,
                                 limit_choices_to=~Q(type=Types.factory), verbose_name='Seller provider', **NULLABLE)
    credit = models.DecimalField(default=0, decimal_places=2, verbose_name='Seller credit')
    creation_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Seller"
        verbose_name_plural = "Sellers"

    def __str__(self):
        return self.name


class Contact(models.Model):
    email = models.EmailField()