from django.db import models


# Create your models here.

class Items_List(models.Model):
    name = models.TextField(primary_key=True)
    imgs = models.ImageField(upload_to='images/')
    class Meta:
        db_table = "Items_List"  # 연결할 테이블 명
        managed = False
          # 데이터 추가 유무s

class UserScore(models.Model):
    nickname = models.CharField(max_length=50)
    score = models.IntegerField(default=0)
    class Meta:
        db_table = "UserScore"  # 연결할 테이블 명
        managed = True  # 데이터 추가 유무