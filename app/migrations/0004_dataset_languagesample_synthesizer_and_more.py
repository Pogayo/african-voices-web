# Generated by Django 4.0.2 on 2022-04-10 16:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_languagecountry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('data_id', models.CharField(max_length=100, unique=True)),
                ('source', models.CharField(max_length=100)),
                ('pass0_utt', models.FloatField(max_length=100)),
                ('pass0_mcd', models.FloatField(max_length=100)),
                ('pass1_utt', models.IntegerField(default=0)),
                ('pass1_mcd', models.FloatField(default=0)),
                ('duration', models.FloatField(default=0)),
                ('data_location', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='LanguageSample',
            fields=[
                ('uuid', models.CharField(default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('sample_id', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=100)),
                ('pronunciation', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Synthesizer',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('synth_id', models.CharField(max_length=100, unique=True)),
                ('rfs_utt', models.IntegerField(default=0)),
                ('mcd_base', models.FloatField(default=0)),
                ('mcd_rfs', models.FloatField(default=0)),
                ('data_location', models.CharField(max_length=256)),
                ('flite_location', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dataset')),
            ],
        ),
        migrations.RenameField(
            model_name='language',
            old_name='lang_code',
            new_name='lang_code_639_2',
        ),
        migrations.RemoveField(
            model_name='language',
            name='base',
        ),
        migrations.RemoveField(
            model_name='language',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='language',
            name='pass0_mcd',
        ),
        migrations.RemoveField(
            model_name='language',
            name='pass0_utt',
        ),
        migrations.RemoveField(
            model_name='language',
            name='pass1_mcd',
        ),
        migrations.RemoveField(
            model_name='language',
            name='pass1_utt',
        ),
        migrations.RemoveField(
            model_name='language',
            name='rfs',
        ),
        migrations.RemoveField(
            model_name='language',
            name='rfs_utt',
        ),
        migrations.AddField(
            model_name='language',
            name='lang_code_639_1',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='language',
            name='lang_native_speakers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='language',
            name='lang_non_native_speakers',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='SynthesizerSample',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('sample_location', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('lang_sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.languagesample')),
                ('synth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.synthesizer')),
            ],
        ),
        migrations.AddField(
            model_name='synthesizer',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.language'),
        ),
        migrations.AddField(
            model_name='languagesample',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.language'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='lang_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.language'),
        ),
    ]