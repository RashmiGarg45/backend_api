# Generated by Django 5.0 on 2024-05-28 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team2b', '0020_pepperfryorderids_channel_pepperfryorderids_network_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pepperfryorderids',
            name='channel',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='pepperfryorderids',
            name='network',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='pepperfryorderids',
            name='offer_id',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.CreateModel(
            name='BharatmatrimonyUserIds',
            fields=[
                ('serial', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('campaign_name', models.CharField(default='bharatmatrimonymodd', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(max_length=20, unique=True)),
                ('used_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('extra_details', models.JSONField(blank=True, default=dict, null=True)),
            ],
            options={
                'indexes': [models.Index(fields=['id'], name='team2b_bhar_id_6413d2_idx')],
            },
        ),
        migrations.CreateModel(
            name='GomcdOrderIds',
            fields=[
                ('serial', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('campaign_name', models.CharField(default='gomcdoauto', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(max_length=20, unique=True)),
                ('used_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('extra_details', models.JSONField(blank=True, default=dict, null=True)),
            ],
            options={
                'indexes': [models.Index(fields=['id'], name='team2b_gomc_id_7a2fb5_idx')],
            },
        ),
        migrations.CreateModel(
            name='LazuritOrderIds',
            fields=[
                ('serial', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('campaign_name', models.CharField(default='lazuritappmetrica', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(max_length=15, unique=True)),
                ('price', models.CharField(max_length=15, unique=True)),
                ('order_status', models.CharField(default=0, max_length=20)),
                ('used_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('extra_details', models.JSONField(blank=True, default=dict, null=True)),
            ],
            options={
                'indexes': [models.Index(fields=['id'], name='team2b_lazu_id_a0733d_idx')],
            },
        ),
        migrations.CreateModel(
            name='Player6auto',
            fields=[
                ('serial', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('campaign_name', models.CharField(default='player6auto', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event_token', models.CharField(max_length=30, unique=True)),
                ('event_value', models.JSONField(blank=True, default=dict, null=True)),
                ('used_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('device_data', models.JSONField(blank=True, default=dict, null=True)),
                ('app_data', models.JSONField(blank=True, default=dict, null=True)),
                ('extra_details', models.JSONField(blank=True, default=dict, null=True)),
            ],
            options={
                'indexes': [models.Index(fields=['serial'], name='team2b_play_serial_3d0f55_idx')],
            },
        ),
        migrations.CreateModel(
            name='SamsclubMemberIds',
            fields=[
                ('serial', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('campaign_name', models.CharField(default='samsclubmodd', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(max_length=25, unique=True)),
                ('used_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('extra_details', models.JSONField(blank=True, default=dict, null=True)),
            ],
            options={
                'indexes': [models.Index(fields=['id'], name='team2b_sams_id_d17d73_idx')],
            },
        ),
        migrations.CreateModel(
            name='SimulationIds',
            fields=[
                ('serial', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('campaign_name', models.CharField(default='', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date_added', models.DateField()),
                ('timestamp', models.DateTimeField()),
                ('id', models.CharField(max_length=100, unique=True)),
                ('constraint', models.FloatField(default=1)),
            ],
            options={
                'indexes': [models.Index(fields=['id'], name='team2b_simu_id_125d62_idx'), models.Index(fields=['campaign_name'], name='team2b_simu_campaig_767149_idx'), models.Index(fields=['campaign_name', 'id', 'timestamp'], name='team2b_simu_campaig_d1dba2_idx')],
            },
        ),
        migrations.CreateModel(
            name='WeWorldIds',
            fields=[
                ('serial', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('campaign_name', models.CharField(default='weworldauto', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(max_length=25, unique=True)),
                ('used_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('extra_details', models.JSONField(blank=True, default=dict, null=True)),
            ],
            options={
                'db_table': 'team2b_weworlduserids',
                'indexes': [models.Index(fields=['id'], name='team2b_wewo_id_e78421_idx')],
            },
        ),
    ]
