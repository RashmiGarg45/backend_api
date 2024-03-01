from django.db import models

# Create your models here.

class revenueReport(models.Model):
    """
    This is the base model for all the models.
    It has all the requried and common fields in our custom models.
    """
    serial = models.AutoField(primary_key=True, editable=False)
    date = models.CharField(max_length=200)
    channel = models.CharField(max_length=200)
    network = models.CharField(max_length=200)
    offer_id = models.CharField(max_length=200)
    package_name = models.CharField(max_length=200)
    campaign = models.CharField(max_length=200)
    r_install = models.IntegerField()
    payout = models.FloatField()
    revenue = models.FloatField()
    networkrevenue = models.CharField(max_length=200)

    class Meta:
        db_table = 'revenueReport'


class installReport(models.Model):
    """
    This is the base model for all the models.
    It has all the requried and common fields in our custom models.
    """
    date = models.CharField(max_length=200)
    campaign = models.CharField(max_length=200)
    count = models.IntegerField()

    class Meta:
        db_table = 'install_report'