from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    image = models.ImageField(upload_to='media/categories', null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return str(self.name)

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    price = models.FloatField(default=0.0, verbose_name='Price')
    categories = models.ManyToManyField(Category, verbose_name='Categories')
    is_active = models.BooleanField(verbose_name='Active?', default=False)
    image = models.ImageField(upload_to='media/products', null=True, blank=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return str(self.name)