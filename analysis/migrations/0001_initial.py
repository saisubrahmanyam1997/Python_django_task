# Generated by Django 3.2.3 on 2021-05-21 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=10)),
                ('Roll_Number', models.IntegerField(max_length=10)),
                ('Date_of_Birth', models.DateField(max_length=8)),
            ],
        ),
    ]
