# Generated by Django 3.2.9 on 2021-12-12 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20211211_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=250)),
                ('province', models.CharField(max_length=250)),
                ('city_muni', models.CharField(max_length=250)),
                ('level', models.CharField(max_length=10)),
            ],
        ),
    ]
