# Generated by Django 4.1.3 on 2022-12-12 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video',
            field=models.URLField(default='1'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='video',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
    ]