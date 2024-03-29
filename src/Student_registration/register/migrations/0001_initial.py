# Generated by Django 4.2.7 on 2023-11-18 19:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coll_Units',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2023, 11, 18, 19, 49, 12, 900812, tzinfo=datetime.timezone.utc))),
                ('rm_date', models.DateTimeField(default=datetime.datetime(2023, 11, 18, 19, 49, 12, 900812, tzinfo=datetime.timezone.utc))),
            ],
        ),
        migrations.CreateModel(
            name='Collegian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nationalCode', models.CharField(max_length=10)),
                ('collegianCode', models.CharField(max_length=14)),
                ('collegianFirstName', models.CharField(max_length=200)),
                ('collegianLastName', models.CharField(max_length=300)),
                ('collegianAge', models.IntegerField(default=18)),
                ('collegianFathersName', models.CharField(max_length=400)),
                ('collegianMajor', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2023, 11, 18, 19, 49, 12, 836002, tzinfo=datetime.timezone.utc))),
                ('rm_date', models.DateTimeField(default=datetime.datetime(2023, 11, 18, 19, 49, 12, 836002, tzinfo=datetime.timezone.utc))),
            ],
        ),
        migrations.CreateModel(
            name='Professors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nationalCode', models.CharField(max_length=10)),
                ('professorCode', models.CharField(max_length=14)),
                ('professorFirstName', models.CharField(max_length=200)),
                ('professorLastName', models.CharField(max_length=300)),
                ('professorAge', models.IntegerField(default=28)),
                ('professorFathersName', models.CharField(max_length=400)),
                ('professorMajor', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2023, 11, 18, 19, 49, 12, 900812, tzinfo=datetime.timezone.utc))),
                ('rm_date', models.DateTimeField(default=datetime.datetime(2023, 11, 18, 19, 49, 12, 900812, tzinfo=datetime.timezone.utc))),
            ],
        ),
    ]
