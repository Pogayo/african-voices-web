# Generated by Django 4.0.2 on 2022-04-14 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_synthesizerequestmodel_audio_format_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='synthesizerequestmodel',
            name='synth_id',
            field=models.CharField(choices=[], default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='synthesizerequestmodel',
            name='text',
            field=models.TextField(max_length=100000),
        ),
    ]
