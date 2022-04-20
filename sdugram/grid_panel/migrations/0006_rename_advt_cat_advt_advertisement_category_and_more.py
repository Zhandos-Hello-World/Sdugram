# Generated by Django 4.0.2 on 2022-04-10 09:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('grid_panel', '0005_alter_advt_advt_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advt',
            old_name='advt_cat',
            new_name='advertisement_category',
        ),
        migrations.RenameField(
            model_name='advt',
            old_name='advt_favourite',
            new_name='advertisement_favourites',
        ),
        migrations.RenameField(
            model_name='advt',
            old_name='advt_location',
            new_name='advertisement_location',
        ),
        migrations.RenameField(
            model_name='advt',
            old_name='advt_name',
            new_name='advertisement_name',
        ),
        migrations.RemoveField(
            model_name='advt',
            name='advt_date_created',
        ),
        migrations.RemoveField(
            model_name='advt',
            name='advt_description',
        ),
        migrations.RemoveField(
            model_name='advt',
            name='advt_dt',
        ),
        migrations.RemoveField(
            model_name='advt',
            name='advt_host_id',
        ),
        migrations.RemoveField(
            model_name='advt',
            name='advt_img',
        ),
        migrations.RemoveField(
            model_name='advt',
            name='advt_item_id',
        ),
        migrations.RemoveField(
            model_name='advt',
            name='advt_link',
        ),
        migrations.RemoveField(
            model_name='advt',
            name='advt_price',
        ),
        migrations.RemoveField(
            model_name='advt',
            name='advt_type',
        ),
        migrations.RemoveField(
            model_name='advt',
            name='advt_views',
        ),
        migrations.AddField(
            model_name='advt',
            name='advertisement_date_created',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='advt',
            name='advertisement_description',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='advt',
            name='advertisement_image',
            field=models.ImageField(null=True, upload_to='media/adver/'),
        ),
        migrations.AddField(
            model_name='advt',
            name='advertisement_price',
            field=models.IntegerField(null=True, verbose_name='Price'),
        ),
        migrations.AddField(
            model_name='advt',
            name='advertisement_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]