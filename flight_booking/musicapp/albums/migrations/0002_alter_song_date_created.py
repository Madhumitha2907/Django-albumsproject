# Generated by Django 5.0.7 on 2024-07-31 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='date_created',
            field=models.DateField(),
        ),
    ]
