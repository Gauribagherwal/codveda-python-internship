from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from accounts import views as account_views


urlpatterns = [
    path("admin/", admin.site.urls),

    path("register/", account_views.register, name="register"),

    path("logout/", account_views.user_logout, name="user_logout"),

    path("", RedirectView.as_view(
        url="/dashboard/",
        permanent=False
    )),

    path("", include("django.contrib.auth.urls")),

    path("", include("tasks.urls")),
]