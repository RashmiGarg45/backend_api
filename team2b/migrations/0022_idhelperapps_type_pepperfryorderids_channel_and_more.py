# Generated by Django 5.0 on 2024-05-28 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team2b', '0021_pepperfryorderids_channel_pepperfryorderids_network_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='idhelperapps',
            name='type',
            field=models.CharField(default='order_id', max_length=8),
        ),
    ]