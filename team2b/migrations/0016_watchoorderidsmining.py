# Generated by Django 5.0 on 2024-02-17 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team2b', '0015_rename_ostinshopscriptorderidsconstants_habibscriptorderidsconstants_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchoOrderIdsMining',
            fields=[
                ('serial', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('campaign_name', models.CharField(default='igpmodd', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(max_length=50, unique=True)),
                ('order_status', models.CharField(default=0, max_length=100)),
                ('used_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('extra_details', models.JSONField(blank=True, default=dict, null=True)),
            ],
            options={
                'indexes': [models.Index(fields=['id'], name='team2b_watc_id_61a72f_idx')],
            },
        ),
    ]
