from django.db import models

class Article(models.Model):
    title      = models.CharField('제목', max_length=126, null=False)
    content    = models.TextField('내용', null=False)
    author     = models.CharField('작성자', max_length=16, null=False) # auther => author 로 수정
    created_at = models.DateTimeField('작성일', auto_now_add=True)
