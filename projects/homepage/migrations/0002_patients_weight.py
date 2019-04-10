# Generated by Django 2.2 on 2019-04-10 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sex', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cp', models.DecimalField(decimal_places=2, max_digits=5)),
                ('trestbps', models.DecimalField(decimal_places=2, max_digits=5)),
                ('chol', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fbs', models.DecimalField(decimal_places=2, max_digits=5)),
                ('restecg', models.DecimalField(decimal_places=2, max_digits=5)),
                ('thalach', models.DecimalField(decimal_places=2, max_digits=5)),
                ('exang', models.DecimalField(decimal_places=2, max_digits=5)),
                ('oldpeak', models.DecimalField(decimal_places=2, max_digits=5)),
                ('slope', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ca', models.DecimalField(decimal_places=2, max_digits=5)),
                ('thai', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='patients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('ResultTest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.ResultTest')),
            ],
        ),
    ]