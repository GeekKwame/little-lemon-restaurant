from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from restaurant import views

router = DefaultRouter()
router.register(r'booking/tables', views.BookingViewSet, basename='booking')

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include('restaurant.urls')),
   path('restaurant/', include('restaurant.urls')),
   path('restaurant/', include(router.urls)),
   path('auth/', include('djoser.urls')),
   path('auth/', include('djoser.urls.authtoken')),
   path('api-token-auth/', obtain_auth_token),
]
