# Generated by Django 4.2.11 on 2024-04-15 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Recommended',
            new_name='Recommend',
        ),
    ]