# Generated by Django 2.2 on 2019-04-11 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='num',
            field=models.DecimalField(decimal_places=2, default=-1, max_digits=5),
        ),
    ]
