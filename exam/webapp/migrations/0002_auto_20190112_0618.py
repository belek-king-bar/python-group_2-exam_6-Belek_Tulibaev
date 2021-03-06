# Generated by Django 2.1 on 2019-01-12 06:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='author', to=settings.AUTH_USER_MODEL, verbose_name='Автор поста'),
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='friends',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='friends',
            field=models.ManyToManyField(blank=True, null=True, related_name='friend', to=settings.AUTH_USER_MODEL, verbose_name='Друзья'),
        ),
    ]
