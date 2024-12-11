from django.urls import path
from . import views
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    # path('', views.home, name="home"),
    path('api-token-auth', ObtainAuthToken.as_view()),
    path('', views.index, name='index'),
    path('add_menu_item', views.menu_item_form_view, name="menu_item_form_view"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('bookings/', views.BookingViewClass.as_view(), name="bookings"),
    path('reservations/', views.reservations, name="reservations"),    
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]
