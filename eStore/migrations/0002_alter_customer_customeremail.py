# Generated by Django 4.0 on 2022-01-12 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eStore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customeremail',
            field=models.EmailField(max_length=254),
        ),
    ]
