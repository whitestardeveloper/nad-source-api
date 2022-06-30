from django.contrib import admin
from .models import Category, Material, Product, ProductMaterial, AltarnativeProduct
from django.contrib.admin.widgets import (
    AutocompleteSelect, AutocompleteSelectMultiple
)
from django.forms import widgets

# from dal import autocomplete
# from django import forms


# admin.site.register(Category)
# admin.site.register(Material)
# admin.site.register(Product)

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    search_fields = ['name',]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class ProductMaterialInline(admin.TabularInline):
    # search_fields = ("material_name", )
    model = Product.ingredients.through
    autocomplete_fields =['material',]
    extra = 0


class AltarnativeProductInline(admin.TabularInline):
    model = AltarnativeProduct
    autocomplete_fields =['product',]
    extra = 0
    fk_name = 'altarnative_product'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # search_fields = ("id", )
    # autocomplete_fields = ('ingredients',)
    search_fields = ['material','product',]
    filter_horizontal = ('ingredients', 'altarnative_products')
    inlines = (ProductMaterialInline, AltarnativeProductInline)

# Register your models here.
