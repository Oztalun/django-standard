# from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Article

def articles(request):
    context = {"articles":Article.objects.all().order_by("-created_at")}
    return render(request, "articles/articles.html", context)
# '{{article.title}}'
# <a href="{% url 'articles:data-throw' %}">
def new(request):
    return render(request, "articles/new.html")

def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    Article.objects.create(title=title, content=content)
    return render(request, "articles/create.html")

def index(request):
    return render(request, "articles/index.html")

# 지우랬는데 안지울거임
def hello(request):
    name = "희경"
    tags = ["python", "django", "html", "css"]
    books = ["해변의 카프카", "코스모스", "백설공주","어린왕자"]
    context = {
		"name":name,
		"tags":tags,
		"books":books,
	}
    return render(request, "articles/hello.html", context)


def data_throw(request):
    return render(request, "articles/data_throw.html")


def data_catch(request):
    message = request.GET.get("message")
    context = {"data": message, }
    return render(request, "articles/data_catch.html", context)

