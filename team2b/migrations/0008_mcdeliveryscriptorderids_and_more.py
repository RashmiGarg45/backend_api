# Generated by Django 4.1.2 on 2023-12-22 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team2b', '0007_igpscriptorderids_booking_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='McdeliveryScriptOrderIds',
            fields=[
                ('serial', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('campaign_name', models.CharField(default='igpmodd', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(max_length=50, unique=True)),
                ('invoice_date_time', models.DateTimeField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('gross_amount', models.FloatField(default=0)),
                ('member_name', models.CharField(blank=True, max_length=100, null=True)),
                ('used_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('extra_details', models.JSONField(default=dict)),
            ],
        ),
        migrations.AddIndex(
            model_name='mcdeliveryscriptorderids',
            index=models.Index(fields=['id'], name='team2b_mcde_id_74db41_idx'),
        ),
        migrations.AddIndex(
            model_name='mcdeliveryscriptorderids',
            index=models.Index(fields=['invoice_date_time'], name='team2b_mcde_invoice_76de7a_idx'),
        ),
    ]
