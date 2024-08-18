from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path("", views.articles, name="articles"),
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.article_detail, name="article_detail"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("index/", views.index, name="index"),
    path("<int:pk>/update/", views.update, name="update"),
    path("hello/", views.hello, name="hello"),# 지우랬는데 안지울거임
    path("data_throw/", views.data_throw, name="data-throw"),
    path("data_catch/", views.data_catch, name="data-catch"),
]