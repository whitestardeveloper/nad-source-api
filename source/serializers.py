from dataclasses import fields
from itertools import product
from rest_framework import serializers
from .models import Category, Material, Product, AltarnativeProduct, ProductMaterial

class MaterialListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields= '__all__'

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields= ['id', 'name','description', 'category_id', 'image','priority']



class ProductMaterialListSerializer(serializers.ModelSerializer):
    # product = ProductListSerializer(read_only=True)
    # material = MaterialListSerializer(read_only=True)
    class Meta:
        model = ProductMaterial
        fields= '__all__'

# class AltarnativeProductListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AltarnativeProduct
#         fields= '__all__'

class ProductDetailSerializer(serializers.ModelSerializer):
    # ingredients = serializers.SerializerMethodField()
    # def get_ingredients(self, obj):
    #     ingredientList = []
        
    #     for intredient in obj.ingredients.all().order_by('ingredients__priority'):
    #         # print(intredient)
    #         details = {}
    #         # material = Material.objects.get(id=intredient.id)
    #         # material_serializer = ProductMaterialListSerializer(material)
    #         # print(material_serializer.data)
    #         details['id'] = intredient.id
    #         details['name'] = intredient.name
    #         details['description'] = intredient.name
    #         # details['priotity'] = ProductMaterial.objects.get(material = intredient)
    #         # cs_details = ComponentSupplier.objects.get(supplier=supplier, component=obj)
    #         # details['priority'] = intredient.priority
    #         # details['currency'] = cs_details.currency
    #         # details['included_donation_amount'] = cs_details.members_price - cs_details.bought_at
    #         ingredientList.append(details)

    #     return ingredientList

    ingredients = MaterialListSerializer(read_only=True, many=True)
    altarnative_products = ProductListSerializer(read_only=True, many=True)
    # altarnative_products = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields= ['id','name', 'description', 'image','category_id','created_at','updated_at','rozets','ingredients','altarnative_products']
        depth = 1


class CategoryListSerializer(serializers.ModelSerializer):
    # product_count = Category.objects.all().annotate(product_count=Product('category'))
    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'parent_id','priority']
        depth = 1

# class CategoryAllSerializer(CategorySerializer):
#     class Meta:
#         model = Category
#         fields = ['id', 'name', 'parent_id', 'priority', 'image', 'children']
#         depth = 1
