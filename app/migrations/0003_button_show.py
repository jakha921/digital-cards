# Generated by Django 4.2.5 on 2023-09-30 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_client_fio_remove_client_position_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='button',
            name='show',
            field=models.BooleanField(default=True),
        ),
    ]
