from django.urls import path
from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView, TokenVerifyView )

from . import views

urlpatterns = [
    path('test', views.index, name='index'),
    path('categories', views.CategoriesViewSet.as_view()),
    path('categories/<str:id>', views.CategoryDetailViewSet.as_view()),
    path('products', views.ProductViewSet.as_view()),
    path('products/<str:id>', views.ProductDetailViewSet.as_view()),
    path('favorite-products',  views.favorite_product_list, name='favorite_product_list'),
    path('products/<str:id>/favorite', views.product_favorite, name='product_favorite'),
    path('products/<str:id>/reviews', views.add_review, name='add_review_product'),
    path('products/<str:product_id>/reviews/<str:review_id>', views.edit_review, name='edit_review_product'),
    # path('addreview/<int:id>/',views.add_review,name="add_review"),
    # path('editreview/<int:product_id>/<int:review_id>',views.edit_review,name="edit_review"),
    # path('deletereview/<int:product_id>/<int:review_id>',views.delete_review,name="delete_review"),
    path('materials', views.MaterialsViewSet.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
