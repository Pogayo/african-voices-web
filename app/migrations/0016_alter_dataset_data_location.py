# Generated by Django 4.0.2 on 2022-04-24 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_synthesizer_is_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='data_location',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
