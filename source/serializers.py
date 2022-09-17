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

class AltarnativeProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AltarnativeProduct
        fields= '__all__'

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
    
    # altarnative_products = AltarnativeProductListSerializer(read_only=True, many=True)
    # ingredients = MaterialListSerializer(read_only=True, many=True)
    
    altarnative_products = serializers.SerializerMethodField(read_only=True)
    def get_altarnative_products(self, model):
        altarnativeProductList = []
        for item in model.altarnative_products.all().order_by('altarnative_product__priority'):
            details = {}
            details['id'] = item.id
            details['name'] = item.name
            details['description'] = item.description
            details['category_id'] = item.category_id
            if item.image:
                details['image'] = item.image.url
            else:
                details['image'] = None
            altarnativeProductList.append(details)

        return altarnativeProductList
        # def get_image(img):
        #     if(img):
        #         return img.url
        #     else:
        #         return None

        # data = [{'id':altarnative_products.id, 'name':altarnative_products.name, 'category_id': altarnative_products.category_id,'description': altarnative_products.description, 'image': get_image(altarnative_products.image) } for altarnative_products in model.altarnative_products.all().order_by('altarnative_products__priority')]
        # print(data)
        # return data

    ingredients = serializers.SerializerMethodField(read_only=True)
    def get_ingredients(self, model):
        data = [{'id':ingredients.id, 'name':ingredients.name, 'description': ingredients.description } for ingredients in model.ingredients.all().order_by('productmaterial__priority')]
        return data

    favorite = serializers.SerializerMethodField(read_only=True)
    def get_favorite(self, model):
        if self.context['request'].user.id is None:
            return False
        else:
            return model.favorite.filter(id=self.context['request'].user.id).exists()

    # altarnative_products = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields= ['id','name', 'description', 'image','category_id','created_at','updated_at','rozets', 'favorite','ingredients','altarnative_products']
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
