from django.db import models

class User(models.Model):
    nickname = models.CharField(max_length=20,primary_key=True)
    class Meta:
        db_table = "User"  # 연결할 테이블 명
        managed = True # 데이터 추가 유무