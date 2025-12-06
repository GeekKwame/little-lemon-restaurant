from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant import views

router = DefaultRouter()
router.register(r'booking/tables', views.BookingViewSet, basename='booking')

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include('restaurant.urls')),
   path('restaurant/', include('restaurant.urls')),
   path('restaurant/', include(router.urls)),
]
