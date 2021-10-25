from django.urls import path, include

from accounts import views

app_name = "accounts"
urlpatterns = [
    path("redirect/", views.LogoutRedirect.as_view(), name='redirect'),
    path('', include("django.contrib.auth.urls")),
]
