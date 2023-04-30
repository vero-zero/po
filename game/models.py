from django.db import models
import base64


class Items_List(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(default='my_default_value')
    imgs = models.TextField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        with open(self.imgs.path, 'rb',encoding='utf-8') as img_file:
            encoded_string = base64.b64encode(img_file.read()).decode('utf-8')
            self.imgs = encoded_string
            self.save(update_fields=['imgs'])

    class Meta:
        db_table = "Items_List"
        managed = False

    
class UserScore(models.Model):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=50,default='my_default_value')
    score = models.IntegerField(default=0)

    class Meta:
        db_table = "UserScore"
        managed = True