# Generated by Django 4.0.3 on 2022-04-24 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donor', '0033_rename_datetime_appointment_date_appointment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='Height',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='Weight',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]