from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products',on_delete=models.CASCADE)
    title = models.CharField(max_length=200, db_index=True)
    arthur = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=False)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    available = models.BooleanField(default=True)
    inventory = models.IntegerField(null=True,blank=True)
    featureproduct = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title
    
    def catagory(self):
        return self.category.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])