# Generated by Django 3.2.4 on 2021-06-10 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=16, unique=True)),
                ('u_password', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_address', models.CharField(max_length=128)),
                ('a_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.usermodel')),
            ],
        ),
    ]
