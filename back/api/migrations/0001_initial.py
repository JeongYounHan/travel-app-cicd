# Generated by Django 3.1.4 on 2021-09-22 12:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('continent', models.CharField(max_length=20)),
                ('image', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('div', models.CharField(max_length=20)),
                ('lat', models.FloatField(max_length=15)),
                ('lng', models.FloatField(max_length=15)),
                ('description', models.TextField(blank=True)),
                ('time', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.TextField(blank=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.city')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.city')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('order', models.FloatField(max_length=15)),
                ('memo', models.TextField(blank=True)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.place')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.trip')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]