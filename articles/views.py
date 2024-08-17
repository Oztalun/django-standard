from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "articles/index.html")

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

