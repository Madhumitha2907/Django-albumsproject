# Generated by Django 5.0.7 on 2024-07-31 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0006_alter_singer_date_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singer',
            name='date_updated',
            field=models.DateField(auto_now=True),
        ),
    ]