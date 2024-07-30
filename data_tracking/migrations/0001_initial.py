# Generated by Django 5.0 on 2024-06-25 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='combined_app_data',
            fields=[
                ('serial', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('pckname', models.CharField(max_length=200)),
                ('appname', models.CharField(max_length=200)),
                ('filename', models.CharField(max_length=200)),
                ('qa', models.CharField(max_length=200)),
                ('qa_upperlevel', models.CharField(max_length=200)),
                ('devteam', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'combined_app_data',
            },
        ),
        migrations.CreateModel(
            name='installReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=200)),
                ('campaign', models.CharField(max_length=200)),
                ('count', models.IntegerField()),
            ],
            options={
                'db_table': 'install_report',
            },
        ),
        migrations.CreateModel(
            name='revenueReport',
            fields=[
                ('serial', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=200)),
                ('channel', models.CharField(max_length=200)),
                ('network', models.CharField(max_length=200)),
                ('offer_id', models.CharField(max_length=200)),
                ('package_name', models.CharField(max_length=200)),
                ('campaign', models.CharField(max_length=200)),
                ('r_install', models.IntegerField()),
                ('payout', models.FloatField()),
                ('revenue', models.FloatField()),
                ('networkrevenue', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'revenueReport',
            },
        ),
    ]
