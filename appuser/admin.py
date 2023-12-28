from django.contrib import admin
from django.db.models.aggregates import Count
from . import models
# Register your models here.




@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email','date_of_birth','phone','address']
    list_select_related = ['address']
    ordering = ['user__first_name','user__last_name']
    autocomplete_fields = ['user']
    list_select_related = ['user']
    search_fields = ['first_name__istartswith','last_name__istartswith']
    list_per_page = 50

    # @admin.display(ordering='order_count')
    # def orders(self,customer):
    #     url = (
    #         reverse('admin:base_order_changelist')
    #         +'?'
    #         +urlencode({
    #             'customer_id': str(customer.id)
    #         })
    #     )
    #     return format_html('<a href="{}">{}</a>',url,customer.order_count)

    # def get_queryset(self, request):
    #     return super().get_queryset(request).annotate(order_count = Count('order'))
    



@admin.register(models.Address)
class AdressAdmin(admin.ModelAdmin):
    list_display = ['customer','street','city','country']
    autocomplete_fields = ['customer']
