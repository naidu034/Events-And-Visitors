# Generated by Django 3.2.4 on 2021-08-18 10:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_alter_event_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]