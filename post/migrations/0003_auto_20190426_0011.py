# Generated by Django 2.2 on 2019-04-25 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20190424_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='İçerik'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publiishing_date',
            field=models.DateTimeField(verbose_name='Yayınlanma tarihi'),
        ),
    ]
