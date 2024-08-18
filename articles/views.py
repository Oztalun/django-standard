# from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


def articles(request):
    context = {"articles": Article.objects.all().order_by("-created_at")}
    return render(request, "articles/articles.html", context)
# '{{article.title}}'


# def new(request):
#     forms = ArticleForm()
#     context = {"forms":forms}
#     return render(request, "articles/new.html", context)



# def create(request):
#     form = ArticleForm(request.POST) # form에 request.POST에 있는 데이터 채워
#     if form.is_valid(): # form 형식에 맞으면
#         article = form.save() # 저장하고 해당 객체 반환 
#         return redirect("articles:article_detail", article.id)
#     return redirect("articles:new")

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect("articles:article_detail", article.id)
    else:
        forms = ArticleForm()
    context = {"forms": forms}
    return render(request, "articles/new.html", context)

def article_detail(request, pk):
    context = {"article": Article.objects.get(pk=pk)}
    return render(request, "articles/article_detail.html", context)


# def edit(request, pk):
#         context = {"article": Article.objects.get(pk=pk),}
#         return render(request, "articles/edit.html", context)


# def update(request, pk):
#     article = Article.objects.get(pk=pk)
#     article.title = request.POST.get("title")
#     article.content = request.POST.get("content")
#     article.save()
#     return redirect("articles:article_detail", article.pk)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect("articles:article_detail", article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        "form": form,
        "article": article,
    }
    return render(request, "articles/edit.html", context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect("articles:articles")


def index(request):
    return render(request, "articles/index.html")

# 지우랬는데 안지울거임


def hello(request):
    name = "희경"
    tags = ["python", "django", "html", "css"]
    books = ["해변의 카프카", "코스모스", "백설공주", "어린왕자"]
    context = {
        "name": name,
        "tags": tags,
        "books": books,
    }
    return render(request, "articles/hello.html", context)


def data_throw(request):
    return render(request, "articles/data_throw.html")


def data_catch(request):
    message = request.GET.get("message")
    context = {"data": message, }
    return render(request, "articles/data_catch.html", context)
