from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from team2b.models import MumzworldOrderIds,PepperfryOrderIds,SimulationIds,DamnrayOrderIds,IndigoScriptOrderIds,IgpScriptOrderIds,McdeliveryScriptOrderIds,LightInTheBox,DominosIndodeliveryScriptOrderIds,OstinShopScriptOrderIds,HabibScriptOrderIdsConstants,WatchoOrderIdsMining,TripsygamesOrderIds, LazuritOrderIds, GomcdOrderIds, BharatmatrimonyUserIds, SamsclubMemberIds, WeWorldIds, Player6auto, IDHelperApps, FantossUserIds, OkeyvipUserId, SephoraOrderId, PumaOrderId, TimoclubUserId, EmailIdMining, RevenueHelper, IndigoV2Mining, ScriptChecks,SephoraOrderIdV2, ghnUserId, RummytimeUserId, ScoreoneUserId, ApnatimeUserId, KhiladiaddaUserId, DatingGlobalUserId, DatingGlobalSubscribedUserId
from team2b.services.redis import Redis

from datetime import datetime,timedelta,date
import json, time, random
import requests

from django.db.models import Count
from django.db.models import Avg

class GenericScriptFunctions(APIView):
    def get(self, request):
        tablesDict = {
            'mcdeliverymodd':McdeliveryScriptOrderIds,
            'dominosindomodd':DominosIndodeliveryScriptOrderIds,
            'watchomodd':WatchoOrderIdsMining,
            'pepperfrymodd':PepperfryOrderIds,
            # 'habibmodd':HabibScriptOrderIdsConstants,
            # 'tripsygamesmodd': TripsygamesOrderIds,
            # 'ostinshopmodd': OstinShopScriptOrderIds,
            # 'lazuritappmetrica': LazuritOrderIds,
            # 'gomcdoauto': GomcdOrderIds,
            # 'bharatmatrimonymodd': BharatmatrimonyUserIds,
            # 'weworldauto': WeWorldIds,
            # 'fantosst2modd': FantossUserIds,
            # 'okeyvipmodd': OkeyvipUserId,
            'scoreone': ScoreoneUserId,
            'ghnmodd': ghnUserId,
            # 'rummytimemodd': RummytimeUserId,
            'sephoramodd': SephoraOrderIdV2,
            'pumaauto': PumaOrderId, 
            'timoclubauto': TimoclubUserId,
            'apnatimeauto': ApnatimeUserId,
            'khiladiaddamodd': KhiladiaddaUserId,
            'datingglobalt2modd': DatingGlobalUserId,
            'Subs_datingglobalt2modd': DatingGlobalSubscribedUserId,
            'indigomoddteam2modd': IndigoV2Mining,
            # 'samsclubmodd': SamsclubMemberIds,
            # 'mumzworldautoios':MumzworldOrderIds,
            'damnraymodd':DamnrayOrderIds,
            # 'indigomodd':IndigoScriptOrdersIds,
            # 'lightinthebox':LightInTheBox,
        }
        today = datetime.now().strftime('%Y-%m-%d')
        ids_mined = {}
        for key,value in tablesDict.items():
            ids_mined[key] = tablesDict[key].objects.filter(created_at__gte=str(today),created_at__lte=str(today+" 23:59:59")).count()

        from data_tracking.util import googleChatBot_send_message
        space_name = "AAAAh8zMzAw"
        message = {
                        "cardsV2": [
                            {
                                "cardId": "reminderCard",
                                "card": {
                                        "header": {
                                            "title": "Order/User Ids Mined Today",
                                        },
                                        "sections": [
                                            {
                                            "header": "",
                                            "collapsible": False,
                                            "uncollapsibleWidgetsCount": 1,
                                            "widgets": [
                                            ]
                                            }
                                        ]
                                    },
                            },
                        ]
                }

        widgets = []
        for sciptname,mined_num in ids_mined.items():
            widgets.append({
                            "columns": {
                                "columnItems": [
                                                    {
                                                        "horizontalSizeStyle": "FILL_AVAILABLE_SPACE",
                                                        "horizontalAlignment": "CENTER",
                                                        "verticalAlignment": "CENTER",
                                                        "widgets": [{
                                                                        "decoratedText": {
                                                                            "text": sciptname,
                                                                        }
                                                                    }]
                                                    },
                                                    {
                                                        "widgets": [{
                                                                    "decoratedText": {
                                                                        "text": str(mined_num),
                                                                    }
                                                                    }]
                                                    }
                                ]
                            }
                        })
        message['cardsV2'][0]['card']['sections'][0]['widgets'] = widgets
        # print(json.dumps(message['cardsV2'][0]['card'],indent=4))
        googleChatBot_send_message(space_name=space_name,message=message)    
        googleChatBot_send_message(space_name='AAAA7sIzS9Q',message=message)    

        return Response({
            'ids_mined':ids_mined,
        })


class GenericUnusedIdScriptFunctions(APIView):
    def get(self, request):
        tablesDict = {
            'mcdeliverymodd':McdeliveryScriptOrderIds,
            'dominosindomodd':DominosIndodeliveryScriptOrderIds,
            'pepperfrymodd':PepperfryOrderIds,
            # 'habibmodd':HabibScriptOrderIdsConstants,
            # 'tripsygamesmodd': TripsygamesOrderIds,
            # 'ostinshopmodd': OstinShopScriptOrderIds,
            # 'lazuritappmetrica': LazuritOrderIds,
            # 'gomcdoauto': GomcdOrderIds,
            'scoreone': ScoreoneUserId,
            'ghnmodd': ghnUserId,
            # 'rummytimemodd': RummytimeUserId,
            # 'bharatmatrimonymodd': BharatmatrimonyUserIds,
            # 'weworldauto': WeWorldIds,
            # 'fantosst2modd': FantossUserIds,
            # 'okeyvipmodd': OkeyvipUserId,
            'sephoramodd': SephoraOrderIdV2,
            'pumaauto': PumaOrderId,
            'timoclubauto': TimoclubUserId,
            'apnatimeauto': ApnatimeUserId,
            'khiladiaddamodd': KhiladiaddaUserId,
            'datingglobalt2modd': DatingGlobalUserId,
            'Subs_datingglobalt2modd': DatingGlobalSubscribedUserId,
            'indigomoddteam2modd': IndigoV2Mining,
            # 'emailIds_Mined': EmailIdMining

            # 'samsclubmodd': SamsclubMemberIds,
            # 'mumzworldautoios':MumzworldOrderIds,
            'damnraymodd':DamnrayOrderIds,
            # 'indigomodd':IndigoScriptOrdersIds,
            # 'lightinthebox':LightInTheBox,
        }
        ids_mined = {}
        for key in tablesDict.keys():
            ids_mined[key] = tablesDict[key].objects.filter(used_at = None).count()

        from data_tracking.util import googleChatBot_send_message
        space_name = "AAAAh8zMzAw"
        message = {
                        "cardsV2": [
                            {
                                "cardId": "reminderCard",
                                "card": {
                                        "header": {
                                            "title": "Remaining Order/User Ids In Database",
                                        },
                                        "sections": [
                                            {
                                            "header": "",
                                            "collapsible": False,
                                            "uncollapsibleWidgetsCount": 1,
                                            "widgets": [
                                            ]
                                            }
                                        ]
                                    },
                            },
                        ]
                }

        widgets = []
        for sciptname,mined_num in ids_mined.items():
            widgets.append({
                            "columns": {
                                "columnItems": [
                                                    {
                                                        "horizontalSizeStyle": "FILL_AVAILABLE_SPACE",
                                                        "horizontalAlignment": "CENTER",
                                                        "verticalAlignment": "CENTER",
                                                        "widgets": [{
                                                                        "decoratedText": {
                                                                            "text": sciptname,
                                                                        }
                                                                    }]
                                                    },
                                                    {
                                                        "widgets": [{
                                                                    "decoratedText": {
                                                                        "text": str(mined_num),
                                                                    }
                                                                    }]
                                                    }
                                ]
                            }
                        })
        message['cardsV2'][0]['card']['sections'][0]['widgets'] = widgets

        googleChatBot_send_message(space_name=space_name,message=message)    
        googleChatBot_send_message(space_name='AAAA7sIzS9Q',message=message)    

        return Response({
            'ids_mined':ids_mined,
        })


def id_helper_function(id_helper_data,constant_timestamp=None,constraint=1):
    user_id_increase_per_second_list = []
    for i in range(len(id_helper_data)):
        if i == 0 and len(id_helper_data)!=2:
            constraint = id_helper_data[i].get('constraint')
            continue
        if i+1!=len(id_helper_data):
            timestamp_diff = id_helper_data[i].get('timestamp') - id_helper_data[i+1].get('timestamp')
            user_id_diff = id_helper_data[i].get('id') - id_helper_data[i+1].get('id')

            user_id_increase_per_second = float(user_id_diff)/float(timestamp_diff)
            user_id_increase_per_second_list.append(user_id_increase_per_second)

    print('[+] User ID per second : {}'.format(user_id_increase_per_second))

    current_time = constant_timestamp if constant_timestamp else time.time()
    last_ordered_item = id_helper_data[1]
    time_diff = current_time - last_ordered_item.get('timestamp')
    avg_ord_id_increase = (sum(user_id_increase_per_second_list)/len(user_id_increase_per_second_list))*constraint
    trans_id = (time_diff*avg_ord_id_increase)+last_ordered_item.get('id')

    return int(trans_id)

class SimulatedIdFunction(APIView):
    def put(self, request):
        put_query = SimulationIds()
        scriptname = request.data.get('campaign_name')
        type = request.data.get('type','order_id')
        for item in ['campaign_name','type','timestamp','id','date_added']:
            if not request.data.get(item):
                raise ValidationError({
                    'error':item+' was not provided.'
                })
        search_query = SimulationIds.objects.filter(campaign_name=request.data.get('campaign_name'),type=type).order_by('-timestamp').first()
        if search_query:
            # if int(search_query.id)>=request.data.get('id'):
            #     raise ValidationError({
            #         'error':'ID provided is old, we have a newer id than this in our DB, and cannot be simulated'
            #     })
            
            if datetime.strptime(search_query.timestamp.strftime("%Y-%m-%d %H:%M:%S"),"%Y-%m-%d %H:%M:%S")>datetime.strptime(request.data.get('timestamp'),"%Y-%m-%d %H:%M:%S"):
                raise ValidationError({
                    'error':'Timestamp provided is old, we have a newer timestamp than this in our DB'
                })

        put_query.campaign_name = request.data.get('campaign_name')
        put_query.timestamp = request.data.get('timestamp')
        put_query.id=request.data.get('id')
        put_query.type=request.data.get('type','order_id')
        put_query.date_added = request.data.get('date_added')
        put_query.constraint = request.data.get('constraint',1)
        put_query.save()
        
        redis_obj = Redis()
        search_query = SimulationIds.objects.filter(campaign_name=scriptname,type=type).order_by('-timestamp')
        data_list = []
        for item in search_query:
            data_list.append({
                'timestamp':item.timestamp.timestamp(),
                'id':int(item.id),
                'constraint':item.constraint
            })
        redis_obj.delete(key=(scriptname+'_'+type+'_'+'last_used_id'))
        redis_obj.save(key=scriptname+'_'+type,value=data_list)

        return Response({
            'message':'Updated'
        })

    def get(self, request):
        scriptname = request.GET.get('scriptname')
        type = request.GET.get('type','order_id')

        redis_obj = Redis()
        data_list = redis_obj.retrieve_data(key=scriptname+'_'+type)

        if not data_list:
            print('Did not got id from redis')
            search_query = SimulationIds.objects.filter(campaign_name=scriptname,type=type).order_by('-timestamp')
            data_list = []
            for item in search_query:
                data_list.append({
                    'timestamp':item.timestamp.timestamp(),
                    'id':int(item.id),
                    'constraint':item.constraint
                })
            redis_obj.save(key=scriptname+'_'+type,value=data_list)
        
        if len(data_list)>=2:
            id_gen = id_helper_function(data_list,time.time())
            last_id_used_dict = redis_obj.retrieve_data(scriptname+'_'+type+'_'+'last_used_id')
            if last_id_used_dict:
                last_id_used = last_id_used_dict.get('id_gen')
                if last_id_used:
                    while last_id_used>=id_gen:
                        id_gen = id_gen+1
                else:
                    pass

            redis_obj.save(key=scriptname+'_'+type+'_'+'last_used_id',value={"id_gen":id_gen,"ts":time.time()})
            return Response({
                'id_gen':id_gen,
            })
        else:
            raise ValidationError({
                'error':'Need 2 rows for id simulation'
            })
        
class AppsForSimulation(APIView):
    def get(self, request):
        url = "http://info.appsuccessor.com/devteamnumbers.php?secret=b0a492d6271466cb71e9ab53982ddd1d&team=team2&datefrom={}&dateto={}".format(date.today(),date.today())
        today_r6_data = requests.get(url).json()
        apps_list_query = IDHelperApps.objects.all()
        apps_list_dict = {}
        for item in apps_list_query:
            apps_list_dict[item.campaign_name+"_"+item.type] = {"description":item.description,"type":item.type}

        apps_list = apps_list_dict.keys()

        data = {}

        redis_obj = Redis()

        data_list = []

        for app_item in apps_list:
            dict__ = {}
            app = app_item.split('_')[0]
            type = app_item.split('_',1)[1]
            dict__.update(apps_list_dict.get(app_item))
            dict__['script_name'] = app
            dict__['status'] = 'Needs Update'

            data[app] = {}

            if today_r6_data.get(app,{}).get(str(date.today()),{}).get('i2'):
                data[app] = {}
                dict__['i2'] = today_r6_data.get(app,{}).get(str(date.today()),{}).get('i2')
            
            key = app +'_'+type
            if redis_obj.retrieve_data(key=key):
                data[app].update({'data_list':redis_obj.retrieve_data(key=key)})
                dict__['data_list'] = redis_obj.retrieve_data(key=key)
                dict__['last_updated_id'] = data.get(app).get('data_list')[0].get('id')
                dict__['last_updated_id_timestamp'] = data.get(app).get('data_list')[0].get('timestamp')
                if datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d') == datetime.fromtimestamp(int(dict__['last_updated_id_timestamp'])).strftime('%Y-%m-%d'):
                    dict__['status'] = 'Updated'                    

            if redis_obj.retrieve_data(key=key+'_'+'last_used_id'):
                data[app].update({'last_used_dict':redis_obj.retrieve_data(key=key+'_'+'last_used_id')})
                dict__['last_used_id'] = data.get(app).get('last_used_dict').get('id_gen')
                dict__['last_used_id_timestamp'] = data.get(app).get('last_used_dict').get('ts')
            data_list.append(dict__)
        return Response({
            'data':data_list
            })
    
    def put(self, request):
        campaign_name = request.data.get('campaign_name')
        date_added = date.today()
        description = request.data.get('description','')
        type=request.data.get('type')
        data = request.data.get('data')
        
        qq = IDHelperApps.objects.filter(campaign_name=campaign_name,type=type).first()
        if qq:
            return Response({
                'message':'Already Present, please update id.'
                })
        dd = {
            "campaign_name":campaign_name,
            "date_added":date_added,
            "description":description,
            "type":type
        }
        id_helper_app = IDHelperApps.objects.create(**dd)

        # data.reverse()
        for item in data:
            tt = int(item.get('timestamp'))
            ii = int(item.get('id'))
            datadd = {
                "constraint":1,
                "campaign_name":campaign_name,
                "timestamp":datetime.fromtimestamp(tt).strftime('%Y-%m-%d %H:%M:%S.000000'),
                "id":ii,
                "date_added":datetime.fromtimestamp(tt).strftime('%Y-%m-%d'),
                "type":type
            }
            print(requests.put("http://localhost:8000/team2b/idsimulated",json=datadd))

        return Response({
            'message':'Successfully stored the app.'
            })
    
class Indigo(APIView):
    def put(self, request):
        query = IndigoScriptOrderIds()
        query.campaign_name = request.data.get('camp_name','indigomoddteam2modd')
        query.id = request.data.get('pnr')
        query.type = request.data.get('id_type','pnr')
        query.departure_date=request.data.get('departure_date')
        query.booking_date=request.data.get('booking_date')
        query.used_at = None
        query.extra_details = request.data.get('other_details','{}')
        query.save()
        return Response({
        })

    def get(self, request):
        departure_date=datetime.now().strftime('%Y-%m-%d')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        pnr_used = IndigoScriptOrderIds.objects.filter(used_at__contains=str(departure_date)).aggregate(Count('used_at'))
        if pnr_used:
            pnr_used = pnr_used.get('used_at__count')

        data = {}
        if pnr_used<=100:
            query = IndigoScriptOrderIds.objects.filter(used_at=None).first()
            print(query)
            if query:
                extra_details = query.extra_details
                
                data = {
                        "booking_date": query.booking_date, 
                        "usedAt": query.used_at, 
                        "departure_date": query.departure_date.strftime('%Y-%m-%d %H:%M:%S'), 
                        "transaction_id": extra_details.get('transaction_id'),#[{"value": "113097902036", "key": "ReferenceNo"}], 
                        "email": extra_details.get('email'),#"nrd981@gmail.com", 
                        "flight_reference": extra_details.get('flight_reference'),#"20231227 6E5265 GWLBOM", 
                        "departure_city": extra_details.get('departure_city'),#"GWL", 
                        "pnr": query.id, 
                        "fare": extra_details.get('fare'),#"6031.0", 
                        "company": extra_details.get('company'),#null, 
                        "arrival_date": extra_details.get('arrival_date'),#"2023-12-27T16:15:00", 
                        "used": True if query.used_at else False,#false, 
                        "arrival_city": extra_details.get('arrival_city'),#"BOM", 
                        "pushed_at": query.created_at
                }
                if setUsed:
                    query = IndigoScriptOrderIds.objects.filter(id=data.get('pnr')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
            'pnr_used':pnr_used+1
        })

    def post(self, request):
        set_used = request.data.get('used')
        pnr = request.data.get('pnr')
        channel = request.data.get('channel')
        offer_id = request.data.get('offer_id')
        network_name = request.data.get('network_name')
        if set_used:
            query = IndigoScriptOrderIds.objects.filter(id=pnr).first()
            custom_text = query.extra_details
            custom_text.update({
                'channel':channel,
                'offer_id':offer_id,
                'network_name':network_name,
            })
            IndigoScriptOrderIds.objects.filter(id=pnr).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),extra_details=custom_text)
        else:
            query = IndigoScriptOrderIds.objects.filter(id=pnr).update(used_at=None)
        return Response({
            'used':set_used,
            'pnr':pnr
        })

class IGP(APIView):
    def put(self, request):
        query = IgpScriptOrderIds()
        query.campaign_name = request.GET.get('camp_name','igpmodd')
        query.id = request.GET.get('id')
        query.type = request.GET.get('id_type','order_id')
        if request.GET.get('delivered_date'):
            query.delivered_date=datetime.strptime(request.GET.get('delivered_date'),'%Y-%m-%d %H:%M:%S')
        query.booking_date=datetime.strptime(request.GET.get('booking_date'),'%Y-%m-%d %H:%M:%S')
        query.used_at = None
        query.extra_details = request.GET.get('other_details','{}')
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used')
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        query = IgpScriptOrderIds.objects.filter(used_at=None).order_by('-delivered_date').first()
        data = {
            'id':query.id,
            'extra_details':query.extra_details,
            'booking_date':query.booking_date,
            'delivered_date':query.delivered_date
        }
        if setUsed:
            query = IgpScriptOrderIds.objects.filter(id=data.get('id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'data':data
        })
        

    def post(self, request):
        query = IgpScriptOrderIds.objects.filter(id=request.GET.get('id'))
        if query:
            query.used_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            query.save()
        return Response({
        })

class Mcdelivery(APIView):
    def put(self, request):
        query = McdeliveryScriptOrderIds()
        query.campaign_name = request.data.get('camp_name','mcdeliverymodd')
        query.id = request.data.get('id')
        query.amount = request.data.get('amount')
        query.payment_mode = request.data.get('payment_mode',{})
        query.order_id=request.data.get('order_id')
        query.order_no=request.data.get('order_no')
        query.payment_method=request.data.get('payment_method')
        query.payment_order_id = request.data.get('payment_order_id')
        query.payment_status = request.data.get('payment_status')
        query.user_id = request.data.get('user_id')
        query.used_at = None
        try:
            query.save()
            return Response({
            })
        except:
            return Response({
            })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = McdeliveryScriptOrderIds.objects.filter(used_at=None).order_by('-created_at').first()
        
        data = {
                'id': query.id,
                'amount': query.amount,
                'payment_mode':query.payment_mode,
                'order_id':query.order_id,
                'order_no':query.order_no,
                'payment_method':query.payment_method,
                'payment_order_id':query.payment_order_id,
                'payment_status':query.payment_status,
                'user_id': query.user_id,
                'used_at':query.used_at,
                
        }
        if setUsed:
            query = McdeliveryScriptOrderIds.objects.filter(id=data.get('id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })

class LightInTheBoxAPI(APIView):
    def put(self, request):
        query = LightInTheBox()
        query.campaign_name = request.data.get('camp_name','lightintheboxmodd')
        query.id = request.data.get('order_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = LightInTheBox.objects.filter(used_at=None).order_by('-created_at').first()
        
        data = {
                'order_id':query.id,
        }
        if setUsed:
            query = LightInTheBox.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })


class DominosIndo(APIView):
    def put(self, request):
        query = DominosIndodeliveryScriptOrderIds()
        query.campaign_name = request.data.get('camp_name','dominosindoauto')
        query.id = request.data.get('order_id')
        query.invoice_date_time = request.data.get('order_date_time')
        query.address=request.data.get('address')
        query.order_type=request.data.get('order_type')
        query.order_status=request.data.get('order_status')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        order_type = request.GET.get('order_type')
        order_status = request.GET.get('order_status')
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        filter_dict = {}
        if order_type:
            filter_dict['order_type'] = order_type
        if order_status:
            filter_dict['order_status'] = order_status
        query = DominosIndodeliveryScriptOrderIds.objects.filter(used_at=None,**filter_dict).order_by('-invoice_date_time')[0:50].all()
        query = random.choice(query)
        
        data = {
                'order_id':query.id,
                'invoice_date':query.invoice_date_time.strftime('%Y-%m-%d %H:%M:%S'),
                'address':query.address,
                'order_status':query.order_status,
                'order_type':query.order_type,
                'used_at':query.used_at,
        }
        if setUsed:
            query = DominosIndodeliveryScriptOrderIds.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })



class OstinShop(APIView):
    def put(self, request):
        query = OstinShopScriptOrderIds()
        query.campaign_name = request.data.get('camp_name','ostinshopmodd')
        query.id = request.data.get('order_id')
        query.amount=request.data.get('amount')
        query.order_status=request.data.get('order_status')
        query.extra_details=request.data.get('extra_details',{})
        query.used_at = None
        try:
            query.save()
            return Response({
            })
        except:
            return Response({
            })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        order_status = request.GET.get('order_status')
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        filter_dict = {}
        if order_status:
            filter_dict['order_status'] = order_status
        query = OstinShopScriptOrderIds.objects.filter(used_at=None,**filter_dict).order_by('-created_at')[0:50].first()
        
        data = {
                'order_id':query.id,
                'order_status':query.order_status,
                'used_at':query.used_at,
                'extra_details':query.extra_details
        }
        if setUsed:
            query = OstinShopScriptOrderIds.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })

class HabibOrderIdConstants(APIView):
    def put(self, request):
        query = HabibScriptOrderIdsConstants()
        query.campaign_name = request.data.get('camp_name','ostinshopmodd')
        query.id = request.data.get('order_id')
        query.amount=request.data.get('amount')
        query.order_status=request.data.get('order_status')
        query.extra_details=request.data.get('extra_details',{})
        query.used_at = None
        try:
            query.save()
            return Response({
            })
        except:
            return Response({
            })
        
    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        order_status = request.GET.get('order_status')
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        filter_dict = {}
        if request.GET.get('old_ids'):
            filter_dict['created_at__lte'] = '2024-02-10'

        if order_status:
            filter_dict['order_status'] = order_status
        query = HabibScriptOrderIdsConstants.objects.filter(used_at=None,**filter_dict).order_by('-created_at')[0:50].first()
        
        data = {
                'order_id':query.id,
                'order_status':query.order_status,
                'used_at':query.used_at,
                'extra_details':query.extra_details
        }
        if setUsed:
            query = HabibScriptOrderIdsConstants.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })

class DamnRayMiningAPI(APIView):
    def put(self, request):
        query = DamnrayOrderIds()
        query.campaign_name = request.data.get('camp_name','damnray')
        query.id = request.data.get('order_id')
        query.products = request.data.get('products')
        query.payment = request.data.get('payment')
        query.price = request.data.get('price')
        query.extra_details=request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        order_status = request.GET.get('order_status')
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        filter_dict = {}
        if order_status:
            filter_dict['order_status'] = order_status
        query = DamnrayOrderIds.objects.filter(used_at=None,**filter_dict).order_by('-created_at')[0:50].first()
        
        data = {
                'order_id':query.id,
                'order_status':query.order_status,
                'used_at':query.used_at,
                'products':query.products,
                'payment':query.payment,
                'price':query.price,
                'extra_details':query.extra_details,
        }
        if setUsed:
            query = DamnrayOrderIds.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })


class WatchoOrderIdsMiningAPI(APIView):
    def put(self, request):
        query = WatchoOrderIdsMining()
        query.campaign_name = request.data.get('camp_name','watchomodd')
        query.id = request.data.get('order_id')
        query.order_status=request.data.get('order_status')
        query.extra_details=request.data.get('extra_details',{})
        query.used_at = None
        try:
            query.save()
            return Response({
            })
        except:
            return Response({
            })
        
    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        order_status = request.GET.get('order_status')
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        filter_dict = {}
        if order_status:
            filter_dict['order_status'] = order_status
        query = WatchoOrderIdsMining.objects.filter(used_at=None,**filter_dict).order_by('-created_at')[0:50].first()
        
        data = {
                'order_id':query.id,
                'order_status':query.order_status,
                'used_at':query.used_at,
                'extra_details':query.extra_details
        }
        if setUsed:
            query = WatchoOrderIdsMining.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })

class WatchoOrderIdsMiningAPIV2(APIView):
    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        channel = request.GET.get('channel',True)
        network = request.GET.get('network',True)
        offer_id = request.GET.get('offer_id',True)
        
        if not channel or not network or not offer_id:
            return Response({
                        'body':'error',
                        'message':'channel,offer_id,network id missing.'
                    })
        
        order_status = request.GET.get('order_status')
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        filter_dict = {}
        if order_status:
            filter_dict['order_status'] = order_status
        filter_dict['created_at__gte'] = date.today()
        
        exclude_dict = {}
        exclude_dict['channel_list__contains'] = channel
        exclude_dict['network_list__contains'] = network
        exclude_dict['offer_id_list__contains'] = offer_id

        query_list = WatchoOrderIdsMining.objects.filter(used_at=None,**filter_dict).order_by('-created_at')[0:25].all()
        if not query_list:
            query_list = WatchoOrderIdsMining.objects.filter(**filter_dict).exclude(**exclude_dict).order_by('-created_at')[0:25].all()
        
        if query_list:
            for i in range(3):
                query = random.choice(query_list)

                if not query.channel_list:
                    new_channel_list = [channel]
                else:
                    if channel in query.channel_list:
                        continue
                    new_channel_list = query.channel_list
                    new_channel_list.append(channel)

                if not query.network_list:
                    new_network_list = [network]
                else:
                    if network in query.network_list:
                        continue
                    new_network_list = query.network_list
                    new_network_list.append(network)

                if not query.offer_id_list:
                    new_offer_id_list = [offer_id]
                else:
                    if offer_id in query.offer_id_list:
                        continue
                    new_offer_id_list = query.offer_id_list
                    new_offer_id_list.append(offer_id)

                data = {
                        'order_id':query.id,
                        'order_status':query.order_status,
                        'used_at':query.used_at,
                        'extra_details':query.extra_details
                }
                if setUsed:
                    query = WatchoOrderIdsMining.objects.filter(id=data.get('order_id')).update(
                        used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        channel_list=new_channel_list,
                        network_list=new_network_list,
                        offer_id_list=new_offer_id_list,
                        )
                return Response({
                    'body':data,
                })

        return Response({
            'body':'error',
            'message':'no id found'
        })


class DamnRayMiningAPI(APIView):
    def put(self, request):
        query = DamnrayOrderIds()
        query.campaign_name = request.data.get('camp_name','damnray')
        query.id = request.data.get('order_id')
        query.products = request.data.get('products')
        query.payment = request.data.get('payment')
        query.price = request.data.get('price')
        query.extra_details=request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        order_status = request.GET.get('order_status')
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        filter_dict = {}
        if order_status:
            filter_dict['order_status'] = order_status
        query = DamnrayOrderIds.objects.filter(used_at=None,**filter_dict).order_by('-created_at')[0:50].first()
        
        data = {
                'order_id':query.id,
                'used_at':query.used_at,
                'products':query.products,
                'payment':query.payment,
                'price':query.price,
                'extra_details':query.extra_details,
        }
        if setUsed:
            query = DamnrayOrderIds.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })



class PepperfryMiningAPI(APIView):
    def put(self, request):
        query = PepperfryOrderIds()
        query.campaign_name = request.data.get('camp_name','pepperfrymodd')
        query.id = request.data.get('order_id')
        query.order_status=request.data.get('order_status')
        query.extra_details=request.data.get('extra_details',{})
        query.used_at = None
        try:
            query.save()
            return Response({
            })
        except:
            return Response({
            })

    def get(self, request):
        try:
            channel = request.GET.get('channel', '')
            network = request.GET.get('network', '')
            offer_id = request.GET.get('offer_id', '')
            setUsed = request.GET.get('set_used',True)
            order_status = request.GET.get('order_status')

            try:
                if int(offer_id):
                    panel_offer = True
            except:
                panel_offer = False

            if panel_offer or (not channel and not network and not offer_id):
                query = PepperfryOrderIds.objects.exclude(used_at=None).order_by('-created_at')[0:500].all()
                
                if query:
                    query = random.choice(query)
                    data = {
                        'order_id':query.id,
                        'order_status':query.order_status,
                        'used_at':query.used_at,
                        'extra_details':query.extra_details
                    }
                    return Response({
                        'body':data,
                        'set_used':False
                    })
                else:
                    return Response({
                        'body':{},
                        'set_used':False
                    })
                
            if setUsed and (setUsed == 'False' or setUsed == 'false'):
                setUsed = False
            
            filter_dict = {}
            if order_status:
                filter_dict['order_status'] = order_status
            query = PepperfryOrderIds.objects.filter(used_at=None,**filter_dict).order_by('-created_at')[0:50].first()
            if query:
                data = {
                        'order_id':query.id,
                        'order_status':query.order_status,
                        'used_at':query.used_at,
                        'extra_details':query.extra_details
                }
                if setUsed:
                    query = PepperfryOrderIds.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
                return Response({
                    'body':data,
                })
            else:
                filter_dict.update({"used_at__lte":datetime.now()-timedelta(days=14)})
                if channel and offer_id and network:
                    exclude_dict = {
                        'channel':channel,
                        'network':network,
                        'offer_id':offer_id,
                    }
                else:
                    exclude_dict = {}
                query = PepperfryOrderIds.objects.filter(used_at_2=None,**filter_dict).exclude(**exclude_dict).order_by('-created_at')[0:50].all()
                query = random.choice(query)
                data = {
                        'order_id':query.id,
                        'order_status':query.order_status,
                        'used_at':query.used_at,
                        'extra_details':query.extra_details
                }
                if setUsed:
                    query = PepperfryOrderIds.objects.filter(id=data.get('order_id')).update(used_at_2=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                return Response({
                    'body':data,
                })
        except:
            return Response({
            })

class MumzworldAPI(APIView):
    def put(self, request):
        query = MumzworldOrderIds()
        query.campaign_name = request.data.get('camp_name','mumzworld')
        query.id = request.data.get('order_id')
        query.order_at = request.data.get('order_at')
        query.extra_details=request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        filter_dict = {}
        query = MumzworldOrderIds.objects.filter(used_at=None,**filter_dict).order_by('-order_at')[0:50].first()
        
        data = {
                'order_id':query.id,
                'used_at':query.used_at,
                'extra_details':query.extra_details
        }
        if setUsed:
            query = MumzworldOrderIds.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })

class TripsygamesAPI(APIView):
    def put(self, request):
        query = TripsygamesOrderIds()
        query.campaign_name = request.data.get('camp_name','tripsygamesmodd')
        query.id = request.data.get('order_id')
        query.order_status = request.data.get('order_status')
        query.extra_details=request.data.get('extra_details',{})
        query.used_at = None
        try:
            query.save()
            return Response({
            })
        except:
            return Response({
            })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        filter_dict = {}
        query = TripsygamesOrderIds.objects.filter(used_at=None,**filter_dict).order_by('-created_at')[0:50].first()
        
        data = {
                'order_id':query.id,
                'used_at':query.used_at,
                'extra_details':query.extra_details
        }
        if setUsed:
            query = TripsygamesOrderIds.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })


class LazuritAPI(APIView):
    def put(self, request):
        query = LazuritOrderIds()
        query.campaign_name = request.data.get('camp_name','lazuritappmetrica')
        query.id = request.data.get('order_id')
        query.price = request.data.get('amount')
        query.order_status = request.data.get('order_status')
        query.extra_details=request.data.get('extra_details',{})
        query.used_at = None
        try:
            query.save()
            return Response({
            })
        except:
            return Response({
            })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        filter_dict = {}
        query = LazuritOrderIds.objects.filter(used_at=None,**filter_dict).order_by('-created_at')[0:50].first()
        
        data = {
                'order_id':query.id,
                'price': query.price,
                'order_status':query.order_status,
                'used_at':query.used_at,
                'extra_details':query.extra_details
        }
        if setUsed:
            query = LazuritOrderIds.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })

class GomcdAPI(APIView):
    def put(self, request):
        query = GomcdOrderIds()
        query.campaign_name = request.data.get('camp_name','gomcdoauto')
        query.id = request.data.get('user_id')
        query.extra_details=request.data.get('extra_details',{})
        query.used_at = None
        try:
            query.save()
            return Response({
            })
        except Exception as e:
            import traceback
            traceback.print_exc()
            return Response({
            })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        filter_dict = {}
        query = GomcdOrderIds.objects.filter(used_at=None,**filter_dict).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'used_at':query.used_at,
                'extra_details':query.extra_details
        }
        if setUsed:
            query = GomcdOrderIds.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })

class BharatmatrimonyAPI(APIView):
    def put(self, request):
        query = BharatmatrimonyUserIds()
        query.campaign_name = request.data.get('camp_name','bharatmatrimonymodd')
        query.id = request.data.get('user_id')
        query.extra_details=request.data.get('extra_details',{})
        query.used_at = None
        try:
            query.save()
            return Response({
            })
        except Exception as e:
            import traceback
            traceback.print_exc()
            return Response({
            })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        filter_dict = {}
        query = BharatmatrimonyUserIds.objects.filter(used_at=None,**filter_dict).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'used_at':query.used_at,
                'extra_details':query.extra_details
        }
        if setUsed:
            query = BharatmatrimonyUserIds.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })

class SamsclubAPI(APIView):
    def put(self, request):
        query = SamsclubMemberIds()
        query.campaign_name = request.data.get('camp_name','samsclubmodd')
        query.id = request.data.get('id')
        query.extra_details=request.data.get('extra_details',{})
        query.used_at = None
        try:
            query.save()
            return Response({
            })
        except Exception as e:
            import traceback
            traceback.print_exc()
            return Response({
            })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        filter_dict = {}
        query = SamsclubMemberIds.objects.filter(used_at=None,**filter_dict).order_by('-created_at')[0:50].first()
        
        data = {
                'id':query.id,
                'used_at':query.used_at,
                'extra_details':query.extra_details
        }
        if setUsed:
            query = SamsclubMemberIds.objects.filter(id=data.get('id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })


class WeWorldAPI(APIView):
    def put(self, request):
        query = WeWorldIds()
        query.campaign_name = request.data.get('camp_name','weworldauto')
        query.id = request.data.get('id')
        query.extra_details=request.data.get('extra_details',{})
        query.used_at = None
        try:
            query.save()
            return Response({
            })
        except Exception as e:
            import traceback
            traceback.print_exc()
            return Response({
            })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        filter_dict = {}
        query = WeWorldIds.objects.filter(used_at=None,**filter_dict).order_by('-created_at')[0:50].first()
        
        data = {
                'id':query.id,
                'used_at':query.used_at,
                'extra_details':query.extra_details
        }
        if setUsed:
            query = WeWorldIds.objects.filter(id=data.get('id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })

class Player6API(APIView):
    def put(self, request):
        query = Player6auto()
        query.campaign_name = request.data.get('camp_name','player6auto')
        query.event_token = request.data.get('event_token')
        query.event_value = request.data.get('event_value')
        query.app_data = request.data.get('app_data')
        query.device_data = request.data.get('device_data')
        query.extra_details=request.data.get('extra_details',{})
        query.used_at = None
        try:
            query.save()
            return Response({
            })
        except Exception as e:
            import traceback
            traceback.print_exc()
            return Response({
            })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        filter_dict = {}
        query = Player6auto.objects.filter(used_at=None,**filter_dict).order_by('-created_at')[0:50].first()
        
        data = {
                'event_token':query.event_token,
                'event_value':query.event_value,
                'device_data':query.device_data,
                'app_data':query.app_data,
                'used_at':query.used_at,
                'extra_details':query.extra_details
        }
        if setUsed:
            query = Player6auto.objects.filter(serial=data.get('serial')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })



class stock3Api(APIView):
    def get(self, request):
        from team2b import encryption
        call_url = ''
        call_data = ''
        device_id = ''
        cksm_v4 = encryption.cksm_v4(call_url, call_data, device_id)
        fingerprint = encryption.fingerprint(device_id)
        
        
        return Response({
            'cksm_v4':cksm_v4,
            'fingerprint':fingerprint
        })



class FantossMiningAPI(APIView):
    def put(self, request):
        query = FantossUserIds()
        query.campaign_name = request.data.get('camp_name','fantosst2modd')
        query.id = request.data.get('id')
        query.extra_details=request.data.get('extra_details',{})
        query.used_at = None
        try:
            query.save()
            return Response({
            })
        except:
            return Response({
            })

    def get(self, request):
        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        filter_dict = {}
        query = FantossUserIds.objects.filter(used_at=None,**filter_dict).order_by('-created_at')[0:50].first()
        
        data = {
                'id':query.id,
                'used_at':query.used_at,
                'extra_details':query.extra_details
        }
        if setUsed:
            query = FantossUserIds.objects.filter(id=data.get('id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })


class OkeyvipMiningAPI(APIView):
    def put(self, request):
        query = OkeyvipUserId()
        query.campaign_name = request.data.get('camp_name','okeyvipmodd')
        query.id = request.data.get('id')
        query.extra_details=request.data.get('extra_details',{})
        query.used_at = None
        try:
            query.save()
            return Response({
            })
        except:
            return Response({
            })

    def get(self, request):
        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        filter_dict = {}
        query = OkeyvipUserId.objects.filter(used_at=None,**filter_dict).order_by('-created_at')[0:50].first()
        
        data = {
                'id':query.id,
                'used_at':query.used_at,
                'extra_details':query.extra_details
        }
        if setUsed:
            query = OkeyvipUserId.objects.filter(id=data.get('id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })

class SephoraMiningAPI(APIView):
    def put(self, request):
        query = SephoraOrderId()
        query.campaign_name = request.data.get('camp_name','sephoramodd')
        query.id = request.data.get('id')
        query.price = request.data.get('price')
        query.extra_details=request.data.get('extra_details',{})
        query.used_at = None
        try:
            query.save()
            return Response({
            })
        except:
            return Response({
            })

    def get(self, request):
        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        filter_dict = {}
        query = SephoraOrderId.objects.filter(used_at=None,**filter_dict).order_by('-created_at')[0:50].first()
        
        data = {
                'id':query.id,
                'price':query.price,
                'used_at':query.used_at,
                'extra_details':query.extra_details
        }
        if setUsed:
            query = SephoraOrderId.objects.filter(id=data.get('id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })

class SephoraMiningAPIV2(APIView):
    def put(self, request):
        query = SephoraOrderIdV2()
        query.campaign_name = request.data.get('camp_name','sephoramodd')
        query.id = request.data.get('id')
        query.price = request.data.get('price')
        query.extra_details=request.data.get('extra_details',{})
        query.payment_type=request.data.get('payment_type','cash')
        query.used_at = None
        try:
            query.save()
            return Response({
            })
        except:
            return Response({
            })

    def get(self, request):
        
        setUsed = request.GET.get('set_used',True)
        channel = request.GET.get('channel')
        network = request.GET.get('network')
        af_prt = request.GET.get('af_prt')
        offer_id = request.GET.get('offer_id')
        payment_type = request.GET.get('payment_type')
        test = request.GET.get('test')
        
        if not channel or not network or not offer_id:
            return Response({
                        'body':'error',
                        'message':'channel,offer_id,network id missing.'
                    })
        
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        if test=="yes":
            filter_dict = {
                "id":60093380
            }
        else:
            filter_dict = {}
        # filter_dict['created_at__gte'] = date.today()
        
        if payment_type:
            filter_dict['payment_type']= payment_type

        exclude_dict = {}
        if channel: 
            exclude_dict['channel__contains'] = channel
            # exclude_dict['af_prt__contains'] = af_prt

        # if af_prt:
        #     exclude_dict['af_prt__contains'] = af_prt

        query_list = SephoraOrderIdV2.objects.filter(used_at=None, price__gte="7000.0",**filter_dict).order_by('-created_at')[0:25].all()
        if not query_list:
            query_list = SephoraOrderIdV2.objects.filter(price__gte="7000.0", **filter_dict).exclude(**exclude_dict).order_by('-created_at')[0:25].all()
        
        if query_list:
            for i in range(3):
                query = random.choice(query_list)

                if not query.channel:
                    new_channel = [channel]
                else:
                    new_channel = query.channel
                    new_channel.append(channel)

                if not query.network:
                    new_network = [network]
                else:
                    new_network = query.network
                    new_network.append(network)

                if not query.offer_id:
                    new_offer_id = [offer_id]
                else:
                    new_offer_id = query.offer_id
                    new_offer_id.append(offer_id)

                new_af_prt = query.af_prt
                if af_prt:
                    new_af_prt.append(af_prt)

                data = {
                        'order_id':query.id,
                        'payment_type':query.payment_type,
                        'used_at':query.used_at,
                        'extra_details':query.extra_details
                }
                if setUsed:
                    query = SephoraOrderIdV2.objects.filter(id=data.get('order_id')).update(
                        used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        channel=new_channel,
                        network=new_network,
                        offer_id=new_offer_id,
                        af_prt=new_af_prt
                        )
                return Response({
                    'body':data,
                })
            
        return Response({
            'body':{},
        })

class PumaMiningAPI(APIView):
    def put(self, request):
        query = PumaOrderId()
        query.campaign_name = request.data.get('camp_name','pumaauto')
        query.id = request.data.get('id')
        query.extra_details=request.data.get('extra_details',{})
        query.used_at = None
        try:
            query.save()
            return Response({
            })
        except Exception as e:
            import traceback
            traceback.print_exc()
            return Response({
            })

    def get(self, request):
        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        filter_dict = {}
        query = PumaOrderId.objects.filter(used_at=None,**filter_dict).order_by('-created_at')[0:50].first()
        
        data = {
                'id':query.id,
                'used_at':query.used_at,
                'extra_details':query.extra_details
        }
        if setUsed:
            query = PumaOrderId.objects.filter(id=data.get('id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })


class ServerHealth(APIView):
    def get(self, request):
        return Response({
            'resp': 'OK'
        })
    

class TimoclubMiningAPI(APIView):
    def put(self, request):
        query = TimoclubUserId()
        query.campaign_name = request.data.get('camp_name','timoclubmodd')
        query.id = request.data.get('id')
        query.extra_details=request.data.get('extra_details',{})
        query.used_at = None
        try:
            query.save()
            return Response({
            })
        except:
            return Response({
            })

    def get(self, request):
        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        filter_dict = {}
        query = TimoclubUserId.objects.filter(used_at=None,**filter_dict).order_by('-created_at')[0:50].first()
        
        data = {
                'id':query.id,
                'used_at':query.used_at,
                'extra_details':query.extra_details
        }
        if setUsed:
            query = TimoclubUserId.objects.filter(id=data.get('id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })

class EmailIdMiningAPI(APIView):
    def put(self, request):
        query = EmailIdMining()
        query.campaign_name = request.data.get('camp_name','petzeauto')
        query.id = request.data.get('id')
        query.extra_details=request.data.get('extra_details',{})
        query.used_at = None
        try:
            query.save()
            return Response({
            })
        except:
            return Response({
            })

    def get(self, request):
        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        filter_dict = {}
        query = EmailIdMining.objects.filter(used_at=None,**filter_dict).order_by('-created_at')[0:50].first()
        
        data = {
                'id':query.id,
                'used_at':query.used_at,
                'extra_details':query.extra_details
        }
        if setUsed:
            query = EmailIdMining.objects.filter(id=data.get('id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })

class IndigoV2MiningAPI(APIView):
    def put(self, request):
        query = IndigoV2Mining()
        query.campaign_name = request.data.get('camp_name','indigomoddteam2modd')
        query.pnr = request.data.get('pnr')
        query.departure_date = request.data.get('departure_date')
        query.booking_date = request.data.get('booking_date')
        query.email = request.data.get('email')
        query.company=request.data.get('company')
        query.extra_details=request.data.get('extra_details',{})
        query.fare = request.data.get('extra_details',{}).get('fare')
        query.currency = request.data.get('extra_details',{}).get('currency')
        query.used_at = None
        try:
            query.save()
            return Response({
            })
        except:
            return Response({
            })

    def get(self, request):
        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        unused_count = request.GET.get('unused_count', False)
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        private_companies = [
            'MAKEMYTRIP INDIA PVT LTD',
            'Paytm',
            'Cleartrip Private Limited',
            'CLEARTRIP TRAVELS PVT LTD',
            'EaseMyTrip',
            'EasyTripPlanners',
            'travelmaster.in',
            'NUPUR TRAVELS',
            'Yatra Online Pvt Ltd'
        ]
        
        filter_dict = {}
        query = None
        
        cc = 21
        if not unused_count:
            cc = IndigoV2Mining.objects.filter(used_at=None,departure_date__gte=datetime.now(),company='None',**filter_dict).order_by('created_at').count()
        
        if unused_count or (not unused_count and cc>20):
            query = IndigoV2Mining.objects.filter(used_at=None,departure_date__gte=datetime.now(),company='None',**filter_dict).order_by('created_at')[0:50].first()
        if not query:
            query = IndigoV2Mining.objects.filter(used_at=None,departure_date__gte=datetime.now(),company='Company',**filter_dict).order_by('created_at')[0:50].first()
        if not query:
            query = IndigoV2Mining.objects.filter(used_at=None,departure_date__gte=datetime.now(),**filter_dict).exclude(company__in=private_companies).order_by('created_at')[0:50].first()
        
        if channel not in ["adshustle", "vestaapps", "appsfollowing"]:
            used_count = IndigoV2Mining.objects.filter(used_at__startswith=datetime.now().strftime('%Y-%m-%d')).count()
            bt2_count = IndigoV2Mining.objects.filter(used_at__startswith=datetime.now().strftime('%Y-%m-%d'), channel="adshustle").count()
            bt2_count += IndigoV2Mining.objects.filter(used_at__startswith=datetime.now().strftime('%Y-%m-%d'), channel="vestaapps").count()
            bt2_count += IndigoV2Mining.objects.filter(used_at__startswith=datetime.now().strftime('%Y-%m-%d'), channel="appsfollowing").count()
            if not unused_count:
                unused_count = IndigoV2Mining.objects.filter(used_at=None,company='None').count()

            
            
            if used_count:
                other_bt_count = used_count - bt2_count

                if other_bt_count > (used_count + unused_count)/2:
                    return Response({
                            'body':{"status": "Not Allowed"}
                        })


        data = {
                'pnr':query.pnr,
                'email': query.email,
                'used_at':query.used_at,
                'extra_details':query.extra_details
        }
        if setUsed:
            query = IndigoV2Mining.objects.filter(pnr=data.get('pnr')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })


class RevenueHelperAPI(APIView):
    def put(self, request):
        query = RevenueHelper()
        query.campaign_name = request.data.get('camp_name','pepperfryyauto')
        query.channel = request.data.get('channel')
        query.network = request.data.get('network')
        query.offer_id = request.data.get('offer_id')
        query.id = request.data.get('id')
        query.revenue = request.data.get('revenue')
        query.currency = request.data.get('currency')
        query.adid = request.data.get('adid')
        query.event_name = request.data.get('event_name')
        query.event_value = request.data.get('event_value', {})
        query.app_version = request.data.get('app_version', '')
        query.script_version = request.data.get('script_version', '')
        try:
            query.save()
            return Response({
            })
        except:
            return Response({
            })
        


def send_to_gchat(_msg,_tag,webhook_url):
    params = { 
            "threadKey": _tag,
            "messageReplyOption": "REPLY_MESSAGE_FALLBACK_TO_NEW_THREAD"
        }
    try:
        resp = requests.post(url=webhook_url,params=params, json={"text": _msg}, verify=False).json()
    except Exception as e:
        print("[+] Something went wrong {}".format(e))

class ScriptRealtimeChecker(APIView):

    def get(self, request):
        from django.db.models import F, Sum, FloatField, Avg
        from tabulate import tabulate
        import pandas

        aov_data_dict = {'Script Name':[],'Channel':[],'Network':[],'Offer ID':[],'Currency':[],'AOV':[],'Total Revenue':[],'Count':[]}
        arpu_data_list = []
        event_percent_list = []

        yesterday_date = (datetime.now()-timedelta(days=1)).strftime("%Y-%m-%d")
        data = ScriptChecks.objects.all()
        for item in data:
            campaign_name = item.campaign_name
            aov_check = item.AOV_check
            arpu_check = item.ARPU_check
            event_percent_check = item.event_percent_check
            if aov_check:
                data = RevenueHelper.objects.filter(campaign_name=campaign_name,created_at__contains=yesterday_date).values('currency','channel','network','offer_id').annotate(count=Count(F('event_name')),total_revenue=Sum(F('revenue')),revenue=Avg(F('revenue')))
                for cc in data:
                    aov_data_dict['Script Name'].append(campaign_name)
                    aov_data_dict['Channel'].append(cc.get('channel'))
                    aov_data_dict['Network'].append(cc.get('network'))
                    aov_data_dict['Offer ID'].append(cc.get('offer_id'))
                    aov_data_dict['Currency'].append(cc.get('currency'))
                    aov_data_dict['AOV'].append(int(cc.get('revenue')))
                    aov_data_dict['Total Revenue'].append(int(cc.get('total_revenue')))
                    aov_data_dict['Count'].append(cc.get('count'))

        tabular_string = tabulate(pandas.DataFrame(aov_data_dict).to_dict(orient="list"), headers="keys", tablefmt="github")
        tabular_string = f"*AOV - {yesterday_date}*\n\n```{tabular_string}```"

        _tag = yesterday_date
        send_to_gchat(tabular_string,_tag,'https://chat.googleapis.com/v1/spaces/AAAAh8zMzAw/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=gzewsbx9lIeHlzEa5j5c1K7eqOS60AevmzgPe1UpZJc')

        
        try:
            return Response({
                'data':aov_data_dict,
            })
        except:
            return Response({
            })
        

class ResetOrderId(APIView):

    def get(self, request):
        tablesDict = {
            'mcdeliverymodd':McdeliveryScriptOrderIds,
            'dominosindomodd':DominosIndodeliveryScriptOrderIds,
            'pepperfryauto':PepperfryOrderIds,
            # 'habibmodd':HabibScriptOrderIdsConstants,
            # 'tripsygamesmodd': TripsygamesOrderIds,
            # 'ostinshopmodd': OstinShopScriptOrderIds,
            # 'lazuritappmetrica': LazuritOrderIds,
            # 'gomcdoauto': GomcdOrderIds,
            'bharatmatrimonymodd': BharatmatrimonyUserIds,
            'weworldauto': WeWorldIds,
            'fantosst2modd': FantossUserIds,
            'okeyvipmodd': OkeyvipUserId,
            'sephoramodd': SephoraOrderId,
            'pumaauto': PumaOrderId,
            'timoclubauto': TimoclubUserId,
            'emailIds_Mined': EmailIdMining

            # 'samsclubmodd': SamsclubMemberIds,
            # 'mumzworldautoios':MumzworldOrderIds,
            # 'damnraymodd':DamnrayOrderIds,
            # 'indigomodd':IndigoScriptOrdersIds,
            # 'lightinthebox':LightInTheBox,
        }
        tablename = request.GET.get('table')
        id_ = request.GET.get('id')
        update_status = tablesDict[tablename].objects.filter(id=id_).update(used_at=None)

        return Response({
            'status':'ok',
            'record_updated':update_status
        })
    
class GhnMiningAPI(APIView):
    def put(self, request):
        query = ghnUserId()
        query.campaign_name = request.data.get('camp_name','ghnmodd')
        query.id = request.data.get('id')
        query.extra_details=request.data.get('extra_details',{})
        query.used_at = None
        try:
            query.save()
            return Response({
            })
        except:
            return Response({
            })

    def get(self, request):
        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        filter_dict = {}
        query = ghnUserId.objects.filter(used_at=None,**filter_dict).order_by('-created_at')[0:50].first()
        
        data = {
                'id':query.id,
                'used_at':query.used_at,
                'extra_details':query.extra_details
        }
        if setUsed:
            query = ghnUserId.objects.filter(id=data.get('id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })

class RummytimeMiningAPI(APIView):
    def put(self, request):
        query = RummytimeUserId()
        query.campaign_name = request.data.get('camp_name','rummytimemodd')
        query.id = request.data.get('id')
        query.extra_details=request.data.get('extra_details',{})
        query.used_at = None
        try:
            query.save()
            return Response({
            })
        except:
            return Response({
            })

    def get(self, request):
        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        filter_dict = {}
        query = RummytimeUserId.objects.filter(used_at=None,**filter_dict).order_by('-created_at')[0:50].first()
        
        data = {
                'id':query.id,
                'used_at':query.used_at,
                'extra_details':query.extra_details
        }
        if setUsed:
            query = RummytimeUserId.objects.filter(id=data.get('id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })


class IndigoTokenRefresh(APIView):
    def get(self,request):
        from oauth2client.service_account import ServiceAccountCredentials
        from googleapiclient.discovery import build
        import gspread
        from data_tracking.util import get_credential

        credentials = get_credential()
        
        sheet_url = "https://docs.google.com/spreadsheets/d/1tDT7Wco4_NgV3wWzI3Q8MqdVzVcDz-qxhljI3nuf1lA/edit?gid=0#gid=0"
        subsheet_name = "Tokens"

        Sheet_credential = gspread.service_account_from_dict(credentials)
        spreadsheet = Sheet_credential.open_by_url(sheet_url)
        print('[+] Subsheet Access: {}'.format(subsheet_name))
        worksheet = spreadsheet.worksheet(subsheet_name)
        list_of_lists = worksheet.get_all_values()
        header_row = list_of_lists[0]
        redis_obj = Redis()
        for item in list_of_lists[1:]:
            no_update = False
            key = 'INDIGO_TOKEN_{}_DATA'.format(item[0])
            old_data = redis_obj.retrieve_data(key=key)
            if old_data:
                if item[0] == old_data.get('INSTANCE_ID'):
                    if item[3] == old_data.get('GET_TOKEN') and item[2] == old_data.get('POST_TOKEN'):
                        no_update = old_data.get('UPDATED_AT')

            value = {
                'INSTANCE_ID':item[0],
                'PNR_USED':item[1],
                'POST_TOKEN':item[2],
                'GET_TOKEN':item[3],
                'INITIALIZER':item[4],
                "UPDATED_AT":str(datetime.now()) if not no_update else no_update,
            }
            redis_obj.save(key=key,value=value)

        return Response({
            'body':list_of_lists,
        })
    


class ScoreoneMiningAPI(APIView):
    def put(self, request):
        query = ScoreoneUserId()
        query.campaign_name = request.data.get('camp_name','scoreone')
        query.id = request.data.get('id')
        query.extra_details=request.data.get('extra_details',{})
        query.used_at = None
        try:
            query.save()
            return Response({
            })
        except:
            return Response({
            })

    def get(self, request):
        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        filter_dict = {}
        query = ScoreoneUserId.objects.filter(used_at=None,**filter_dict).order_by('-created_at')[0:50].first()
        
        data = {
                'id':query.id,
                'used_at':query.used_at,
                'extra_details':query.extra_details
        }
        if setUsed:
            query = ScoreoneUserId.objects.filter(id=data.get('id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })




class TrackScript(APIView):

    def get(self, request):
        from django.db.models import Q,Sum

        start_date = request.GET.get('from_date')
        end_date = request.GET.get('end_date')
        campaign_name = request.GET.get('campaign_name')
        channel = request.GET.get('channel')
        network = request.GET.get('network')
        offer_id = request.GET.get('offer_id')

        filter_dict = {
            'created_at__gte':start_date,
            'created_at__lte':end_date + " 23:59:59.999999",
        }

        for key in ['campaign_name','channel','network','offer_id']:
            if request.GET.get(key):
                dd = {}
                dd[key] = request.GET.get(key)
                filter_dict.update(dd)
                
        values_dict = [
            'campaign_name',
        ]

        data = RevenueHelper.objects.filter(**filter_dict).values(*values_dict).annotate(
            install_count=Count('event_name',filter=Q(event_name='Install')),
            total_count=Count('event_name'),
            total_revenue=Sum('revenue'),
            )

        for item in data:
            item['event_count'] = item.get('total_count') - item.get('install_count')
            item['event_percent']=0
            item['aov']=0
            item['roi']=0
            if item.get('install_count'):
                item['event_percent'] = round(item.get('event_count')*100/item.get('install_count'),2)
            if item.get('total_revenue')>0:
                if item.get('event_count'):
                    item['aov'] = round(item.get('total_revenue')/item.get('event_count'),2)
                if item.get('install_count'):
                    item['roi'] = round(item.get('total_revenue')/item.get('install_count'),2)
        try:
            return Response({
                'data':data
            })
        except:
            return Response({
                'data':data
            })
        

class ApnatimeMiningAPI(APIView):
    def put(self, request):
        query = ApnatimeUserId()
        query.campaign_name = request.data.get('camp_name','apnatimeauto')
        query.id = request.data.get('id')
        query.extra_details=request.data.get('extra_details',{})
        query.used_at = None
        try:
            query.save()
            return Response({
            })
        except:
            return Response({
            })

    def get(self, request):
        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        filter_dict = {}
        query = ApnatimeUserId.objects.filter(used_at=None,**filter_dict).order_by('-created_at')[0:50].first()
        
        data = {
                'id':query.id,
                'used_at':query.used_at,
                'extra_details':query.extra_details
        }
        if setUsed:
            query = ApnatimeUserId.objects.filter(id=data.get('id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })


class KhiladiaddaMiningAPI(APIView):
    def put(self, request):
        query = KhiladiaddaUserId()
        query.campaign_name = request.data.get('camp_name','khiladiaddamodd')
        query.id = request.data.get('id')
        query.extra_details=request.data.get('extra_details',{})
        query.used_at = None
        try:
            query.save()
            return Response({
            })
        except:
            return Response({
            })

    def get(self, request):
        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        filter_dict = {}
        query = KhiladiaddaUserId.objects.filter(used_at=None,**filter_dict).order_by('-created_at')[0:50].first()
        
        data = {
                'id':query.id,
                'used_at':query.used_at,
                'extra_details':query.extra_details
        }
        if setUsed:
            query = KhiladiaddaUserId.objects.filter(id=data.get('id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })


class DatingGlobalMiningAPI(APIView):
    def put(self, request):
        query = DatingGlobalUserId()
        query.campaign_name = request.data.get('camp_name','datingglobalt2modd')
        query.id = request.data.get('id')
        query.extra_details=request.data.get('extra_details',{})
        query.purchase_status=request.data.get('purchase_status')
        query.used_at = None
        try:
            query.save()
            return Response({
            })
        except:
            return Response({
            })

    def get(self, request):
        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        filter_dict = {}
        query = DatingGlobalUserId.objects.filter(used_at=None,**filter_dict).order_by('-created_at')[0:50].first()
        
        data = {
                'id':query.id,
                'used_at':query.used_at,
                'purchase_status':query.purchase_status,
                'extra_details':query.extra_details
        }
        if setUsed:
            query = DatingGlobalUserId.objects.filter(id=data.get('id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })


class DatingGlobalSubscribedMiningAPI(APIView):
    def put(self, request):
        query = DatingGlobalSubscribedUserId()
        query.campaign_name = request.data.get('camp_name','datingglobalt2modd')
        query.id = request.data.get('id')
        query.extra_details=request.data.get('extra_details',{})
        query.purchase_status=request.data.get('purchase_status')
        query.used_at = None
        try:
            query.save()
            return Response({
            })
        except:
            return Response({
            })

    def get(self, request):
        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        filter_dict = {}
        query = DatingGlobalSubscribedUserId.objects.filter(used_at=None,**filter_dict).order_by('-created_at')[0:50].first()
        
        data = {
                'id':query.id,
                'used_at':query.used_at,
                'purchase_status':query.purchase_status,
                'extra_details':query.extra_details
        }
        if setUsed:
            query = DatingGlobalSubscribedUserId.objects.filter(id=data.get('id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })

