# Generated by Django 5.1.5 on 2025-03-01 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentsrecord', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='USN',
            new_name='usn',
        ),
    ]
