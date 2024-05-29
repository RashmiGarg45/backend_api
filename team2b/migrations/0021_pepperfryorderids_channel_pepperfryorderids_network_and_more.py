# Generated by Django 5.0 on 2024-05-28 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team2b', '0020_pepperfryorderids_channel_pepperfryorderids_network_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IDHelperApps',
            fields=[
                ('serial', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('campaign_name', models.CharField(default='', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('date_added', models.DateField()),
                ('description', models.TimeField(default='')),
            ],
            options={
                'indexes': [models.Index(fields=['serial'], name='team2b_idhe_serial_a01b29_idx'), models.Index(fields=['campaign_name'], name='team2b_idhe_campaig_a94394_idx')],
            },
        ),
    ]