# Generated by Django 4.2.1 on 2023-05-17 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoomModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Junior Suite', 'Junior Suite'), ('Executive Suite', 'Executive Suite'), ('Super Deluxe', 'Super Deluxe')], max_length=120, null=True)),
                ('room_number', models.IntegerField()),
                ('floor_number', models.IntegerField()),
                ('price_per_night', models.IntegerField()),
                ('description', models.EmailField(max_length=120, null=True)),
            ],
        ),
    ]