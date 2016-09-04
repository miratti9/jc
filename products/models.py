from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
    MARKET_CD = models.CharField(max_length=10)
    STORE_CD = models.CharField(max_length=10)
    PRDT_ID = models.CharField(max_length=20)
    UPC_PLU_ID = models.CharField(max_length=20)
    PRICE_AMT = models.FloatField(null=True,blank=True)
    PC = models.IntegerField(blank=True)
    WEIGHT = models.FloatField(blank=True)
    ALLERGENS = models.TextField(blank=True)
    USE_YN = models.CharField(max_length=1,default='Y')
    DELETE_YN = models.CharField(max_length=1,default='N')
    INSERT_DATE = models.DateTimeField(auto_now_add=True)
    PRDT_NAME = models.CharField(max_length=255)
    SIZE_NAME = models.CharField(max_length=255)
    NOTE = models.CharField(max_length=255)
    PRDT_CATE_CD = models.CharField(max_length=50)
    INGREDIENTS = models.TextField(blank=True)
    SHELF_LIFE = models.IntegerField(default=0)
    LABEL_YN = models.CharField(max_length=1,default='Y')

    class Meta:
        db_table = 'v10_price_info'






