# Generated by Django 3.2.11 on 2022-01-18 22:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_remove_newspost_news_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspost',
            name='news_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Post date'),
        ),
    ]
