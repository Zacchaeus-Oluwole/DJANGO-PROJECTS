# Generated by Django 3.1.1 on 2023-01-04 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0002_auto_20230104_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='offence',
            field=models.CharField(max_length=250),
        ),
    ]
