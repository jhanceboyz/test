# Generated by Django 4.0 on 2022-01-13 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eStore', '0009_ticket_fault'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='fault',
        ),
        migrations.DeleteModel(
            name='fault',
        ),
    ]
