# Generated by Django 5.0 on 2024-05-28 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team2b', '0025_simulationids_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='idhelperapps',
            name='team',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AddField(
            model_name='idhelperapps',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='idhelperapps',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
