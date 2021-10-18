from django.urls import path

from bookstore import views

urlpatterns = [
    path("", views.home, name="home_page")
]
