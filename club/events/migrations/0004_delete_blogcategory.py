# Generated by Django 3.2.11 on 2022-01-20 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_blogcategory'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogCategory',
        ),
    ]