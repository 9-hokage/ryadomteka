# Generated by Django 3.1.7 on 2021-03-13 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drugs', '0012_auto_20210313_1432'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drug',
            old_name='producer_id_s',
            new_name='producer',
        ),
    ]
