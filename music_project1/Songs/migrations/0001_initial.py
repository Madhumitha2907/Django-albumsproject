# Generated by Django 5.0.7 on 2024-07-29 09:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Albums', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('SongID', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=255)),
                ('Duration', models.TimeField()),
                ('DateCreated', models.DateField(auto_now_add=True)),
                ('DateUpdated', models.DateField(auto_now=True)),
                ('Album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Albums.album')),
            ],
        ),
    ]
