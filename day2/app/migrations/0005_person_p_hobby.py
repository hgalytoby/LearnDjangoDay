# Generated by Django 3.1.1 on 2020-09-06 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200905_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='p_hobby',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
