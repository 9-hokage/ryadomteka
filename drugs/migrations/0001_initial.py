# Generated by Django 3.1.3 on 2020-12-02 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('form_drug', models.CharField(max_length=255)),
                ('recipe', models.BooleanField()),
                ('reg_id', models.CharField(max_length=255)),
                ('atc_classification', models.CharField(max_length=255)),
                ('producer', models.CharField(max_length=255)),
                ('classification', models.CharField(max_length=255)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'drugs',
            },
        ),
    ]
