# Generated by Django 5.0.7 on 2024-07-29 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('SingerID', models.AutoField(primary_key=True, serialize=False)),
                ('Singer_Name', models.CharField(max_length=255)),
            ],
        ),
    ]