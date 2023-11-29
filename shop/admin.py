from django.contrib import admin
from .models import Category, Product

#register
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','arthur' ,'slug', 'price','featureproduct','rating','catagory', 'available','image', 'created']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 50