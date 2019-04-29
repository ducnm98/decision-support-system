# Generated by Django 2.2 on 2019-04-18 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20190413_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='age',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='ca',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='chol',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='cp',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='exang',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='fbs',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='num',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='oldpeak',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='restecg',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='sex',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='slope',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='thal',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='thalach',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='trestbps',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True),
        ),
    ]
