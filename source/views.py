from django.http import HttpResponse
from .models import Category, Material, Product
from .serializers import CategoryListSerializer, MaterialListSerializer, ProductListSerializer, ProductDetailSerializer
import requests
import os
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics,generics,filters
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist
from django_filters.rest_framework import DjangoFilterBackend


def index(request):
    return HttpResponse("Testing one sources")

@method_decorator(csrf_exempt, name='dispatch')
class CategoriesViewSet(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ['name',]
    filterset_fields = ['parent_id','name','is_leaf','level']

    def get(self, request, *args, **kwargs):
        root_nodes = Category.objects.all().get_cached_trees()
        data = []
        for n in root_nodes:
            data.append(self.recursive_node_to_dict(n))

        return Response(data)

    def recursive_node_to_dict(self, node):
        result = self.get_serializer(instance=node).data
        children = [self.recursive_node_to_dict(c) for c in node.get_children()]
        result['is_leaf'] = True
        result['product_count'] = 0
        queryset = Product.objects.filter(category_id=result['id'])
        result['product_count'] = queryset.count()

        if children:
            result['children'] = children
            result['is_leaf'] = False
            for category in children:
                result['product_count'] += category['product_count']
        return result

    def has_parent_question(self, parent_id):
        if parent_id:
            question_count = Product.objects.filter(category_id=parent_id).count()
            if (question_count > 0):
                return True


    def post(self, request, *args, **kwargs):
        parent_id = request.data.get('parent_id')

        if self.has_parent_question(parent_id):
            raise ValidationError({'detail': ('You can\'t add category because parent category include products')})

        if Category.objects.filter(pk=parent_id).exists() or parent_id == None:
            pass
        else:
            raise ValidationError({'detail': ('There is no category')})

        return self.create(request, *args, **kwargs)


@ method_decorator(csrf_exempt, name='dispatch')
class CategoryDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        if "id" in kwargs:
            try:
                category = Category.objects.get(id=kwargs["id"])
                is_child = Category.objects.get(id=kwargs["id"]).is_leaf_node()
                queryset = Product.objects.filter(category_id=category.id)

                if queryset.count() > 0:
                    raise ValidationError({'detail': ('It cannot be deleted because there is question belonging to the category.')})
                if is_child == False:
                    raise ValidationError({'detail': ('Cannot be deleted because it is subcategory.')})

                category.delete()
                return HttpResponse(status=204)

            except ObjectDoesNotExist:
                raise ValidationError({'detail': ('Not found.')})

        return self.destroy(request, *args, **kwargs)


# @ method_decorator(csrf_exempt, name='dispatch')
# class CategoryDetailAll(generics.RetrieveAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategoryAllSerializer
#     lookup_field = 'id'


################
@ method_decorator(csrf_exempt, name='dispatch')
class MaterialsViewSet(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialListSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ['name',]

################
@ method_decorator(csrf_exempt, name='dispatch')
class ProductViewSet(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ['name',]
    filterset_fields = ['category_id',]


################
@method_decorator(csrf_exempt, name='dispatch')
class ProductDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'id'
    # filterset_fields = ['category_id',]