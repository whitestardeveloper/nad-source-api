from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from mptt.models import MPTTModel, TreeForeignKey
from django_cleanup import cleanup

# from cloudinary.models import CloudinaryField


@cleanup.ignore
class Category(MPTTModel):
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    priority = models.SmallIntegerField(default=1)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to='categories', null=True, blank=True)
    # image = CloudinaryField("Image",overwrite=True,resource_type="image",transformation={"quality": "auto:eco"})

    def __str__(self):     
        # return self.name                      
        full_path = [self.name]                  
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])

    class MPTTMeta:
        order_insertion_by=['priority']

    class Meta: 
        verbose_name=('Kategori')
        verbose_name_plural=('Kategoriler')
        db_table='categories'
        ordering=['created_at']
        unique_together=('slug', 'parent')   


class Material(models.Model):
    name = models.CharField(max_length=2500)
    description = models.TextField(null=True,blank=True)
    cas_no =  models.CharField(max_length=200, null=True, blank=True)
    ec_no =  models.CharField(max_length=200, null=True, blank=True)
    europa_eu_id = models.CharField(max_length=200, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # inhaleIndex = models.IntegerField(default=1)
    # swallowIndex = models.IntegerField(default=1)
    # contactIndex = models.IntegerField(default=1)
    # environmentIndex = models.IntegerField(default=1)
    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('cas_no', 'europa_eu_id')   
        verbose_name = ('Mataryel')
        verbose_name_plural=('Materyeller')


PRODUCT_ROZETS = (('PESTICIDES_FREE', 'Tarım ilacı içermez'),
                 ('TRANS_OIL_FREE', 'Trans yağ içermez'),
                 ('GLUTEN_FREE', 'Gluten içermez'),
                 ('NON_TOXIC', 'Toksik değildir'),
                 ('PARABEN_FREE', 'Paraben içermez'))        

@cleanup.ignore
class Product(models.Model):
    category = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE,  related_name='products')
    name = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Material, blank=True, through='ProductMaterial',related_name='ingredients')
    description = models.TextField(null=True,blank=True)
    priority = models.SmallIntegerField(default=1)
    altarnative_products = models.ManyToManyField("self", blank=True, through='AltarnativeProduct', symmetrical=True)
    rozets = MultiSelectField(choices=PRODUCT_ROZETS, max_choices=5, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products', null=True, blank=True)
    favorite = models.ManyToManyField(User, related_name='favorite', null=True, blank=True)


    def __str__(self):
        return self.name

    class Meta: 
        verbose_name=('Ürün')
        verbose_name_plural=('Ürünler')
        ordering=['priority','created_at']


class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    priority = models.SmallIntegerField(default=1)
    class Meta: 
        unique_together = ('product', 'material')
        ordering=('priority',)

class AltarnativeProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = 'product')
    altarnative_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = 'altarnative_product')
    priority = models.SmallIntegerField(default=1)
    class Meta: 
        unique_together = ('product', 'altarnative_product')
        ordering=['priority']


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=2000, null=True, blank=True)
    rating = models.SmallIntegerField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.username

# class ProductCategory(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     priority = models.SmallIntegerField(default=1)

#     class Meta(object):
#         unique_together = ('product', 'category')
