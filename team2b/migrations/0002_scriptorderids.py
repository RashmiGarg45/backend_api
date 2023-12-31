# Generated by Django 5.0 on 2023-12-21 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team2b', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScriptOrderIds',
            fields=[
                ('serial', models.IntegerField(default=0, editable=False, primary_key=True, serialize=False)),
                ('campaign_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('used_at', models.DateTimeField(default=None)),
                ('id', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('extra_details', models.JSONField(default=dict)),
            ],
            options={
                'indexes': [models.Index(fields=['id'], name='team2b_scri_id_793708_idx')],
            },
        ),
    ]
