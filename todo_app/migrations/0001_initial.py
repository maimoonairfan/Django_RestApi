# Generated by Django 4.1.7 on 2023-04-09 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
