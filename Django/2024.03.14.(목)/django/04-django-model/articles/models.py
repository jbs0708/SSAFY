from django.db import models

# Create your models here.
class Article(models.Model):
  # 필드이름 = 데이터 타입(제약 조건)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# 최종 테이블 이름은 "앱이름_클래스이름"
