# Generated by Django 4.0 on 2022-01-13 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eStore', '0008_remove_ticket_fault'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='fault',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eStore.fault'),
        ),
    ]
