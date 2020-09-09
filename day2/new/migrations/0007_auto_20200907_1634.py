# Generated by Django 3.1.1 on 2020-09-07 16:34

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0006_animal'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='animal',
            managers=[
                ('a_obj', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]
