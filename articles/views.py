# from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from django.conf import settings
from django.utils import timezone



def index(request):
    return render(request, "articles/index.html")




def articles(request):
    context = {"articles": Article.objects.all().order_by("-created_at"), "timediff": timezone.now()}
    return render(request, "articles/articles.html", context)
# '{{article.title}}'


@require_POST
def like(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
    else:
        return redirect("accounts:login")

    return redirect("articles:articles")


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
@login_required
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article = form.save()
            return redirect("articles:article_detail", article.id)
    else:
        forms = ArticleForm()
    context = {"forms": forms}
    return render(request, "articles/new.html", context)



def article_detail(request, pk): 
    article = get_object_or_404(Article, pk=pk)
    print(article.time_dif())
    comment_form = CommentForm()
    comments = article.comments.all()
    context = {"article": article, "comment_form":comment_form, "comments":comments}
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

@login_required
@require_http_methods(["GET", "POST"])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
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



@require_POST
def comment_create(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
    return redirect("articles:article_detail", article.pk)


@require_POST
def comment_delete(request, pk):# comment의 pk
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=pk)# 해당 comment 불러옴
        articleid = comment.article
        article = articleid.id
        comment.delete()
        return redirect("articles:article_detail", article)


@login_required
@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        article.delete()
    return redirect("articles:articles")


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
