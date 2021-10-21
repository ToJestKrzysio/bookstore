from django.shortcuts import render


def logout(request):
    return render(request, "accounts/logout.html")
