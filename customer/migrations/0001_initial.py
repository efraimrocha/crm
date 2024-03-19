# Generated by Django 5.0.3 on 2024-03-15 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('birth_date', models.DateField()),
                ('area_code', models.CharField(max_length=3)),
                ('phone_number', models.CharField(max_length=15)),
                ('country', models.CharField(max_length=30)),
                ('estate', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=60)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('update_data', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]
