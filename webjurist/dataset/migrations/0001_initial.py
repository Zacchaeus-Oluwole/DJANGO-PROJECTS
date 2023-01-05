# Generated by Django 3.1.1 on 2023-01-04 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cca_section', models.CharField(max_length=5)),
                ('offence', models.CharField(max_length=250)),
                ('law', models.TextField()),
                ('penalty', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'dataset',
            },
        ),
    ]