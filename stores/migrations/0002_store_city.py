# Generated by Django 3.1.3 on 2020-12-02 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='city',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
