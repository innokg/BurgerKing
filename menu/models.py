from django.db import models


class Category(models.Model):
    slug = models.SlugField(primary_key=True)
    title = models.CharField(max_length=55, unique=True)
    image = models.ImageField(upload_to='category_images', null=True, blank=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    STATUS_CHOICES = (
        ('in stock', 'В наличии'),
        ('out of stock', 'Нет в наличии')
    )

    name = models.CharField(max_length=155)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images')
    kkal = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name

