# Generated by Django 3.1.7 on 2021-03-06 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('stores', '0004_auto_20210306_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='city_new',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.city'),
        ),
    ]
