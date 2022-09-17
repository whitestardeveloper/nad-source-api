"""ws_source URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from source.views import GoogleLogin
# from source.views import google_token
from rest_framework_swagger.views import get_swagger_view
from source.views import AppleLogin

schema_view = get_swagger_view(title='NAD SOURCE API')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/docs', schema_view),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('allauth.urls')),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('auth/google', GoogleLogin.as_view(), name='google_login'),
    path('auth/apple', AppleLogin.as_view(), name='google_login'),
    # path('auth/google', google_token, name='google_login'),

    path('api/', include('source.urls')),

]
