# Generated by Django 3.2.11 on 2022-01-20 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_eventcategory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventcategory',
            options={'verbose_name': 'Event Category', 'verbose_name_plural': 'Event Categories'},
        ),
        migrations.AddField(
            model_name='eventpost',
            name='event_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='events.eventcategory'),
        ),
    ]