# Generated by Django 5.0.7 on 2024-07-31 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0005_alter_singer_name_alter_writer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singer',
            name='date_updated',
            field=models.DateField(),
        ),
    ]
