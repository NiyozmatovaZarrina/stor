"""from django.urls import path
from .views import CategoryList, CategoryDetail

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
]"""

"""
URL configuration for store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import include


urlpatterns = [
        #path('api/v1/', include('categorys.urls')),
        ]


"""urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('categorys.urls')),
    path('api/v1/profile/', include('users.api.urls')),
    path('api/v1/prihod/', include('prihod.urls')),
    path('api/v1/produkt/', include('produkt.urls')),
    path('api/v1/agent/', include('agent.urls')),
    
    
]
"""
