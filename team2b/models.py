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
    campaign_name = models.CharField(max_length=20,default='mcdeliverymodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    payment_status = models.CharField(max_length=50,blank=True, null=True)
    payment_mode = models.JSONField(default=dict)
    user_id = models.TextField(default='')
    order_no = models.TextField(default='')
    amount = models.FloatField(default=0)
    payment_order_id = models.CharField(max_length=50, default='')
    order_id = models.CharField(max_length=50, default='')
    payment_method = models.CharField(max_length=50,blank=True, null=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)

    
    class Meta:
        indexes = [
            models.Index(fields=['id'])
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
    spdn = models.CharField(max_length=50,default='',blank=True,)
    order_status = models.CharField(default=0,max_length=100)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    channel_list = models.JSONField(default = list,blank=True, null=True)
    network_list = models.JSONField(default = list,blank=True, null=True)
    offer_id_list = models.JSONField(default = list,blank=True, null=True)
    
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
    campaign_name = models.CharField(max_length=40,default='')
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
    campaign_name = models.CharField(max_length=40,default='')
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

class FantossUserIds(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='fantosst2modd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class OkeyvipUserId(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='okeyvipmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class SephoraOrderId(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='sephoramodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    id = models.CharField(max_length=50,unique=True)
    price = models.CharField(max_length=15)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class SephoraOrderIdV2(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='sephoramodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    channel = models.JSONField(default = list,blank=True, null=True)
    network = models.JSONField(default = list,blank=True, null=True)
    offer_id = models.JSONField(default = list,blank=True, null=True)
    af_prt = models.JSONField(default = list,blank=True, null=True)
    id = models.CharField(max_length=50,unique=True)
    price = models.CharField(max_length=15)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    payment_type = models.TextField()
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]
class PumaOrderId(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='pumaauto')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    id = models.CharField(max_length=50,unique=True)
    price = models.FloatField(default=0)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class TimoclubUserId(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='timoclubmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    id = models.CharField(max_length=70,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]


class EmailIdMining(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='petzeauto')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    id = models.CharField(max_length=200,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]



class IndigoV2Mining(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='indigomoddteam2modd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    company = models.CharField(default='', blank=True, max_length=100)
    pnr = models.CharField(max_length=20,unique=True)
    email = models.CharField(max_length=100, unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    departure_date = models.DateTimeField(blank=False, null=True)
    booking_date = models.DateTimeField(blank=True, null=True)
    fare = models.CharField(default='', blank=True, max_length=40)
    currency = models.CharField(default='', blank=True, max_length=3)

    class Meta:
        indexes = [
            models.Index(fields=['serial']),
            models.Index(fields=['company','departure_date']),
        ]


class RevenueHelper(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=50,default='pepperfryyauto')
    created_at = models.DateTimeField(auto_now_add=True)
    day = models.IntegerField(default='', blank=True, max_length=10)
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


class ScriptChecks(models.Model):

    campaign_name = models.CharField(primary_key=True, max_length=100, editable=True)
    AOV_check = models.BooleanField(default=False)
    ARPU_check = models.BooleanField(default=False)
    event_percent_check = models.BooleanField(default=False)
    
    class Meta:
        indexes = [
            models.Index(fields=['campaign_name']),
        ]

class CountChecks(models.Model):

    campaign_name = models.CharField(primary_key=True, max_length=100, editable=True)
    AOV_check = models.BooleanField(default=False)
    ARPU_check = models.BooleanField(default=False)
    event_percent_check = models.BooleanField(default=False)
    
    class Meta:
        indexes = [
            models.Index(fields=['campaign_name']),
        ]

class ghnUserId(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='ghnmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    id = models.CharField(max_length=70,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class RummytimeUserId(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='rummytimemodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    id = models.CharField(max_length=70,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class ScoreoneUserId(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='scoreone')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    id = models.CharField(max_length=70,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class ApnatimeUserId(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='apnatimeauto')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    id = models.CharField(max_length=70,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class KhiladiaddaUserId(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='khiladiaddamodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    id = models.CharField(max_length=70,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class DatingGlobalUserId(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='datingglobalt2modd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    id = models.CharField(max_length=70,unique=True)
    purchase_status = models.CharField(default='', blank=True, max_length=100)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class DatingGlobalSubscribedUserId(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='datingglobalt2modd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    id = models.CharField(max_length=70,unique=True)
    purchase_status = models.CharField(default='', blank=True, max_length=100)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Bluerewards(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='bluerewardsauto')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Holodilink(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='holodilinkappmetrica')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class RentomojoUserId(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='rentmojomodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    id = models.CharField(max_length=70,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Shahid(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='shahidmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Eztravel(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='eztravel')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Betwinner(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='betwinner')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Ladygentleman(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='ladygentlemanmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Tajrummy(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='tajrummymodd')
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=50,unique=True)    
    updated_at = models.DateTimeField(auto_now=True)    
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Bet22(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='bet22modd')
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=50,unique=True)
    price = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)    
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class PepperFry(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='pepperfryyauto')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Igpmodd(models.Model):

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

class Travelata(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='tajrummymodd')
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=50,unique=True)    
    booking_type = models.CharField(default='', blank=True, max_length=100)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    price = models.FloatField(default=0)
    number = models.CharField(default='', blank=True, max_length=20)
    updated_at = models.DateTimeField(auto_now=True)    
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Ontime(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='tajrummymodd')
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=50,unique=True)    
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)    
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Mcdmodd(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='mcdeliverymodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class tipsAosValid(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='tipstopauto')
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=50,unique=True)    
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)    
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class tipsAosCancelled(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='tipstopauto')
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=50,unique=True)    
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)    
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class tipsIosValid(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='tipsstopautoios')
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=50,unique=True)    
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)    
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class tipsIosCancelled(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='tipstopauto')
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=50,unique=True)    
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)    
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Skyline(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='skylineautoios')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Reserva(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='reservamodd')
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=50,unique=True)    
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    profile_details = models.JSONField(default = dict,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)    
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class GuruShort(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='gurushortmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=50,unique=True)    
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)    
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class GuruShortNotPremium(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='gurushortmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=50,unique=True)    
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)    
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class GuruShortOrderId(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='gurushortmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=50,unique=True)    
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)    
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class GuruShortValidId(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='gurushortmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=50,unique=True)    
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)    
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]


class Credito(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='clickcreditomodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Ajio(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='ajiomodd')
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=50,unique=True)    
    brand = models.CharField(default='', blank=True, max_length=100)
    price = models.FloatField(default=0)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)    
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Jungleepoker(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='jungleepokerauto')
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=50,unique=True)    
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)    
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class GameRummy(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='gamerummyprimemodd')
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=50,unique=True)    
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)    
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Navrang(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='navrangmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=50,unique=True)    
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)    
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Lotter69(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='lotter_69')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Lotter38(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='lotter_38')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class ChaleeSultan(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='chaalesultanauto')
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=50,unique=True)    
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)    
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Ejaby(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='ejabyauto')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Flappdeals(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='flappdealsmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=50,unique=True)    
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)    
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Laundrymate(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='laundrymateauto')
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=50,unique=True)    
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)    
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Parimatch(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='parimatchmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=50,unique=True)    
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)    
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class KisanKonnect(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='kisankonnectmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=50,unique=True)    
    price = models.FloatField(default=0)
    payment_type = models.CharField(default='', blank=True, max_length=100)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)    
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class EpoCosmetic(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='epocosmeticmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=50,unique=True)    
    price = models.FloatField(default=0)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)    
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Ebebek(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='ebebekauto')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]