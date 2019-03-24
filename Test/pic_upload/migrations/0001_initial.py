# Generated by Django 2.1.7 on 2019-03-21 05:31

import datetime
from django.db import migrations, models
import pic_upload.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='unname', max_length=100, verbose_name='标题')),
                ('image', models.ImageField(blank=True, upload_to=pic_upload.models.user_dir_path, verbose_name='图片')),
                ('date', models.DateField(default=datetime.date.today)),
            ],
            options={
                'db_table': 'picture',
            },
        ),
    ]