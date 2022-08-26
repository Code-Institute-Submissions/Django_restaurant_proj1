# Generated by Django 3.2.15 on 2022-08-26 11:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bar', '0035_alter_reservation_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='name',
            field=models.ForeignKey(default='first_name', on_delete=django.db.models.deletion.CASCADE, to='bar.customer'),
        ),
    ]