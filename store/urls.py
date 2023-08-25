from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import include


urlpatterns = [
    path('admin/' , admin.site.urls),
    path('', include("categorys.urls")),
    path('', include("agent.urls")),
    path('', include("prihoddetails.urls")),
    path('', include("prihods.urls")),
    path('', include("prodaja.urls")),
    path('', include("prodajadetails.urls")),
    path('', include("produkts.urls")),
    path('', include("storage.urls")),
     path('', include("users.urls")),
    
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
if (settings.DEBUG):
    from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
    urlpatterns += [        
        path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
        # Optional UI:
        path('api/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
        path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    ]
