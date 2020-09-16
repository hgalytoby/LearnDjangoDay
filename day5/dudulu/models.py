from django.db import models


# Create your models here.

class UserModel(models.Model):
    u_name = models.CharField(max_length=32)
    # upload_to 根據路徑， 相對於 MEDIA_ROOT 媒體根目錄
    u_icon = models.ImageField(upload_to='%Y/%m/%d/icons')
