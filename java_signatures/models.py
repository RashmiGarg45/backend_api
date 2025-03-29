from django.db import models

class RevenueHelper(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=50,default='pepperfryyauto')
    created_at = models.DateTimeField(auto_now_add=True)
    # day = models.IntegerField(default=100, blank=True)
    c_day = models.IntegerField(default=100, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    id = models.CharField(max_length=200, blank=True)
    revenue = models.FloatField(default='', blank=True, max_length=100)
    currency = models.CharField(default='', blank=True, max_length=100)
    adid = models.UUIDField(default='', blank=True)
    event_name = models.CharField(default='', blank=True, max_length=100)
    event_value = models.JSONField(default = dict,blank=True, null=True)
    app_version = models.TextField(blank=True, null=True)
    script_version = models.TextField(blank=True, null=True)    


    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class RevenueHelper(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=50,default='pepperfryyauto')
    created_at = models.DateTimeField(auto_now_add=True)
    # day = models.IntegerField(default=100, blank=True)
    c_day = models.IntegerField(default=100, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    id = models.CharField(max_length=200, blank=True)
    revenue = models.FloatField(default='', blank=True, max_length=100)
    currency = models.CharField(default='', blank=True, max_length=100)
    adid = models.UUIDField(default='', blank=True)
    event_name = models.CharField(default='', blank=True, max_length=100)
    event_value = models.JSONField(default = dict,blank=True, null=True)
    app_version = models.TextField(blank=True, null=True)
    script_version = models.TextField(blank=True, null=True)    


    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class EventInfo(models.Model):
    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=50,default='pepperfryyauto')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    install_date = models.DateField()
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    stats = models.JSONField(default = dict,blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['campaign_name','channel','network','offer_id']),
        ]