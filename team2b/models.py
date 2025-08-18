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
    amount = models.FloatField(default=0)    
    order_status = models.CharField(default=0,max_length=100)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    extra_details2 = models.JSONField(default = dict,blank=True, null=True)
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
    state = models.CharField(max_length=20,blank=True)
    is_paid = models.CharField(max_length=20,blank=True)
    age = models.CharField(max_length=20,blank=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    mother_tongue = models.CharField(max_length=20,blank=True)
    
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


class IndigoV3Mining(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='indigomoddteam2modd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    company = models.CharField(default='', blank=True, max_length=100)
    pnr = models.CharField(max_length=20,unique=True)
    email = models.CharField(max_length=100, unique=False)
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

class Ebebekuid(models.Model):

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

class Underarmour(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='underarmourauto')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class UnderarmourOID(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='underarmourauto')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Pinoypeso(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='pinoypesomodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Ohi(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='ohiauto')
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

class Fivepaisa(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='fivepaisamodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Adda(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='adda52tmodd')
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

class AddaOrderId(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='adda52tmodd')
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

class Bambootauto(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='bambootauto')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Paynearby(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='paynearbyauto')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class in2X(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='in2xmodd')
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

class BluerewardsV2(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='bluerewardsauto')
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

class Signnow(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='signnowmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class SixerDream(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='sixerdream11apktmodd')
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

class WesternUnion(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='westernunion')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class StolotoUserId(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='stolototmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class StolotoOrderId(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='stolototmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class PaysettUserId(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='paysettmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class ShopeevnUID(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='shopeevntauto')
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

class ShopeevnOID(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='shopeevntauto')
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


class Poppolive(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='poppolivetmodd')
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

class ShopeemyUID(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='shoppemytauto')
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

class ShopeemyOID(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='shoppemytauto')
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

class Shiprocket(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='shiprocketcouriert')
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

class Novawater(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='novawateriosmodd')
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

class Moglix(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='moglixauto')
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=50,unique=True)    
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    price = models.FloatField(default=0)
    updated_at = models.DateTimeField(auto_now=True)    
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Viu(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='viuhkmodd')
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

class Betr(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='betrmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class ShopeeidUID(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='shopeeno1tauto')
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

class Dupoin(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='dupoin')
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

class ShopeephUID(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='shopeephtauto')
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

class Epikodd(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='epikoddiosmodd')
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

class Stoloto(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='stolototmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    payment_data = models.DateTimeField()
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

class Casinopluss(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='casinoplussmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Storyland(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='storylandappmetrica')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Homiedev(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='homiedevmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class TikettOID(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='tikettmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class ApnaTime(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='apnatimeauto')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class MotiLal(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='motilaloswaltmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Frendipay(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='frendipayautoios')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Magicland(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='magiclandmodd')
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

class FoxtaleOrderId(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='foxtalemodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    id = models.CharField(max_length=50,unique=True)
    price = models.FloatField(default=0)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    extra_details = models.JSONField(default = dict,blank=True, null=True)
    order_placed_date = models.DateTimeField(default=None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Hoteltonight(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='hoteltonightautoios')
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

class stolotoCIF(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='stoloto')
    created_at = models.DateTimeField(auto_now_add=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    id = models.CharField(max_length=50,unique=True)
    payment_date = models.DateTimeField(default=None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Yesmadam(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='yesmadammodd')
    booking_date = models.DateTimeField(default=None,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.FloatField(default=0)
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

class Beymen(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='beymenclubiosauto')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Bncauto(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='bncauto')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Kfcmexico(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='kfcmexicotmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Jazzcash(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='jazzcashmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    channel_list = models.JSONField(default = list,blank=True, null=True)
    network_list = models.JSONField(default = list,blank=True, null=True)
    offer_id_list = models.JSONField(default = list,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Petbook(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='petbookappmetrica')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class tejimaandi(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='tejimaandiauto')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    channel = models.CharField(default='', blank=True, max_length=100)
    network = models.CharField(default='', blank=True, max_length=100)
    offer_id = models.CharField(default='', blank=True, max_length=100)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Tejimaandinew(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='tejimaandiauto')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    channel_list = models.JSONField(default = list,blank=True, null=True)
    network_list = models.JSONField(default = list,blank=True, null=True)
    offer_id_list = models.JSONField(default = list,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]
        
class Paytmmoneyt(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='paytmmoneytmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]


class Anqgoldrewards(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='anqgoldrewardsmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Anqgoldrewardscuid(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='anqgoldrewardsmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Anqgoldrewardsoid(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='anqgoldrewardsmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class OkeyvipMining(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='okeyvipmodd')
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

class Moneymetmodduid(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='moneymetmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Imagineart(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='imaginearttautoios')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]


class Parimatchth(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='parimatchthmodd')
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

class Melive(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='melivemodd')
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

class Metlive(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='metlivemodd')
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

class MeliveUID(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='melivemodd')
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=50,unique=True)
    country =  models.CharField(default='', blank=True, max_length=20) 
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

class MetliveUID(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='metlivemodd')
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=50,unique=True)  
    country =  models.CharField(default='', blank=True, max_length=20)
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

class Opay(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='opaymodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    channel_list = models.JSONField(default = list,blank=True, null=True)
    network_list = models.JSONField(default = list,blank=True, null=True)
    offer_id_list = models.JSONField(default = list,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]


class Bevietnames(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='bevietnamesmodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Boost(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='boostappmyauto')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    phone = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    channel_list = models.JSONField(default = list,blank=True, null=True)
    network_list = models.JSONField(default = list,blank=True, null=True)
    offer_id_list = models.JSONField(default = list,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Cimbthai(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='cimbthaimodd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Myauchan(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='myauchanappmetrica')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class Ikea(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='ikeaauto')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=50,unique=True)
    used_at = models.DateTimeField(default = None,blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

class ShopeebrUID(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='shopeebrtauto')
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


class ShopeethUID(models.Model):

    serial = models.AutoField(primary_key=True, editable=False)
    campaign_name = models.CharField(max_length=20,default='shopeet')
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