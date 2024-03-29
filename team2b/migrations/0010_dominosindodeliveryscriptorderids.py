# Generated by Django 5.0 on 2024-01-11 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team2b', '0009_lightinthebox_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DominosIndodeliveryScriptOrderIds',
            fields=[
                ('serial', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('campaign_name', models.CharField(default='igpmodd', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(max_length=50, unique=True)),
                ('invoice_date_time', models.DateTimeField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('order_type', models.FloatField(default=0)),
                ('used_at', models.DateTimeField(blank=True, default=None, null=True)),
            ],
            options={
                'indexes': [models.Index(fields=['id'], name='team2b_domi_id_b46c71_idx'), models.Index(fields=['invoice_date_time'], name='team2b_domi_invoice_0c7aba_idx')],
            },
        ),
    ]
