# Generated by Django 4.2.11 on 2024-03-29 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=10)),
                ('plan', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
    ]
