# Generated by Django 3.1.7 on 2021-03-26 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=1024)),
                ('original_link', models.CharField(max_length=2048)),
                ('newspaper_name', models.CharField(max_length=255)),
                ('img_link', models.CharField(max_length=2048)),
            ],
        ),
    ]
