from django.urls import path

from . import views

urlpatterns = [
    path('test', views.index, name='index'),
    path('categories', views.CategoriesViewSet.as_view()),
    path('categories/<str:id>', views.CategoryDetailViewSet.as_view()),
    path('products', views.ProductViewSet.as_view()),
    path('products/<str:id>', views.ProductDetailViewSet.as_view()),
    path('materials', views.MaterialsViewSet.as_view()),

]
