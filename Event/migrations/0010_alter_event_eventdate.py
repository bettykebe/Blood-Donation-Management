# Generated by Django 4.0.3 on 2022-04-21 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0009_event_eventpic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='EventDate',
            field=models.DateField(),
        ),
    ]
