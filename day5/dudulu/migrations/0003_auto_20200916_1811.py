# Generated by Django 3.1.1 on 2020-09-16 18:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('dudulu', '0002_auto_20200916_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='u_icon',
            field=models.ImageField(upload_to='%Y/%m/%d/icons'),
        ),
    ]
