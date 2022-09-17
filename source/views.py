from django.http import HttpResponse
from .models import Category, Material, Product
from .serializers import CategoryListSerializer, MaterialListSerializer, ProductListSerializer, ProductDetailSerializer
import requests
from django.shortcuts import get_object_or_404
from django.core import serializers
import os
from rest_framework.exceptions import ValidationError
from rest_framework.exceptions import APIException
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics,generics,filters
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist
from django_filters.rest_framework import DjangoFilterBackend
# from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
# from allauth.socialaccount.providers.oauth2.client import OAuth2Client
# from dj_rest_auth.registration.views import SocialLoginView

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from rest_framework.utils import json
from rest_framework.views import APIView
import requests
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User


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
    filterset_fields = ['parent_id','name','level']

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


#######################
@method_decorator(csrf_exempt, name='dispatch')
def product_favorite(request, id):
    product = Product.objects.get(pk=id)
    if request.user.id is None:
        result = { 'message': 'User not found.' }
        response = HttpResponse(json.dumps(result), content_type='application/json')
        response.status_code = 400
        return response
    else:
        result = {}
        if product.favorite.filter(id=request.user.id).exists():
            product.favorite.remove(request.user)
            result = { 'state': 'Removed Favorite' } 
        else:
            product.favorite.add(request.user)
            result = { 'state': 'Added Favorite' } 
        response = HttpResponse(json.dumps(result), content_type='application/json')
        response.status_code = 201
        return response


@method_decorator(csrf_exempt, name='dispatch')
def favorite_product_list(request):
    if request.user.id is None:
        result = { 'message': 'User not found.' }
        response = HttpResponse(json.dumps(result), content_type='application/json')
        response.status_code = 400
        return response
    else:
        user = request.user
        favorite_products = serializers.serialize('json',user.favorite.all())
        # data = []
        # for n in favorite_products:
        #     data.append(n.fields)
        #     print(json.dumps(n))
        response = HttpResponse(favorite_products, content_type='application/json')
        response.status_code = 201
        return response


    # product = Product.objects.get(pk=id)
    # print(product)
    # print(request.user)
    # if request.user.id is None:
    #     result = { 'message': 'User not found.' }
    #     response = HttpResponse(json.dumps(result), content_type='application/json')
    #     response.status_code = 400
    #     return response
    # else:
    #     result = {}
    #     if product.favorite.filter(id=request.user.id).exists():
    #         product.favorite.remove(request.user)
    #         result = { 'state': 'Removed Favorite' } 
    #     else:
    #         product.favorite.add(request.user)
    #         result = { 'state': 'Added Favorite' } 
    #     response = HttpResponse(json.dumps(result), content_type='application/json')
    #     response.status_code = 201
    #     return response


################
@method_decorator(csrf_exempt, name='dispatch')
class ProductDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'id'
    # filterset_fields = ['category_id',]

###############
# class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
#     adapter_class = GoogleOAuth2Adapter
#     callback_url = "http://localhost:8000" ###CALLBACK_URL_YOU_SET_ON_GOOGLE
#     client_class = OAuth2Client

# class GoogleLogin(SocialLoginView): # if you want to use Implicit Grant, use this
#     adapter_class = GoogleOAuth2Adapter
#     def post(self, request, *args, **kwargs):
#             response = super(GoogleLogin, self).post(request, *args, **kwargs)
#             token = Token.objects.get(key=response.data['key'])
#             return Response({'token': token.key, 'id': token.user_id})

# class GoogleLogin(SocialLoginView):
#     adapter_class = GoogleOAuth2Adapter



class GoogleLogin(APIView):
    def post(self, request):
        payload = {'access_token': request.data.get("token")}  # validate the token
        r = requests.get('https://www.googleapis.com/oauth2/v2/userinfo', params=payload)
        data = json.loads(r.text)

        if 'error' in data:
            content = {'message': 'wrong google token / this google token is already expired.'}
            return Response(content)

        # create user if not exist
        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            user = User()
            user.username = data['email']
            # provider random default password
            user.password = make_password(BaseUserManager().make_random_password())
            user.email = data['email']
            user.save()

        token = RefreshToken.for_user(user)  # generate token without username & password
        response = {}
        response['user_name'] = user.username
        response['user_last_name'] = user.last_name
        response['user_e_mail'] = user.email
        response['access_token'] = str(token.access_token)
        response['refresh_token'] = str(token)
        return Response(response)


class AppleLogin(APIView):
    def post(self, request):
        payload = {'access_token': request.data.get("token")}  # validate the token
        r = requests.get('https://appleid.apple.com/auth/token', params=payload)
        data = json.loads(r.text)

        if 'error' in data:
            content = {'message': 'wrong google token / this google token is already expired.'}
            return Response(content)

        # create user if not exist
        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            user = User()
            user.username = data['email']
            # provider random default password
            user.password = make_password(BaseUserManager().make_random_password())
            user.email = data['email']
            user.save()

        token = RefreshToken.for_user(user)  # generate token without username & password
        response = {}
        response['user_name'] = user.username
        response['user_last_name'] = user.last_name
        response['user_e_mail'] = user.email
        # response['token_exp'] = str(token.exp)
        response['access_token'] = str(token.access_token)
        response['refresh_token'] = str(token)
        return Response(response)