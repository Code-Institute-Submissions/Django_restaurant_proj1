# Generated by Django 3.2.15 on 2022-08-26 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0036_auto_20220826_1126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.AlterField(
            model_name='reservation',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]