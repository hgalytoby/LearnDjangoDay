from django.db import models


# Create your models here.

class UserModel(models.Model):
    u_name = models.CharField(max_length=16, unique=True)
    u_password = models.CharField(max_length=256)


class Address(models.Model):
    a_address = models.CharField(max_length=128)
    a_user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True)


class Test(models.Model):
    t_name = models.CharField(max_length=16, null=True, blank=True)
    t_test = models.CharField(max_length=12)
    t_owner = models.ForeignKey(UserModel, on_delete=models.CASCADE)


class Anime(models.Model):
    name = models.CharField()


class Es(models.Model):
    owner = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='aras')

    def delete_file(self):
        pass


anime_db = Anime.objects.filter(name=0).prefetch_related('owner')
for anime in anime_db:
    for es in anime.aras.all():
        es.delete_file()
