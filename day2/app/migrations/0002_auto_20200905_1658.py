# Generated by Django 3.1.1 on 2020-09-05 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='p_name',
            field=models.CharField(max_length=16),
        ),
    ]
