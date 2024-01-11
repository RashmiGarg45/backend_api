# Generated by Django 4.1.2 on 2023-12-21 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckEventCount',
            fields=[
                ('serial', models.IntegerField(default=0, editable=False, primary_key=True, serialize=False)),
                ('campaign_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('channel', models.CharField(max_length=100)),
                ('network', models.CharField(max_length=100)),
                ('offer_id', models.CharField(max_length=100)),
                ('install_event', models.IntegerField(default=0)),
                ('open_event', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddIndex(
            model_name='checkeventcount',
            index=models.Index(fields=['campaign_name'], name='team2b_chec_campaig_764311_idx'),
        ),
        migrations.AddIndex(
            model_name='checkeventcount',
            index=models.Index(fields=['channel'], name='team2b_chec_channel_feff7e_idx'),
        ),
        migrations.AddIndex(
            model_name='checkeventcount',
            index=models.Index(fields=['network'], name='team2b_chec_network_1354a9_idx'),
        ),
        migrations.AddIndex(
            model_name='checkeventcount',
            index=models.Index(fields=['offer_id'], name='team2b_chec_offer_i_af887a_idx'),
        ),
        migrations.AddIndex(
            model_name='checkeventcount',
            index=models.Index(fields=['channel', 'network'], name='team2b_chec_channel_b16330_idx'),
        ),
        migrations.AddIndex(
            model_name='checkeventcount',
            index=models.Index(fields=['offer_id', 'network'], name='team2b_chec_offer_i_95253e_idx'),
        ),
        migrations.AddIndex(
            model_name='checkeventcount',
            index=models.Index(fields=['offer_id', 'channel'], name='team2b_chec_offer_i_804930_idx'),
        ),
        migrations.AddIndex(
            model_name='checkeventcount',
            index=models.Index(fields=['channel', 'offer_id', 'network'], name='team2b_chec_channel_c26bc1_idx'),
        ),
    ]