# Generated by Django 3.1.3 on 2020-12-02 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('longitude', models.CharField(max_length=255)),
                ('latitude', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('work_time_weekdays', models.CharField(max_length=255)),
                ('work_time_sat', models.CharField(max_length=255)),
                ('work_time_sun', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'stores',
            },
        ),
    ]