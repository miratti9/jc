from django.contrib import admin
from .models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('MARKET_CD','STORE_CD','PRDT_NAME','PRICE_AMT','UPC_PLU_ID')
    list_filter = ('MARKET_CD','STORE_CD',)
admin.site.register(Product,ProductAdmin)