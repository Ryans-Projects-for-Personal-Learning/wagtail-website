# Generated by Django 3.2.11 on 2022-01-19 16:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpost',
            name='event_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Event Date'),
        ),
        migrations.AlterField(
            model_name='eventpost',
            name='event_image',
            field=models.ForeignKey(help_text='This is the thumbnail for the event page.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
