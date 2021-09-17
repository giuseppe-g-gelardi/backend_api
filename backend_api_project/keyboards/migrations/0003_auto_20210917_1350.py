# Generated by Django 3.2.7 on 2021-09-17 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('keyboards', '0002_auto_20210917_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyboards',
            name='color',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='keyboards',
            name='layout',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='keyboards',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]