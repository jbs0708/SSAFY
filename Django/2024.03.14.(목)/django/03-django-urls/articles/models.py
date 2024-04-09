from django.db import models

# Create your models here.
class Article(models.Model):
  # 필드이름 = 데이터 타입(제약 조건)
    title = models.CharField(max_length=20)
    content = models.TextField()