from django.db import models

# Create your models here.

class CheckEventCount(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    channel = models.CharField(max_length=100)
    network = models.CharField(max_length=100)
    offer_id = models.CharField(max_length=100)
    install_event = models.IntegerField(default=0)
    open_event = models.IntegerField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=['campaign_name']),
            models.Index(fields=['channel']),
            models.Index(fields=['network']),
            models.Index(fields=['offer_id']),
            models.Index(fields=['channel','network']),
            models.Index(fields=['offer_id','network']),
            models.Index(fields=['offer_id','channel']),
            models.Index(fields=['channel','offer_id','network']),
        ]


class IndigoScriptOrderIds(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=100,default='indigomoddteam2modd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    departure_date = models.DateTimeField(blank=True, null=True)
    booking_date = models.DateTimeField(blank=True, null=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    id = models.CharField(max_length=100,unique=True)
    type = models.CharField(max_length=100)
    extra_details = models.JSONField(default=dict)

    class Meta:
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['created_at'])
        ]

class IgpScriptOrderIds(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=100,default='igpmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    booking_date = models.DateTimeField(default = None,blank=True, null=True)
    delivered_date = models.DateTimeField(default = None,blank=True, null=True)
    id = models.CharField(max_length=100,unique=True)
    type = models.CharField(max_length=100)
    extra_details = models.JSONField(default=dict)

    class Meta:
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['created_at'])
        ]


class McdeliveryScriptOrderIds(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='igpmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    invoice_date_time = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=500,blank=True, null=True)
    gross_amount = models.FloatField(default=0)
    member_name = models.CharField(max_length=100,blank=True, null=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    extra_details = models.JSONField(default=dict)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['invoice_date_time'])
        ]

class LightInTheBox(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='igpmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class DominosIndodeliveryScriptOrderIds(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='igpmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    invoice_date_time = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=500,blank=True, null=True)
    order_status = models.CharField(default=0,max_length=100)
    order_type = models.CharField(default=0,max_length=100)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['invoice_date_time'])
        ]

class OstinShopScriptOrderIds(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='igpmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    order_status = models.CharField(default=0,max_length=100)
    amount = models.CharField(default=0,max_length=100)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]


class HabibScriptOrderIdsConstants(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='igpmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    order_status = models.CharField(default=0,max_length=100)
    amount = models.CharField(default=0,max_length=100)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class WatchoOrderIdsMining(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='igpmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    order_status = models.CharField(default=0,max_length=100)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class DamnrayOrderIds(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='igpmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    products = models.JSONField(default = list,blank=True, null=True)
    payment = models.JSONField(default = dict,blank=True, null=True)
    price = models.CharField(max_length=50)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]


class PepperfryOrderIds(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='pepperfrymodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order_status = models.CharField(default=0,max_length=100)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    used_at_2 = models.DateTimeField(default = None,blank=True, null=True)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]


class MumzworldOrderIds(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='mumzworld')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    order_at = models.DateTimeField(default = None,blank=True, null=True)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class TripsygamesOrderIds(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='tripsygamesmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=15,unique=True)
    order_status = models.CharField(default=0,max_length=10)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class LazuritOrderIds(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='lazuritappmetrica')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=15,unique=True)
    price = models.CharField(max_length=15,unique=True)
    order_status = models.CharField(default=0,max_length=20)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]


class GomcdOrderIds(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='gomcdoauto')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=20,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class BharatmatrimonyUserIds(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='bharatmatrimonymodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=20,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]


class SamsclubMemberIds(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='samsclubmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=25,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]


class IDHelperApps(models.Model):
    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date_added = models.DateField(blank=False)
    type = models.CharField(blank=False,default='order_id',max_length=8)
    description = models.TextField(default='')    
    team = models.CharField(default='',max_length=2)    
    class Meta:
        indexes = [
            models.Index(fields=['serial']),
            models.Index(fields=['campaign_name']),
        ]

class SimulationIds(models.Model):
    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date_added = models.DateField(blank=False)
    timestamp = models.DateTimeField(blank=False)
    type = models.CharField(blank=False,default='order_id',max_length=8)
    id = models.CharField(max_length=100,unique=True)
    constraint = models.FloatField(default=1)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['campaign_name']),
            models.Index(fields=['campaign_name','id','timestamp']),
        ]


class Player6auto(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='player6auto')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    event_token = models.CharField(max_length=30,unique=True)
    event_value = models.JSONField(default=dict, blank=True, null=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    device_data = models.JSONField(default=dict, blank=True, null=True)
    app_data = models.JSONField(default=dict, blank=True, null=True)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['serial']),
        ]



class WeWorldIds(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='weworldauto')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=25,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    
    class Meta:
        db_table = 'team2b_weworlduserids'
        indexes = [
            models.Index(fields=['id']),
        ]
