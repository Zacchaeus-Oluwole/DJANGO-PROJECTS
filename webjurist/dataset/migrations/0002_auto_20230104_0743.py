# Generated by Django 3.1.1 on 2023-01-04 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='offence',
            field=models.TextField(),
        ),
        migrations.AlterModelTable(
            name='dataset',
            table=None,
        ),
    ]