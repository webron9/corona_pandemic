# Generated by Django 3.0.3 on 2020-05-12 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stats',
            name='new_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
