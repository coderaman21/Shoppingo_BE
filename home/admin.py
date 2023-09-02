from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name','total_products')
    search_fields = ('id','brand_name')
admin.site.register(Brand,BrandAdmin)
class ProductTagAdmin(admin.ModelAdmin):
    search_fields = ('tag',)
    list_display = ('tag',)
admin.site.register(ProductTag,ProductTagAdmin)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('sub_category','category')
    list_filter = ('category',)
    search_fields = ('category__id','category__category','id','sub_category')
admin.site.register(SubCategory,SubCategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','category','brand','sold_units')
    list_filter = ('category','brand','tags')
    autocomplete_fields = ('tags',)
    search_fields = ('id','name','category__id','category__sub_category','brand__brand_name')
admin.site.register(Product,ProductAdmin)