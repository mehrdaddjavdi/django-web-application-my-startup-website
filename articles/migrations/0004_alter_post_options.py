# Generated by Django 3.2.2 on 2021-06-08 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20210517_2147'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('publish',)},
        ),
    ]