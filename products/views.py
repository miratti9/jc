from django.shortcuts import render
from django.conf import settings
from .models import Product

import xlrd
# Create your views here.
def import_excel(request):
    workbook = xlrd.open_workbook(settings.MEDIA_ROOT+'/great.xlsx')
    worksheet = workbook.sheet_by_index(0)
    num_rows = worksheet.nrows - 1
    curr_row = 1
    #test
    #test 9999
    while curr_row < num_rows:
        curr_row += 1
        row = worksheet.row(curr_row)
        print 'Row:', curr_row

        MARKET_CD = 'GREAT'
        STORE_CD =  'C00000103'
        PRDT_ID = int(worksheet.cell_value(curr_row, 0))
        upc = str(int(worksheet.cell_value(curr_row, 3)))
        UPC_PLU_ID = upc
        PRICE_AMT =  worksheet.cell_value(curr_row, 7)
        PC = worksheet.cell_value(curr_row, 8)
        weight = worksheet.cell_value(curr_row, 9)
        WEIGHT =  weight[:-2]
        ALLERGENS = worksheet.cell_value(curr_row, 14)

        PRDT_NAME = worksheet.cell_value(curr_row, 4)
        SIZE_NAME = worksheet.cell_value(curr_row, 5)
        NOTE = worksheet.cell_value(curr_row, 15)
        PRDT_CATE_CD =worksheet.cell_value(curr_row, 2)
        INGREDIENTS = worksheet.cell_value(curr_row, 13)
        shelf = worksheet.cell_value(curr_row, 10)
        SHELF_LIFE = shelf[:-4]

        product = Product(MARKET_CD=MARKET_CD,STORE_CD = STORE_CD, PRDT_ID = PRDT_ID, UPC_PLU_ID = UPC_PLU_ID,PRICE_AMT= PRICE_AMT, PC = PC, WEIGHT = WEIGHT, ALLERGENS = ALLERGENS, PRDT_NAME = PRDT_NAME, SIZE_NAME = SIZE_NAME,
                          NOTE = NOTE, PRDT_CATE_CD = PRDT_CATE_CD,INGREDIENTS=INGREDIENTS,SHELF_LIFE=SHELF_LIFE)
        product.save()