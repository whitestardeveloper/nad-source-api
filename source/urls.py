from django.urls import path
from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView, TokenVerifyView )

from . import views

urlpatterns = [
    path('test', views.index, name='index'),
    path('categories', views.CategoriesViewSet.as_view()),
    path('categories/<str:id>', views.CategoryDetailViewSet.as_view()),
    path('products', views.ProductViewSet.as_view()),
    path('products/<str:id>', views.ProductDetailViewSet.as_view()),
    path('materials', views.MaterialsViewSet.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
