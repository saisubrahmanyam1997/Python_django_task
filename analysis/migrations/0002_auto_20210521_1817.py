# Generated by Django 3.2.3 on 2021-05-21 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Date_of_Birth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='Name',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='student',
            name='Roll_Number',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
