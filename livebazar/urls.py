from django.urls import path
from .views import home, support, register_seller, login, seller_dashboard

urlpatterns = [
    path("home/", home, name="home"),
    path("support/", support , name="support"),
    path("register_seller/", register_seller, name="register_seller" ),
    path("login/", login, name="login"),
    path("seller_dashboard/", seller_dashboard, name="seller_dashboard" )
]
