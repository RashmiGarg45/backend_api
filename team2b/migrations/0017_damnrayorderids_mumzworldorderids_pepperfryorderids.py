# Generated by Django 5.0 on 2024-03-12 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team2b', '0016_watchoorderidsmining'),
    ]

    operations = [
        migrations.CreateModel(
            name='DamnrayOrderIds',
            fields=[
                ('serial', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('campaign_name', models.CharField(default='igpmodd', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(max_length=50, unique=True)),
                ('products', models.JSONField(blank=True, default=list, null=True)),
                ('payment', models.JSONField(blank=True, default=dict, null=True)),
                ('price', models.CharField(max_length=50)),
                ('used_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('extra_details', models.JSONField(blank=True, default=dict, null=True)),
            ],
            options={
                'indexes': [models.Index(fields=['id'], name='team2b_damn_id_1c4ede_idx')],
            },
        ),
        migrations.CreateModel(
            name='PepperfryOrderIds',
            fields=[
                ('serial', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('campaign_name', models.CharField(default='pepperfrymodd', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order_status', models.CharField(default=0, max_length=100)),
                ('id', models.CharField(max_length=50, unique=True)),
                ('used_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('extra_details', models.JSONField(blank=True, default=dict, null=True)),
            ],
            options={
                'indexes': [models.Index(fields=['id'], name='team2b_pepp_id_21bf25_idx')],
            },
        ),
    ]