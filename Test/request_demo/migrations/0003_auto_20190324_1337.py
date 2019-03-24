# Generated by Django 2.1.7 on 2019-03-24 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request_demo', '0002_auto_20190324_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='sex',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=10, verbose_name='性别'),
        ),
    ]
