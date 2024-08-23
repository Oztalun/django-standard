from django.db import models
from django.conf import settings
import datetime as dt
from django.utils import timezone



class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/article/", blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles")
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_articles"
    )

    def __str__(self):
        return self.title
    
    def time_dif(self):
        difftotal = timezone.now()-self.updated_at
        day = difftotal.days
        second = difftotal.seconds
        if day>0:
            if day<7:
                print(day)
                return f'{day}일 전'
            elif day<30:
                return f'{day//7}주 전'
            elif day<365:
                return f'{day//30}달 전'
            else:
                return f'{day//365}년 전'
        elif second>3599:
            return f'{second//3600}시간 전'
        elif second>59:
            return f'{second//60}분 전'
        else:
            return f'{second}초 전'


# class ArticleLike(models.Model):
#     article = models.ForeignKey(
#         Article, on_delete=models.CASCADE, related_name="likes"
#     )
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="likes"
#     )


class Comment(models.Model):
    # article = models.ForeignKey(Article, on_delete=models.CASCADE)
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
