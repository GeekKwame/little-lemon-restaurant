from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu_page, name='menu'),
    path('book/', views.booking_page, name='book'),
    # API endpoints
    path('menu/items/', views.MenuItemView.as_view(), name='menu-items'),
    path('menu/items/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu-item'),
]