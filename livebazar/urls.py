from django.urls import path
from .views import home, support

urlpatterns = [
    path("home/", home, name="home"),
    path("support/", support , name="support")
]
