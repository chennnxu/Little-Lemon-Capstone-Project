from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    # path('about/', views.about, name="about"),
    # path('book/', views.book, name="book"),
    # path('reservations/', views.reservations, name="reservations"),
    path("menu/", views.MenuItemView.as_view()),
    path("menu/<int:pk>/", views.SingleMenuItemView.as_view()),
    # path('bookings', views.bookings, name='bookings'),
]
