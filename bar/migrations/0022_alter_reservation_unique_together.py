# Generated by Django 3.2.15 on 2022-08-24 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0021_alter_menu_details'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reservation',
            unique_together={('date', 'time')},
        ),
    ]