from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    # path("", views.articles, name="articles"),
    # path("index/", views.profile, name="index"),
    path("hello/", views.hello, name="hello"),
    path("data_throw/", views.data_throw, name="data-throw"),
    path("data_catch/", views.data_catch, name="data-catch"),
]