# Generated by Django 3.2.4 on 2021-06-10 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_alter_address_a_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='a_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.usermodel'),
        ),
    ]
