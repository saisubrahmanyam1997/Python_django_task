# Generated by Django 3.2.3 on 2021-05-22 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0002_auto_20210521_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='marks',
            field=models.PositiveIntegerField(null=True),
        ),
    ]