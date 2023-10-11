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
    provider = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Seller provider', **NULLABLE)
    credit = models.DecimalField(default=0, decimal_places=2, max_digits=100, verbose_name='Seller credit')
    creation_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Seller"
        verbose_name_plural = "Sellers"

    def __str__(self):
        return self.name


class Contact(models.Model):
    email = models.EmailField(max_length=50, unique=True, verbose_name='Contact email')
    country = models.CharField(max_length=100, verbose_name='Contact country', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='Contact city', **NULLABLE)
    street = models.CharField(max_length=100, verbose_name='Contact street', **NULLABLE)
    building = models.CharField(max_length=100, verbose_name='Contact building', **NULLABLE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, verbose_name='Seller contact', related_name='contacts')

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.email


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Product title')
    model = models.CharField(max_length=100, verbose_name='Product model')
    date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Product publish date')
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, verbose_name='Seller product',
                               related_name='product', **NULLABLE)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title
