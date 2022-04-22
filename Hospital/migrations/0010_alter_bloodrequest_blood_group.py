# Generated by Django 4.0.3 on 2022-04-11 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0009_alter_bloodrequest_blood_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodrequest',
            name='Blood_Group',
            field=models.CharField(blank=True, choices=[(None, 'Select type'), ('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB-')], max_length=10, null=True),
        ),
    ]