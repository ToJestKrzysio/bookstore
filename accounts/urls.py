from django.urls import path, include

from accounts import views

urlpatterns = [
    path("logout/", views.logout, name='logout'),
    path('', include("django.contrib.auth.urls")),
]
