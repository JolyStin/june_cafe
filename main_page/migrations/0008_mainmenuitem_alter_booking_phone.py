# Generated by Django 4.2.2 on 2023-07-03 16:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0007_remove_booking_date_time_booking_date_booking_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainMenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='menu item')),
                ('slug', models.SlugField(unique=True, verbose_name='url')),
                ('position', models.SmallIntegerField()),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('position',),
            },
        ),
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: +380xxxxxxxxx, 0xxxxxxxxx', regex='^(\\+38)?0\\d{9}$')]),
        ),
    ]
