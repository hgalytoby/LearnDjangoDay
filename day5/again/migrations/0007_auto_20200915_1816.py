# Generated by Django 3.1.1 on 2020-09-15 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('again', '0006_auto_20200915_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idcard',
            name='id_person',
            field=models.OneToOneField(blank=True, default='123', null=True,
                                       on_delete=django.db.models.deletion.SET_DEFAULT, to='again.person'),
        ),
    ]
