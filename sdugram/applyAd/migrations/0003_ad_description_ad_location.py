# Generated by Django 4.0.2 on 2022-03-09 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applyAd', '0002_ad_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='description',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='ad',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
