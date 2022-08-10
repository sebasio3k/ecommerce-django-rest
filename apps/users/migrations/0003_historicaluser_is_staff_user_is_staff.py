# Generated by Django 4.1 on 2022-08-10 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_historicaluser_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaluser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]