# Generated by Django 4.2.1 on 2023-05-18 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grand_oasis', '0003_alter_roommodel_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='roommodel',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
