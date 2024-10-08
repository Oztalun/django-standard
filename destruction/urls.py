from django.contrib import admin
from django.urls import path, include
from articles import views
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("articles/", include("articles.urls")),
    path("users/", include("users.urls")),
    path("accounts/", include("accounts.urls")),
    path("", lambda request : redirect("articles:articles")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)