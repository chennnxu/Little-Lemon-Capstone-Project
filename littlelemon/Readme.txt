urls.py (Project-level):
urlpatterns = [
    path("admin/", admin.site.urls),
    path("restaurant/", include("restaurant.urls")),
    path("restaurant/menu/", include("restaurant.urls")),
    path("restaurant/booking/", include(router.urls)),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]

urls.py (App-level):
urlpatterns = [
    path("", views.home, name="home"),
    path("menu/", views.MenuItemView.as_view()),
    path("menu/<int:pk>/", views.SingleMenuItemView.as_view()),
    path("message/", views.msg),
    path("api-token-auth/", obtain_auth_token),
]

Superuser:
username: admin
password: admin@123
token: 28ef4229c179b7d3a76dd4e647555bd65a7bf052