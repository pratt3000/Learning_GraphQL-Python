# Generated by Django 2.1.4 on 2020-08-28 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('links', '0002_vote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='link',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='user',
        ),
        migrations.AddField(
            model_name='link',
            name='posted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]