# Generated by Django 3.2.2 on 2021-05-25 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0002_alter_emailformagazine_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailformagazine',
            name='joined',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
