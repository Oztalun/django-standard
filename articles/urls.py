from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path("", views.articles, name="articles"),
    path("new/", views.new, name="new"),
    path("create/", views.create, name="create"),
    path("hello/", views.hello, name="hello"),# 지우랬는데 안지울거임
    path("data_throw/", views.data_throw, name="data-throw"),
    path("data_catch/", views.data_catch, name="data-catch"),
]