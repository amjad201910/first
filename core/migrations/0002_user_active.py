# Generated by Django 4.2.3 on 2023-07-29 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='active',
            field=models.BooleanField(default=False, verbose_name='active for chat'),
        ),
    ]