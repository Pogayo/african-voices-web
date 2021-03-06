# Generated by Django 4.0.2 on 2022-04-10 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_dataset_speaker_gender_synthesizer_rfs_hrs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='languagesample',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='language_sample_set', to='app.language'),
        ),
        migrations.AlterField(
            model_name='synthesizersample',
            name='lang_sample',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='synthesizer_samples_set', to='app.languagesample'),
        ),
    ]
