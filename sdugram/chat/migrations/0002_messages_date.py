# Generated by Django 4.0.2 on 2022-04-10 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]