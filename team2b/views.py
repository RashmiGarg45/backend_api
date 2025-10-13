from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from team2b.models import MumzworldOrderIds,PepperfryOrderIds,SimulationIds,DamnrayOrderIds,IndigoScriptOrderIds,IgpScriptOrderIds,McdeliveryScriptOrderIds,LightInTheBox,DominosIndodeliveryScriptOrderIds,OstinShopScriptOrderIds,HabibScriptOrderIdsConstants,WatchoOrderIdsMining,TripsygamesOrderIds, LazuritOrderIds, GomcdOrderIds, BharatmatrimonyUserIds, SamsclubMemberIds, WeWorldIds, Player6auto, IDHelperApps, FantossUserIds, OkeyvipUserId, SephoraOrderId, PumaOrderId, TimoclubUserId, EmailIdMining, RevenueHelper,IndigoV3Mining, IndigoV2Mining, ScriptChecks,SephoraOrderIdV2, ghnUserId, RummytimeUserId, ScoreoneUserId, ApnatimeUserId, KhiladiaddaUserId, DatingGlobalUserId, DatingGlobalSubscribedUserId, CountChecks, Bluerewards, Holodilink, RentomojoUserId, Shahid, Eztravel, Betwinner, Ladygentleman, Tajrummy, Bet22, PepperFry, Igpmodd, Travelata, Ontime, Mcdmodd, tipsAosValid, tipsAosCancelled, tipsIosValid, tipsIosCancelled, Skyline, Reserva, GuruShort, GuruShortNotPremium, Credito, GuruShortOrderId, GuruShortValidId, Ajio, Jungleepoker, GameRummy, Navrang, Lotter38, Lotter69, ChaleeSultan, Ejaby, Flappdeals, Laundrymate, Parimatch, KisanKonnect, EpoCosmetic,Ebebekuid, Ebebek, Underarmour, UnderarmourOID, Pinoypeso, Ohi, Fivepaisa, Adda, AddaOrderId, Bambootauto, Paynearby, in2X, BluerewardsV2, Signnow, SixerDream, WesternUnion, StolotoUserId, StolotoOrderId, PaysettUserId, ShopeevnOID, ShopeevnUID, Poppolive, ShopeemyOID, ShopeemyUID, Shiprocket, Novawater, Moglix, Viu, Betr, ShopeeidUID, Dupoin,Parimatchth, ShopeephUID, Epikodd, Stoloto, Casinopluss, Homiedev, Storyland, TikettOID, ApnaTime, MotiLal, Frendipay, Magicland, FoxtaleOrderId, Hoteltonight, stolotoCIF, Yesmadam, Beymen, Bncauto, Kfcmexico, Jazzcash, Petbook, tejimaandi,Tejimaandinew,Paytmmoneyt,Anqgoldrewards,Anqgoldrewardscuid,Anqgoldrewardsoid,OkeyvipMining,Moneymetmodduid,Imagineart,Melive,Metlive, MetliveUID, MeliveUID, Opay,Bevietnames, Boost,Myauchan,Ikea,Cimbthai,ShopeebrUID,ShopeethiosUID,ShopeethUID,Anqgoldrewardsnew,MyfriendUID,MyfriendOID,MambaUID,GalaxyChatCountry, GalaxyChatRU, GalaxyChat,Alphacapital,Cabst13,Bigloan,IndigoV4Mining,Coinmena, TikettUID, R888casino,Joybuy, Atomepht2uid, Atomepht2aid,Myshift,Clubeextra,Clubeextracid,Hering,Babytracker
from team2b.services.redis import Redis
from django.utils import timezone
from decimal import Decimal
from django.db.models import Q
from datetime import datetime,timedelta,date
import json, time, random
import requests

from django.db.models import Count, Sum, Case, When, IntegerField, FloatField
from django.db.models import Avg
from django.db import transaction
from django.db.models.functions import Cast

def db_controlled_apps():
    li = ["TikettUIDAPI", "CoinmenaAPI", "bigloanAPI", "MyfriendOIDAPI", "IkeaAPI", "MyauchanAPI", "CimbthaiAPI", "BevietnamesAPI", "ImagineartAPI", "MoneymetmodduidAPI", "AnqgoldrewardsoidAPI", "AnqgoldrewardscuidAPI", "PaytmmoneytAPI", "KfcAPI", "BncAPI", "BeymenAPI", "FrendipayAPI", "MotiLalAPI", "ApnaTimeAPI", "HomiedevAPI", "StorylandAPI", "CasinoplussAPI", "BetrAPI", "PaysettUserIdAPI", "StolotoOrderIdAPI", "WesternUnionAPI", "SignnowAPI", "BluerewardsV2API", "PaynearbyAPI", "BambootautoAPI", "FivepaisaAPI", "PinoypesoAPI", "UnderarmourOIDAPI", "UnderarmourAPI", "EbebekuidAPI", "EbebekAPI", "ParimatchAPI", "EjabyAPI", "ChaleeSultanAPI", "Lotter69API", "Lotter38API", "creditoAPI", "skylineAPI", "mcdAPI", "igpAPI", "pepperfryAPI", "betwinnerAPI", "eztravelAPI", "shahidAPI"]

def mining_apps():
    from datetime import datetime,timedelta

    d = {'dominosindomodd_OID': 'dominosindomodd', 'watchomodd_OID': 'watchomodd', 'pepperfryyauto_OID': 'pepperfryyauto', 'tripsygamesmodd_OID': 'tripsygamesmodd', 'ostinshopmodd_OID': 'ostinshopmodd', 'lazuritappmetrica_OID': 'lazuritappmetrica', 'bharatmatrimonymodd_UID': 'bharatmatrimonymodd', 'weworldauto_UID': 'weworldauto', 'fantosst2modd_UID': 'fantosst2modd', 'okeyvipmodd_UID': 'okeyvipmodd', 'scoreone_UID': 'scoreone', 'ghnmodd_UID': 'ghnmodd', 'rummytimemodd_UID': 'rummytimemodd', 'sephoramodd_OID': 'sephoramodd', 'pumaauto_OID': 'pumaauto', 'timoclubauto_UID': 'timoclubauto', 'khiladiaddamodd_UID': 'khiladiaddamodd', 'datingglobalt2modd_UID': 'datingglobalt2modd', 'Subs_datingglobalt2modd_UID': 'datingglobalt2modd', 'indigomoddteam2modd_OID': 'indigomoddteam2modd', 'samsclubmodd_UID': 'samsclubmodd', 'mumzworldautoios_OID': 'mumzworldautoios', 'damnraymodd_OID': 'damnraymodd', 'rentmojomodd_UID': 'rentmojomodd', 'lightinthebox_OID': ['lightintheboxmodd', 'lightintheboxiosmodd'], 'ladygentlemanmodd_OID': 'ladygentlemanmodd', 'tajrummymodd_UID': 'tajrummymodd', 'bet22modd/planbetmodd_UID': ['bet22modd', 'planbetmodd'], 'reservamodd_UID': 'reservamodd', 'gurushortmodd_UID': 'gurushortmodd', 'gurushortmodd_OID': 'gurushortmodd', 'jungleepokerauto_UID': 'jungleepokerauto', 'gamerummyprimemodd_UID': 'gamerummyprimemodd', 'navrangmodd_UID': 'navrangmodd', 'flappdealsmodd_OID': 'flappdealsmodd', 'laundrymateauto_OID': 'laundrymateauto', 'parimatchmodd_UID': 'parimatchmodd', 'epocosmeticmodd': 'epocosmeticmodd', 'kisankonnectmodd_OID': 'kisankonnectmodd', 'ohiauto_UID': 'ohiauto', 'adda52_UID': ['adda52tmodd', 'adda52pokeriosmodd'], 'adda52_OID': ['adda52tmodd', 'adda52pokeriosmodd'], 'shopeevn_UID': 'shopeevntauto', 'shopeevn_OID': 'shopeevntauto', 'poppolivetmodd_UID': 'poppolivetmodd', 'shopeemy_UID': 'shoppemytauto', 'shopeeid_UID': 'shopeeno1tauto', 'shiprocketcouriert_UID': 'shiprocketcouriert', 'novawateriosmodd_OID': 'novawateriosmodd', 'moglixauto_OID': 'moglixauto', 'viuhkmodd_UID': 'viuhkmodd', 'dupoin_UID': 'dupointmodd', 'shopeephtauto_UID': 'shopeephtauto', 'ontimeautoios_UID': 'ontimeautoios', 'stolototmodd_UID': 'stolototmodd', 'magiclandmodd': 'magiclandmodd', 'foxtalemodd': 'foxtalemodd', 'yesmadammodd': 'yesmadammodd', 'hoteltonight': ['hoteltonightauto', 'hoteltonightautoios'], "jazzcash_UID": "jazzcashmodd", "petbookappmetrica": "petbookappmetrica", "tejimaandiauto": "tejimaandiauto", "metlivemodd": "metlivemodd", "melivemodd": "melivemodd", "metlivemodd_recharged": "metlivemodd", "melivemodd_recharged": "melivemodd", "opaynewmodd": "opaynewmodd", 'anqgoldrewardsmodd_uid': 'anqgoldrewardsmodd', 'shopeet_uid': 'shopeet', 'myfriendauto_uid': 'myfriendauto','alphacapital_num':'alphacapitalmodd', "r888casinomodd_uid": 'r888casinomodd','babytracker_uid':'babytrackermodd'}

    running_apps = []
    from_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    to_date = (datetime.now() - timedelta(days=0)).strftime('%Y-%m-%d')

    report6Data = requests.get('https://info.appsuccessor.com/devteamnumbers.php?secret=b0a492d6271466cb71e9ab53982ddd1d&team=team2&datefrom={}&dateto={}'.format(from_date,to_date)).json()

    running_apps = []

    for key, value in report6Data.items():
        yesterday_i2 = value.get(from_date, {}).get("i1")
        today_i2 = value.get(to_date, {}).get("i1")

        if yesterday_i2 or today_i2:
            running_apps.append(key) 

    output = []
    for key, value in d.items():
        if isinstance(value, list):
            for i in value:
                if i in running_apps:
                    output.append(key)
        else:
            if value in running_apps:
                output.append(key)

    return output

class GenericScriptFunctions(APIView):
    def get(self, request):
        all_apps = {
            'jazzcash_UID': Jazzcash,
            'dominosindomodd_OID':DominosIndodeliveryScriptOrderIds,
            'watchomodd_OID':WatchoOrderIdsMining,
            'pepperfryyauto_OID':PepperfryOrderIds,
            'tripsygamesmodd_OID': TripsygamesOrderIds,
            'ostinshopmodd_OID': OstinShopScriptOrderIds,
            'lazuritappmetrica_OID': LazuritOrderIds,
            # 'gomcdoauto/mcdot2ios_OID': GomcdOrderIds,
            'bharatmatrimonymodd_UID': BharatmatrimonyUserIds,
            'weworldauto_UID': WeWorldIds,
            'fantosst2modd_UID': FantossUserIds,
            'okeyvipmodd_UID': OkeyvipMining,
            'scoreone_UID': ScoreoneUserId,
            'ghnmodd_UID': ghnUserId,
            'rummytimemodd_UID': RummytimeUserId,
            'sephoramodd_OID': SephoraOrderIdV2,
            'pumaauto_OID': PumaOrderId, 
            'timoclubauto_UID': TimoclubUserId,
            # 'apnatimeauto_UID': ApnatimeUserId,
            'khiladiaddamodd_UID': KhiladiaddaUserId,
            'datingglobalt2modd_UID': DatingGlobalUserId,
            'Subs_datingglobalt2modd_UID': DatingGlobalSubscribedUserId,
            'indigomoddteam2modd_OID': IndigoV4Mining,
            'samsclubmodd_UID': SamsclubMemberIds,
            'mumzworldautoios_OID':MumzworldOrderIds,
            'damnraymodd_OID':DamnrayOrderIds,
            'rentmojomodd_UID':RentomojoUserId,
            'lightinthebox_OID':LightInTheBox,
            'ladygentlemanmodd_OID': Ladygentleman,
            'tajrummymodd_UID': Tajrummy,
            'bet22modd/planbetmodd_UID': Bet22,
            'reservamodd_UID': Reserva,
            'gurushortmodd_UID': GuruShort,
            'gurushortmodd_OID': GuruShortOrderId,
            'jungleepokerauto_UID': Jungleepoker,
            'gamerummyprimemodd_UID': GameRummy,
            'navrangmodd_UID': Navrang,
            'flappdealsmodd_OID':Flappdeals,
            'laundrymateauto_OID': Laundrymate,
            'parimatchmodd_UID': Parimatch,
            'epocosmeticmodd': EpoCosmetic,
            'kisankonnectmodd_OID': KisanKonnect,
            'ohiauto_UID': Ohi,
            'adda52_UID': Adda,
            'adda52_OID': AddaOrderId,
            'shopeevn_UID': ShopeevnUID,
            'shopeevn_OID': ShopeevnOID,
            'babytracker_uid':Babytracker,
            'poppolivetmodd_UID': Poppolive,
            'shopeemy_UID': ShopeemyUID,
            'shopeeid_UID': ShopeeidUID,
            'shiprocketcouriert_UID': Shiprocket,
            'novawateriosmodd_OID': Novawater,
            'moglixauto_OID': Moglix,
            'viuhkmodd_UID': Viu,
            'dupoin_UID': Dupoin,
            'shopeephtauto_UID' : ShopeephUID,
            'ontimeautoios_UID': Ontime,
            'stolototmodd_UID': Stoloto,
            'magiclandmodd': Magicland,
            'foxtalemodd': FoxtaleOrderId,
            'yesmadammodd': Yesmadam,
            'hoteltonight': Hoteltonight,
            "petbookappmetrica": Petbook,
            'tejimaandiauto':Tejimaandinew, 
            "metlivemodd": MetliveUID,
            "metlivemodd_recharged": Metlive,
            "melivemodd": MeliveUID,
            "melivemodd_recharged": Melive,
            "opaynewmodd": Opay,
            'anqgoldrewardsmodd_uid': Anqgoldrewardsnew,
            'myfriendauto_uid':MyfriendUID,
            'shopeet_uid':ShopeethUID,
            # 'shopeetios_uid': ShopeethiosUID,
            # 'mambda_uid': MambaUID,
            'alphacapital_num':Alphacapital,
            'r888casinomodd_uid': R888casino,
        }

        running_apps = mining_apps()
        tablesDict = {}
        for i in running_apps:
            tablesDict[i] = all_apps.get(i)

        today = datetime.now().strftime('%Y-%m-%d')
        ids_mined = {}

        private_companies = [
            'MAKEMYTRIP INDIA PVT LTD',
            'Paytm',
            'Cleartrip Private Limited',
            'CLEARTRIP TRAVELS PVT LTD',
            'EaseMyTrip',
            'EasyTripPlanners',
            'travelmaster.in',
            'NUPUR TRAVELS',
            'Yatra Online Pvt Ltd',
            'M**********************D',
            'E********p',
            'P***m',
            'E**************s',
            'C***********************D'
        ]

        for key,value in tablesDict.items():
            ids_mined[key] = tablesDict[key].objects.filter(created_at__gte=str(today),created_at__lte=str(today+" 23:59:59")).count()

            if key == "indigomoddteam2modd_OID":           
                ids_mined[key] = IndigoV4Mining.objects.filter(departure_date__gte=datetime.now(),created_at__gte=str(today),created_at__lte=str(today+" 23:59:59")).count()

        from data_tracking.util import googleChatBot_send_message
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

        googleChatBot_send_message(space_name="AAQAKDdPHnI",message=message)   
        googleChatBot_send_message(space_name='AAAA7sIzS9Q',message=message)    

        return Response({
            'ids_mined':ids_mined,
        })


class GenericUnusedIdScriptFunctions(APIView):
    def get(self, request):
        all_apps = {
            'jazzcash_UID': Jazzcash,
            'dominosindomodd_OID':DominosIndodeliveryScriptOrderIds,
            'watchomodd_OID':WatchoOrderIdsMining,
            'pepperfryyauto_OID':PepperfryOrderIds,
            'tripsygamesmodd_OID': TripsygamesOrderIds,
            'ostinshopmodd_OID': OstinShopScriptOrderIds,
            'lazuritappmetrica_OID': LazuritOrderIds,
            # 'gomcdoauto/mcdot2ios_OID': GomcdOrderIds,
            'bharatmatrimonymodd_UID': BharatmatrimonyUserIds,
            'weworldauto_UID': WeWorldIds,
            'fantosst2modd_UID': FantossUserIds,
            'okeyvipmodd_UID': OkeyvipMining,
            'scoreone_UID': ScoreoneUserId,
            'ghnmodd_UID': ghnUserId,
            'rummytimemodd_UID': RummytimeUserId,
            'sephoramodd_OID': SephoraOrderIdV2,
            'pumaauto_OID': PumaOrderId, 
            'timoclubauto_UID': TimoclubUserId,
            # 'apnatimeauto_UID': ApnatimeUserId,
            'khiladiaddamodd_UID': KhiladiaddaUserId,
            'datingglobalt2modd_UID': DatingGlobalUserId,
            'Subs_datingglobalt2modd_UID': DatingGlobalSubscribedUserId,
            'indigomoddteam2modd_OID': IndigoV4Mining,
            'samsclubmodd_UID': SamsclubMemberIds,
            'mumzworldautoios_OID':MumzworldOrderIds,
            'damnraymodd_OID':DamnrayOrderIds,
            'rentmojomodd_UID':RentomojoUserId,
            'lightinthebox_OID':LightInTheBox,
            'ladygentlemanmodd_OID': Ladygentleman,
            'tajrummymodd_UID': Tajrummy,
            'bet22modd/planbetmodd_UID': Bet22,
            'reservamodd_UID': Reserva,
            'gurushortmodd_UID': GuruShort,
            'gurushortmodd_OID': GuruShortOrderId,
            'jungleepokerauto_UID': Jungleepoker,
            'gamerummyprimemodd_UID': GameRummy,
            'navrangmodd_UID': Navrang,
            'flappdealsmodd_OID':Flappdeals,
            'laundrymateauto_OID': Laundrymate,
            'parimatchmodd_UID': Parimatch,
            'epocosmeticmodd': EpoCosmetic,
            'kisankonnectmodd_OID': KisanKonnect,
            'ohiauto_UID': Ohi,
            'adda52_UID': Adda,
            'adda52_OID': AddaOrderId,
            'shopeevn_UID': ShopeevnUID,
            'shopeevn_OID': ShopeevnOID,
            'babytracker_uid':Babytracker,
            'poppolivetmodd_UID': Poppolive,
            'shopeemy_UID': ShopeemyUID,
            'shopeeid_UID': ShopeeidUID,
            'shiprocketcouriert_UID': Shiprocket,
            'novawateriosmodd_OID': Novawater,
            'moglixauto_OID': Moglix,
            'viuhkmodd_UID': Viu,
            'dupoin_UID': Dupoin,
            'shopeephtauto_UID' : ShopeephUID,
            'ontimeautoios_UID': Ontime,
            'stolototmodd_UID': Stoloto,
            'magiclandmodd': Magicland,
            'foxtalemodd': FoxtaleOrderId,
            'yesmadammodd': Yesmadam,
            'hoteltonight': Hoteltonight,
            "petbookappmetrica": Petbook,
            'tejimaandiauto':tejimaandi,
            "metlivemodd": MetliveUID,
            "metlivemodd_recharged": Metlive,
            "melivemodd": MeliveUID,
            "melivemodd_recharged": Melive,
            "opaynewmodd": Opay,
            'anqgoldrewardsmodd_uid': Anqgoldrewardsnew,
            'myfriendauto_uid':MyfriendUID,
            'shopeet_uid':ShopeethUID,
            # 'shopeetios_uid': ShopeethiosUID,
            # 'mambda_uid': MambaUID,
            'alphacapital_num':Alphacapital,
            'r888casinomodd_uid': R888casino,
        }

        running_apps = mining_apps()
        tablesDict = {}
        for i in running_apps:
            tablesDict[i] = all_apps.get(i)

        private_companies = [
            'MAKEMYTRIP INDIA PVT LTD',
            'Paytm',
            'Cleartrip Private Limited',
            'CLEARTRIP TRAVELS PVT LTD',
            'EaseMyTrip',
            'EasyTripPlanners',
            'travelmaster.in',
            'NUPUR TRAVELS',
            'Yatra Online Pvt Ltd',
            'M**********************D',
            'E********p',
            'P***m',
            'E**************s',
            'C***********************D'
        ]
        ids_mined = {}
        for key in tablesDict.keys():
            ids_mined[key] = tablesDict[key].objects.filter(used_at = None).count()

            if key == "indigomoddteam2modd_OID":
                ids_mined[key] = ids_mined[key] = IndigoV4Mining.objects.filter(used_at=None,departure_date__gte=datetime.now()).count()


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
        googleChatBot_send_message(space_name="AAQAKDdPHnI",message=message)
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
        print (scriptname)

        if not scriptname:
            print ("No script name")
            raise ValidationError({'error': 'scriptname was not provided.'})

        

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
        url = "http://info.appsuccessor.com/devteamnumbers.php?secret=b0a492d6271466cb71e9ab53982ddd1d&team=team2&datefrom={}&dateto={}".format(date.today() - timedelta(days=1),date.today() - timedelta(days=1))
        today_r6_data = requests.get(url).json()

        print (today_r6_data)
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

            if today_r6_data.get(app,{}).get(str(date.today() - timedelta(days=1)),{}).get('TR'):
                data[app] = {}
                dict__['i2'] = today_r6_data.get(app,{}).get(str(date.today() - timedelta(days=1)),{}).get('TR')
            
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


class BluerewardsAPI(APIView):
    def put(self, request):
        query = Bluerewards()
        query.campaign_name = request.data.get('camp_name','bluerewardsauto')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Bluerewards.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = Bluerewards.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })


class holodilinkAPI(APIView):
    def put(self, request):
        query = Holodilink()
        query.campaign_name = request.data.get('camp_name','holodilinkappmetrica')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Holodilink.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = Holodilink.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
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
        query.spdn = request.data.get("spdn")
        query.amount = request.data.get("amount")
        query.extra_details2 = request.data.get("extra_details2")
        query.used_at = None
        # try:
        query.save()
        return Response({
        })
        # except:
        #     return Response({
        #     })
        
    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        order_status = request.GET.get('order_status')
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        filter_dict = {}
        if order_status:
            filter_dict['order_status'] = order_status
        query = WatchoOrderIdsMining.objects.filter(used_at=None,**filter_dict).exclude(spdn="Coupon").order_by('-created_at')[0:50].first()
        
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
        exclude_dict['spdn__contains'] = 'Coupon'

        exclude_dict_1 = {}
        exclude_dict_1['spdn__contains'] = 'Coupon'
        amount_values = [299.0, 2499.0, 309.0, 2599.0, 229.0, 1999.0, 399.0]

        query_list = WatchoOrderIdsMining.objects.filter(~Q(spdn="Coupon"), used_at=None,amount__in=amount_values,**filter_dict).exclude(**exclude_dict_1).order_by('-created_at')[0:25].all()        
        if not query_list:
            # return None
            query_list = WatchoOrderIdsMining.objects.filter(~Q(spdn="Coupon"),**filter_dict).exclude(**exclude_dict).order_by('-created_at')[0:25].all()
        
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
        query.state = request.data.get('state', '')
        query.age = request.data.get('age', '')
        query.is_paid = request.data.get('is_paid', '')
        query.mother_tongue = request.data.get('mother_tongue', '')
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
        mother_tongue = request.GET.get("mother_tongue")
        is_paid = request.GET.get("is_paid")
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        filter_dict = {"mother_tongue": mother_tongue, "is_paid": is_paid}
        query = BharatmatrimonyUserIds.objects.filter(used_at=None,**filter_dict).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'used_at':query.used_at,
                'extra_details':{"age": query.age, "gender": query.extra_details.get("viewProfile").get("gender")}
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
        query.save()
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
        query.price = request.data.get('price')
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

        r = random.randint(1, 100)

        # if r<= 70:
        #     min_price = '5000.0'
        #     max_price = '10000.0'
        # elif r<= 90:
        #     min_price = '1500.0'
        #     max_price = '5000.0'
        # else:
        #     min_price = '10000.0'
        #     max_price = '20000.0'

        # query = PumaOrderId.objects.filter(used_at=None, price__gte=Decimal(min_price), price__lte=Decimal(max_price),**filter_dict).order_by('-created_at')[0:50].first()

        # if not query:
        query = PumaOrderId.objects.filter(used_at=None, price__gte=Decimal('5000.0'),**filter_dict).order_by('-created_at')[0:50].first()
        
        data = {
                'id':query.id,
                'used_at':query.used_at,
                'extra_details':query.extra_details,
                'price': query.price
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
        except Exception as e:
            if 'team2b_indigov2mining.email' in str(e):
                query = IndigoV3Mining()
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
                    return Response({})
                except Exception as e:
                    return Response({"error": str(e)})
            return Response({"error": str(e)
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
            'Yatra Online Pvt Ltd',
            'M**********************D',
            'E********p',
            'P***m',
            'E**************s',
            'C***********************D'
        ]
        
        filter_dict = {}
        query = None
        
        cc = 21
        if not unused_count:
            cc = IndigoV3Mining.objects.filter(used_at=None, currency="INR",departure_date__gte=datetime.now(),company='None',**filter_dict).order_by('created_at', 'departure_date').count()
        
        if unused_count or (not unused_count and cc>20):
            query = IndigoV3Mining.objects.filter(used_at=None, currency="INR",departure_date__gte=datetime.now(),company='None',**filter_dict).order_by('created_at', 'departure_date')[0:50].first()
        if not query:
            query = IndigoV3Mining.objects.filter(used_at=None, currency="INR",departure_date__gte=datetime.now(),company='C*****y',**filter_dict).order_by('created_at', 'departure_date')[0:50].first()
        if not query:
            # query = IndigoV3Mining.objects.annotate(fare_float=Cast('fare', FloatField())).filter(used_at=None, currency="INR",departure_date__gte=datetime.now(),**filter_dict, fare_float__gt=1000.0).exclude(company__in=private_companies).order_by('departure_date', 'created_at')[0:50].first()
            query = IndigoV3Mining.objects.annotate(fare_float=Cast('fare', FloatField())).filter(used_at=None, currency="INR",departure_date__gte=datetime.now(),**filter_dict, fare_float__gt=1000.0).exclude(company__in=private_companies).order_by('created_at', 'departure_date')[0:50].first()
        
        # if channel not in ["adshustle", "vestaapps", "appsfollowing"]:
        #     used_count = IndigoV2Mining.objects.filter(used_at__startswith=datetime.now().strftime('%Y-%m-%d')).count()
        #     bt2_count = IndigoV2Mining.objects.filter(used_at__startswith=datetime.now().strftime('%Y-%m-%d'), channel="adshustle").count()
        #     bt2_count += IndigoV2Mining.objects.filter(used_at__startswith=datetime.now().strftime('%Y-%m-%d'), channel="vestaapps").count()
        #     bt2_count += IndigoV2Mining.objects.filter(used_at__startswith=datetime.now().strftime('%Y-%m-%d'), channel="appsfollowing").count()
        #     if not unused_count:
        #         unused_count = IndigoV2Mining.objects.filter(used_at=None,company='None').count()
        #     if used_count:
        #         other_bt_count = used_count - bt2_count

        #         if other_bt_count > (used_count + unused_count)/2:
        #             return Response({'body':{"status": "Not Allowed"}})
        if channel in ["mobpine", "77ads", "appamplify"]:
            bt3_count = IndigoV3Mining.objects.filter(used_at__startswith=datetime.now().strftime('%Y-%m-%d'), channel__in=("mobpine", "77ads", "appamplify")).count()
            print (bt3_count)

            if bt3_count > 100:
                return Response({'body':{"status": "Not Allowed"}})

        elif channel in ["adshustle", "vestaapps", "appsfollowing"]:
            bt2_count = IndigoV3Mining.objects.filter(used_at__startswith=datetime.now().strftime('%Y-%m-%d'), channel__in=("adshustle", "vestaapps", "appsfollowing")).count()
            print (bt2_count)
            if bt2_count > 100:
                return Response({'body':{"status": "Not Allowed"}})


        data = {
                'pnr':query.pnr,
                'email': query.email,
                'used_at':query.used_at,
                'extra_details':query.extra_details
        }
        if setUsed:
            query = IndigoV3Mining.objects.filter(pnr=data.get('pnr')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })

class IndigoV3MiningAPI(APIView):
    def put(self, request):
        query = IndigoV4Mining()
        query.campaign_name = request.data.get('camp_name','indigomoddteam2modd')
        query.pnr = request.data.get('pnr')
        query.departure_date = request.data.get('departure_date')
        query.booking_date = request.data.get('booking_date')
        query.extra_details=request.data.get('extra_details',{})
        query.used_at = None
        query.save()
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
        
        query = IndigoV4Mining.objects.filter(used_at=None,departure_date__gte=datetime.now()).order_by('created_at', 'departure_date').first()
        
        if channel in ["mobpine", "77ads", "appamplify"]:
            bt3_count = IndigoV4Mining.objects.filter(used_at__startswith=datetime.now().strftime('%Y-%m-%d'), channel__in=("mobpine", "77ads", "appamplify")).count()
            print (bt3_count)

            if offer_id in ["indigo-prudent-8"]:
                offer_id_count = IndigoV4Mining.objects.filter(used_at__startswith=datetime.now().strftime('%Y-%m-%d'), offer_id=offer_id).count()

                if offer_id_count > 10:
                    return Response({'body':{"status": "Not Allowed"}})

            elif bt3_count > 100:
                return Response({'body':{"status": "Not Allowed"}})


        elif channel in ["adshustle", "vestaapps", "appsfollowing", "appsatiate"]:
            bt2_count = IndigoV4Mining.objects.filter(used_at__startswith=datetime.now().strftime('%Y-%m-%d'), channel__in=("adshustle", "vestaapps", "appsfollowing", "appsatiate")).count()
            print (bt2_count)

            if offer_id in ["idgafsmmp", "idgmedmmp"]:
                print ("indigo inside")
                offer_id_count = IndigoV4Mining.objects.filter(used_at__startswith=datetime.now().strftime('%Y-%m-%d'), offer_id=offer_id).count()
                print ("indigo count", offer_id_count)
                if offer_id_count > 6:
                    return Response({'body':{"status": "Not Allowed"}})
                
            elif bt2_count > 200:
                return Response({'body':{"status": "Not Allowed"}})


        data = {
                'pnr':query.pnr,
                'used_at':query.used_at,
                'extra_details':query.extra_details
        }
        if setUsed:
            query = IndigoV4Mining.objects.filter(pnr=data.get('pnr')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
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
        # query.day = request.data.get("day")
        query.c_day = request.data.get("day", 100)
        try:
            query.save()
            return Response({
            })
        except:
            return Response({
            })
        
    def get(self, request):
        campaign_name = request.GET.get('campaign_name')
        channel = request.GET.get('channel')
        network = request.GET.get('network')
        offer_id = request.GET.get('offer_id')
        date_ = datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d")
        event_name = request.GET.get('event_name')

        install_count = (
            RevenueHelper.objects.filter(
                event_name="Install",
                campaign_name=campaign_name,
                channel=channel,
                network=network,
                offer_id=offer_id,
                created_at__gt=date_,
            ).count()
        )

        revenue_data = (
            RevenueHelper.objects.filter(
                event_name=event_name,
                campaign_name=campaign_name,
                channel=channel,
                network=network,
                offer_id=offer_id,
                created_at__gt=date_,
            ).aggregate(
                total_revenue=Sum("revenue"),
                event_count=Count("event_name")
            )
        )


        total_revenue = revenue_data["total_revenue"]
        event_count = revenue_data["event_count"]

        if total_revenue is None:
            total_revenue = 0.00001
        if install_count is None:
            install_count = 0
        if event_count is None:
            event_count = 0

        

        return Response({"response_code": 200, "message": "success", "data": {"install_count": install_count , "event_count": event_count , "total_revenue": total_revenue }})


        

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
        # send_to_gchat(tabular_string,_tag,'https://chat.googleapis.com/v1/spaces/AAAAh8zMzAw/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=gzewsbx9lIeHlzEa5j5c1K7eqOS60AevmzgPe1UpZJc')

        
        try:
            return Response({
                'data':aov_data_dict,
            })
        except:
            return Response({
            })


class ScriptRealtimeChecker2(APIView):

    def get(self, request):
        from django.db.models import F, Sum, FloatField, Avg
        from tabulate import tabulate
        import pandas

        aov_data_dict = {'Script Name':[], "Event": [],'Channel':[],'Network':[],'Offer ID':[],'Count':[]}
        arpu_data_list = []
        event_percent_list = []

        yesterday_date = (datetime.now()-timedelta(days=1)).strftime("%Y-%m-%d")
        data = CountChecks.objects.all()
        for item in data:   
            aov_data_dict = {'Script Name':[], "Event": [],'Count':[],'Channel':[],'Network':[],'Offer ID':[]}
            campaign_name = item.campaign_name
            aov_check = item.AOV_check
            arpu_check = item.ARPU_check
            event_percent_check = item.event_percent_check
            if aov_check:
                data = RevenueHelper.objects.filter(campaign_name=campaign_name,created_at__contains=yesterday_date).values('event_name','channel','network','offer_id').annotate(count=Count('id'))
                for cc in data:
                    aov_data_dict['Script Name'].append(campaign_name)
                    aov_data_dict['Event'].append(cc.get('event_name'))
                    aov_data_dict['Count'].append(cc.get('count'))
                    aov_data_dict['Channel'].append(cc.get('channel'))
                    aov_data_dict['Network'].append(cc.get('network'))
                    aov_data_dict['Offer ID'].append(cc.get('offer_id'))                    
                    

            df = pandas.DataFrame(aov_data_dict)

            messages = []
            if aov_check:
                messages.append(f"*{campaign_name} Offer ID Wise Stats on {yesterday_date}*")

            for offer_id, group in df.groupby("Offer ID"):
                sorted_group = group.sort_values(by=["Count"] , ascending=False)
                tabular_string = tabulate(
                    sorted_group.to_dict(orient="list"),
                    headers="keys",
                    tablefmt="github",
                    showindex=False
                    )
                message = f"*Offer ID {offer_id} on {yesterday_date}*\n\n```{tabular_string}```"
                messages.append(message)


            # tabular_string = tabulate(pandas.DataFrame(aov_data_dict).sort_values(by=["Offer ID"]).to_dict(orient="list"), headers="keys", tablefmt="github", showindex=False)
            # tabular_string = f"*AOV - {yesterday_date}*\n\n```{tabular_string}```"
            for msg in messages:
                _tag = campaign_name + yesterday_date
                send_to_gchat(msg,_tag,'https://chat.googleapis.com/v1/spaces/AAAAFdZDsFE/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=GRQ8zGftP_Icrs7bsgNhFoLgV1LFrmChBJO7J5U5kis')

        
        try:
            return Response({
                'data':aov_data_dict,
            })
        except:
            return Response({
            })
        
class ConversionStats(APIView):
    def get(self, request):

        data_type = request.GET.get("type")

        if data_type == "Yesterday":
            date = (datetime.now()-timedelta(days=1)).strftime("%Y-%m-%d")
        else:
            date = (datetime.now()).strftime("%Y-%m-%d")

        scripts_list = ["boylesportstmodd", "joybuymodd", "ocbcmodd", "raisinggoblinmodd", "galaxytmodd", "naukrigulftmodd", "muthootfinonemodd", "accorhotelstmodd", "shopeeno1tauto", "musicallyt", "shopeephtauto", "casinoplussmodd", "zee5newmodd", "mcdeliverymodd", "poppolivetmodd", "smartqarzamodd", "magnittmodd", "waylettmodd", "juanhandmodd",'allobankmodd', "gsmtmodd", "jazzcashmodd", "jupitertmodd", "mxplayertmodd", "bigloanmodd", "kisshttmodd", "betwinnerngmodd","clonemcdeliverymodd", "danamodd", "paymayamodd", "opaymodd", "heringmodd", "tikettmodd", "etomomodd", "robotzaimerrmodd", "stolototmodd", "netshoesmodd", "shrirammodd", "credmaxmodd", "tunaikutmodd", "paytmmoneytmodd", "foxtalemodd", "gamerummyprimemodd", "bcsinvestmenttmodd", "myacuvuemodd", "viuhkmodd", "yesmadammodd", "byutmodd", "indigomoddteam2modd", "roxmodd", "cryptocomtmodd", "intercopromodd", "waylettnewmodd", "babytrackermodd", "opaynewmodd", "eaptekatauto", "digitalbankmodd", "bbvamodd", "quickcashonlinemodd", "betrmodd", "heliummobilemodd", "kfcmexicotmodd", "comparemodd", "yesmadammodd", "rupeeredeemodd", "zeptodeliverymodd", "easycashtmodd", "finnixtmodd", "myntmodd", "alphacapitalmodd", "r888casinomodd"]

        output = {}
        for campaign_name in scripts_list:

            data = RevenueHelper.objects.filter(campaign_name=campaign_name,created_at__contains=date, event_name__in=("Non-organic", "Organic")).values('event_name').annotate(count=Count('id'))
            organic_count = 0
            non_organic_count = 0
            d = {}
            for i in data:
                name = i["event_name"]
                count = i["count"]

                if name == "Organic":
                    organic_count = count
                elif name == "Non-organic":
                    non_organic_count =  count


                d[name] =count

            if non_organic_count or organic_count:
                d["RR"] = (non_organic_count / (organic_count+non_organic_count))*100

                output[campaign_name] = d

        output = dict(sorted(output.items(), key=lambda x: x[1].get("RR", 0), reverse=False))

        header = f"{'Campaign':<20} {'Non-Organic':>12} {'Organic':>10} {'RR (%)':>10}"
        lines = ["*"+data_type + "RR Summary:*", header, "-" * len(header)]
        for campaign, stats in output.items():
            non_org = stats.get("Non-organic", stats.get("non-organic", 0))
            org = stats.get("Organic", stats.get("organic", 0))
            rr = stats.get("RR", "")
            line = f"{campaign:<20} {non_org:>12} {org:>10} {rr:>10.2f}" if rr != "" else f"{campaign:<20} {non_org:>12} {org:>10} {'':>10}"
            lines.append(line)

        formatted_table = "```\n" + "\n".join(lines) + "\n```"

        # Send to Google Chat
        payload = {
            "text": formatted_table
        }

        webhook_url = 'https://chat.googleapis.com/v1/spaces/AAQAU-R97AU/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=OqUekeKK07KIs1KJvUSmFhhk4NJS4H4PEDbklzGEY0M'


        response = requests.post(webhook_url, data=json.dumps(payload), headers={"Content-Type": "application/json"})

        webhook_url = 'https://chat.googleapis.com/v1/spaces/AAQAt2N77EQ/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=qo95hAebwGohxef2ePz_vr1ADP6xOjOAk4MfhWrYEqw'
        response = requests.post(webhook_url, data=json.dumps(payload), headers={"Content-Type": "application/json"})

        if response.status_code == 200:
            print("Message sent successfully.")
        else:
            print(f"Failed to send message: {response.status_code} - {response.text}")
            

        return Response({
            'data':output,
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

class RentomojoMiningAPI(APIView):
    def put(self, request):
        query = RentomojoUserId()
        query.campaign_name = request.data.get('camp_name','rentmojomodd')
        query.id = request.data.get('id')
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
        query = RentomojoUserId.objects.filter(used_at=None,**filter_dict).order_by('-created_at')[0:50].first()

        # if channel not in ["adshustle", "vestaapps", "appsfollowing"]:
        #     used_count = RentomojoUserId.objects.filter(used_at__startswith=datetime.now().strftime('%Y-%m-%d')).count()
        #     bt2_count = RentomojoUserId.objects.filter(used_at__startswith=datetime.now().strftime('%Y-%m-%d'), channel="adshustle").count()
        #     bt2_count += RentomojoUserId.objects.filter(used_at__startswith=datetime.now().strftime('%Y-%m-%d'), channel="vestaapps").count()
        #     bt2_count += RentomojoUserId.objects.filter(used_at__startswith=datetime.now().strftime('%Y-%m-%d'), channel="appsfollowing").count()
        #     if not unused_count:
        #         unused_count = RentomojoUserId.objects.filter(used_at=None).count()
        #     if used_count:
        #         other_bt_count = used_count - bt2_count

        #         if other_bt_count > (used_count + unused_count)/3:
        #             return Response({'body':{"status": "Not Allowed"}})
                
        if channel in ["mobpine", "77ads", "appamplify"]:
            bt3_count = RentomojoUserId.objects.filter(used_at__startswith=datetime.now().strftime('%Y-%m-%d'), channel__in=("mobpine", "77ads", "appamplify")).count()
            print (bt3_count)

            if bt3_count > 40:
                return Response({'body':{"status": "Not Allowed"}})

        elif channel in ["quasarmobi", "offersinfinite", "mobiaviator"]:
            bt1_count = RentomojoUserId.objects.filter(used_at__startswith=datetime.now().strftime('%Y-%m-%d'), channel__in=("quasarmobi", "offersinfinite", "mobiaviator")).count()
            print (bt1_count)
            if bt1_count > 40:
                return Response({'body':{"status": "Not Allowed"}})

        
        data = {
                'id':query.id,
                'used_at':query.used_at,
        }
        if setUsed:
            query = RentomojoUserId.objects.filter(id=data.get('id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })

class shahidAPI(APIView):
    def put(self, request):
        query = Shahid()
        query.campaign_name = request.data.get('camp_name','shahidmodd')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Shahid.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = Shahid.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })

class eztravelAPI(APIView):
    def put(self, request):
        query = Eztravel()
        query.campaign_name = request.data.get('camp_name','eztravelmodd')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Eztravel.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = Eztravel.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })
    
class betwinnerAPI(APIView):
    def put(self, request):
        query = Betwinner()
        query.campaign_name = request.data.get('camp_name','betwinner')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Betwinner.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = Betwinner.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })

class ladygentlemanAPI(APIView):
    def put(self, request):
        query = Ladygentleman()
        query.campaign_name = request.data.get('camp_name','ladygentlemanmodd')
        query.id = request.data.get('order_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):


        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = Ladygentleman.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'order_id':query.id,
                'used_at':query.used_at,
        }
        if setUsed:
            query = Ladygentleman.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })

class TajrummyAPI(APIView):
    def put(self, request):
        query = Tajrummy()
        query.campaign_name = request.data.get('camp_name','tajrummymodd')
        query.id = request.data.get('order_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = Tajrummy.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'order_id':query.id,
                'used_at':query.used_at,
        }
        if setUsed:
            query = Tajrummy.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
            

class Bet22API(APIView):
    def put(self, request):
        query = Bet22()
        query.campaign_name = request.data.get('camp_name','bet22modd')
        query.id = request.data.get('order_id')
        query.price = request.data.get('price')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        
        query = Bet22.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'order_id':query.id,
        }
        if setUsed:
            query = Bet22.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
class pepperfryAPI(APIView):
    def put(self, request):
        query = PepperFry()
        query.campaign_name = request.data.get('camp_name','pepperfry')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = PepperFry.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = PepperFry.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })

class igpAPI(APIView):
    def put(self, request):
        query = Igpmodd()
        query.campaign_name = request.data.get('camp_name','igpmodd')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Igpmodd.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = Igpmodd.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })

class TravelataAPI(APIView):
    def put(self, request):
        query = Travelata()
        query.campaign_name = request.data.get('camp_name','travelataappmodd')
        query.id = request.data.get('order_id')
        query.booking_type = request.data.get('booking_type')
        query.extra_details = request.data.get('extra_details',{})
        query.price = request.data.get('price')
        query.number = request.data.get('number')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = Travelata.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'order_id':query.id,
                'used_at':query.used_at,
                'extra_details':query.extra_details, 
                'price': query.price
        }
        if setUsed:
            query = Travelata.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
class OntimeAPI(APIView):
    def put(self, request):
        query = Ontime()
        query.campaign_name = request.data.get('camp_name','ontimeautoios')
        query.id = request.data.get('order_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        
        query = Ontime.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'order_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = Ontime.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
  
class mcdAPI(APIView):
    def put(self, request):
        query = Mcdmodd()
        query.campaign_name = request.data.get('camp_name','mcdeliverymodd')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Mcdmodd.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = Mcdmodd.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })

class tipsAosValidAPI(APIView):
    def put(self, request):
        query = tipsAosValid()
        query.campaign_name = request.data.get('camp_name','tipstopauto')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        
        query = tipsAosValid.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = tipsAosValid.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })

class tipsAosCancelledAPI(APIView):
    def put(self, request):
        query = tipsAosCancelled()
        query.campaign_name = request.data.get('camp_name','tipstopauto')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        
        query = tipsAosCancelled.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = tipsAosCancelled.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
  
class tipsIosValidAPI(APIView):
    def put(self, request):
        query = tipsIosValid()
        query.campaign_name = request.data.get('camp_name','tipsstopautoios')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        
        query = tipsIosValid.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = tipsIosValid.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })

class tipsIosCancelledAPI(APIView):
    def put(self, request):
        query = tipsIosCancelled()
        query.campaign_name = request.data.get('camp_name','tipsstopautoios')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        
        query = tipsIosCancelled.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = tipsIosCancelled.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
  
class skylineAPI(APIView):
    def put(self, request):
        query = Skyline()
        query.campaign_name = request.data.get('camp_name','skylineautoios')
        query.id = request.data.get('order_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Skyline.objects.latest('created_at')
        
        data = {
                'order_id':query.id,
        }
        if setUsed:
            query = Skyline.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })

class ReservaAPI(APIView):
    def put(self, request):
        query = Reserva()
        query.campaign_name = request.data.get('camp_name','reservamodd')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.profile_details = request.data.get('profile_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        
        query = Reserva.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = Reserva.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
  
class GurushortAPI(APIView):
    def put(self, request):
        query = GuruShort()
        query.campaign_name = request.data.get('camp_name','gurushortmodd')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        
        query = GuruShort.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = GuruShort.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
class GurushortNotPremiumAPI(APIView):
    def put(self, request):
        query = GuruShortNotPremium()
        query.campaign_name = request.data.get('camp_name','gurushortmodd')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        
        query = GuruShortNotPremium.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = GuruShortNotPremium.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
class creditoAPI(APIView):
    def put(self, request):
        query = Credito()
        query.campaign_name = request.data.get('camp_name','clickcreditomodd')
        query.id = request.data.get('order_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Credito.objects.latest('created_at')
        
        data = {
                'order_id':query.id,
        }
        if setUsed:
            query = Credito.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })
    
class GurushortOrderIdAPI(APIView):
    def put(self, request):
        query = GuruShortOrderId()
        query.campaign_name = request.data.get('camp_name','gurushortmodd')
        query.id = request.data.get('order_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        
        query = GuruShortOrderId.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'order_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = GuruShortOrderId.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
class GurushortValidAPI(APIView):
    def put(self, request):
        query = GuruShortValidId()
        query.campaign_name = request.data.get('camp_name','gurushortmodd')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        
        query = GuruShortValidId.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = GuruShortValidId.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })

class AjioAPI(APIView):
    def put(self, request):
        query = Ajio()
        query.campaign_name = request.data.get('camp_name','ajiomodd')
        query.id = request.data.get('order_id')
        query.extra_details = request.data.get('extra_details',{})
        query.brand = request.data.get('brand', '')
        query.price = request.data.get('price')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        
        query = Ajio.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'order_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = Ajio.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
class JungleepokerAPI(APIView):
    def put(self, request):
        query = Jungleepoker()
        query.campaign_name = request.data.get('camp_name','jungleepokerauto')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        
        query = Jungleepoker.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = Jungleepoker.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
class GameRummyAPI(APIView):
    def put(self, request):
        query = GameRummy()
        query.campaign_name = request.data.get('camp_name','gamerummyprimemodd')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        if channel in ["quasarmobi", "offersinfinite", "mobiaviator"]:
            return Response({'body':{}})
        
        if offer_id and offer_id.isdecimal():
            return Response({'body':{"status": "Not Allowed"}})

        
        query = GameRummy.objects.filter(used_at=None).order_by('-created_at')[0:50].first()

        if channel in ["mobpine", "77ads", "appamplify"]:
            bt3_count = GameRummy.objects.filter(used_at__startswith=datetime.now().strftime('%Y-%m-%d'), channel__in=("mobpine", "77ads", "appamplify")).count()
            print (bt3_count)

            if bt3_count > 60:
                return Response({'body':{"status": "Not Allowed", "current_count": bt3_count}})

        elif channel in ["adshustle", "vestaapps", "appsfollowing", "appsatiate"]:
            bt2_count = GameRummy.objects.filter(used_at__startswith=datetime.now().strftime('%Y-%m-%d'), channel__in=("adshustle", "vestaapps", "appsfollowing", "appsatiate")).count()
            print (bt2_count)
            if bt2_count > 60:
                return Response({'body':{"status": "Not Allowed","current_count": bt2_count}})
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = GameRummy.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
class navrangAPI(APIView):
    def put(self, request):
        query = Navrang()
        query.campaign_name = request.data.get('camp_name','navrangmodd')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        r = random.randint(1,100)
        if r<= 40:
            plan = "Week"
        elif r<= 90:
            plan = "Month"
        else:
            plan = "Year"
        print (plan)

        query = Navrang.objects.filter(used_at=None, extra_details__icontains='"plan_name": "'+plan+'"').order_by('-created_at')[0:50].first()   
        
        # query = Navrang.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = Navrang.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
class Lotter38API(APIView):
    def put(self, request):
        query = Lotter38()
        query.campaign_name = request.data.get('camp_name','Lotter38')
        query.id = request.data.get('order_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Lotter38.objects.latest('created_at')
        
        data = {
                'order_id':query.id,
        }
        if setUsed:
            query = Lotter38.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })
    
class Lotter69API(APIView):
    def put(self, request):
        query = Lotter69()
        query.campaign_name = request.data.get('camp_name','Lotter69')
        query.id = request.data.get('order_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Lotter69.objects.latest('created_at')
        
        data = {
                'order_id':query.id,
        }
        if setUsed:
            query = Lotter69.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })
   
class ChaleeSultanAPI(APIView):
    def put(self, request):
        query = ChaleeSultan()
        query.campaign_name = request.data.get('camp_name','chaalesultanauto')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        
        query = ChaleeSultan.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                # 'extra_details':query.extra_details, 
        }
        if setUsed:
            query = ChaleeSultan.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
class EjabyAPI(APIView):
    def put(self, request):
        query = Ejaby()
        query.campaign_name = request.data.get('camp_name','ejabyauto')
        query.id = request.data.get('order_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Ejaby.objects.latest('created_at')
        
        data = {
                'order_id':query.id,
        }
        if setUsed:
            query = Ejaby.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })
    
class FlappdealsAPI(APIView):
    def put(self, request):
        query = Flappdeals()
        query.campaign_name = request.data.get('camp_name','flappdealsmodd')
        query.id = request.data.get('order_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        
        query = Flappdeals.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'order_id':query.id,
                # 'extra_details':query.extra_details, 
        }
        if setUsed:
            query = Flappdeals.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
class LaundrymateAPI(APIView):
    def put(self, request):
        query = Laundrymate()
        query.campaign_name = request.data.get('camp_name','laundrymateauto')
        query.id = request.data.get('order_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        
        query = Laundrymate.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'order_id':query.id,
                # 'extra_details':query.extra_details, 
        }
        if setUsed:
            query = Laundrymate.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
class ParimatchAPI(APIView):
    def put(self, request):
        query = Parimatch()
        query.campaign_name = request.data.get('camp_name','parimatchmodd')
        query.id = request.data.get('order_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        
        query = Parimatch.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'order_id':query.id,
                # 'extra_details':query.extra_details, 
        }
        if setUsed:
            query = Parimatch.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
class KisanKonnectAPI(APIView):
    def put(self, request):
        query = KisanKonnect()
        query.campaign_name = request.data.get('camp_name','kisankonnectmodd')
        query.id = request.data.get('order_id')
        query.extra_details = request.data.get('extra_details',{})
        query.price = request.data.get('price')
        query.payment_type = request.data.get('payment_type')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        
        query = KisanKonnect.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'order_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = KisanKonnect.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
class EpoCosmeticAPI(APIView):
    def put(self, request):
        query = EpoCosmetic()
        query.campaign_name = request.data.get('camp_name','epocosmeticmodd')
        query.id = request.data.get('order_id')
        query.extra_details = request.data.get('extra_details',{})
        query.price = request.data.get('price')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        min_price = '20.0'
        max_price = '2000.0'

        query = EpoCosmetic.objects.filter(used_at=None, price__gte=Decimal(min_price), price__lte=Decimal(max_price)).order_by('-created_at')[0:50].first()

        if not query:
            query = EpoCosmetic.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'order_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = EpoCosmetic.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })

    def post(self, request):
        query = EpoCosmetic.objects.order_by('-id').first()

        return Response({
            'id':query.id,
        })
 
class EbebekAPI(APIView):
    def put(self, request):
        query = Ebebek()
        query.campaign_name = request.data.get('camp_name','ebebekauto')
        query.id = request.data.get('order_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Ebebek.objects.latest('created_at')
        
        data = {
                'order_id':query.id,
        }
        if setUsed:
            query = Ebebek.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })

class EbebekuidAPI(APIView):
    def put(self, request):
        query = Ebebekuid()
        query.campaign_name = request.data.get('camp_name','ebebekauto')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Ebebekuid.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = Ebebekuid.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })

    
class UnderarmourAPI(APIView):
    def put(self, request):
        query = Underarmour()
        query.campaign_name = request.data.get('camp_name','underarmourauto')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Underarmour.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = Underarmour.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })
    
class UnderarmourOIDAPI(APIView):
    def put(self, request):
        query = UnderarmourOID()
        query.campaign_name = request.data.get('camp_name','underarmourauto')
        query.id = request.data.get('order_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = UnderarmourOID.objects.latest('created_at')
        
        data = {
                'order_id':query.id,
        }
        if setUsed:
            query = UnderarmourOID.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })
    
class pingAPI(APIView):
    def get(self, request):
        return Response({"status_code": 200})
    
class PinoypesoAPI(APIView):
    def put(self, request):
        query = Pinoypeso()
        query.campaign_name = request.data.get('camp_name','pinoypesomodd')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Pinoypeso.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = Pinoypeso.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })
    
class OhiAPI(APIView):
    def put(self, request):
        query = Ohi()
        query.campaign_name = request.data.get('camp_name','ohiauto')
        query.id = request.data.get('user_id')
        # query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        
        query = Ohi.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                # 'extra_details':query.extra_details, 
        }
        if setUsed:
            query = Ohi.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
class FivepaisaAPI(APIView):
    def put(self, request):
        query = Fivepaisa()
        query.campaign_name = request.data.get('camp_name','fivepaisamodd')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Fivepaisa.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = Fivepaisa.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })
    
class AddaAPI(APIView):
    def put(self, request):
        query = Adda()
        query.campaign_name = request.data.get('camp_name','adda52tmodd')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = Adda.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'used_at':query.used_at,
        }
        if setUsed:
            query = Adda.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
            
class AddaorderIdAPI(APIView):
    def put(self, request):
        query = AddaOrderId()
        query.campaign_name = request.data.get('camp_name','adda52tmodd')
        query.id = request.data.get('order_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = AddaOrderId.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'order_id':query.id,
                'used_at':query.used_at,
        }
        if setUsed:
            query = AddaOrderId.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
            
class BambootautoAPI(APIView):
    def put(self, request):
        query = Bambootauto()
        query.campaign_name = request.data.get('camp_name','bambootauto')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Bambootauto.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = Bambootauto.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })
    
class PaynearbyAPI(APIView):
    def put(self, request):
        query = Paynearby()
        query.campaign_name = request.data.get('camp_name','paynearbyauto')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Paynearby.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = Paynearby.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })
 
class in2XAPI(APIView):
    def put(self, request):
        query = in2X()
        query.campaign_name = request.data.get('camp_name','in2xmodd')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = in2X.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = in2X.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })

class BluerewardsV2API(APIView):
    def put(self, request):
        query = BluerewardsV2()
        query.campaign_name = request.data.get('camp_name','bluerewardsauto')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = BluerewardsV2.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = BluerewardsV2.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
 
class SignnowAPI(APIView):
    def put(self, request):
        query = Signnow()
        query.campaign_name = request.data.get('camp_name','signnowmodd')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Signnow.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = Signnow.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })
 
class SixerDreamAPI(APIView):
    def put(self, request):
        query = SixerDream()
        query.campaign_name = request.data.get('camp_name','sixerdream11apktmodd')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = SixerDream.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = SixerDream.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
 
class WesternUnionAPI(APIView):
    def put(self, request):
        query = WesternUnion()
        query.campaign_name = request.data.get('camp_name','westernunion')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = WesternUnion.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = WesternUnion.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })
    
class StolotoUserIdAPI(APIView):
    def put(self, request):
        query = StolotoUserId()
        query.campaign_name = request.data.get('camp_name','stolototmodd')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = StolotoUserId.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = StolotoUserId.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })
    
class StolotoOrderIdAPI(APIView):
    def put(self, request):
        query = StolotoOrderId()
        query.campaign_name = request.data.get('camp_name','stolototmodd')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = StolotoOrderId.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = StolotoOrderId.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })
    
class PaysettUserIdAPI(APIView):
    def put(self, request):
        query = PaysettUserId()
        query.campaign_name = request.data.get('camp_name','paysettmodd')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = PaysettUserId.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = PaysettUserId.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })
    
class ShopeevnuidAPI(APIView):
    def put(self, request):
        query = ShopeevnUID()
        query.campaign_name = request.data.get('camp_name','shopeevntauto')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = ShopeevnUID.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = ShopeevnUID.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
    def post(self, request):
        query = ShopeevnUID.objects.order_by('-id').first()

        return Response({
            'id':query.id,
        })
 
class ShopeevnoidAPI(APIView):
    def put(self, request):
        query = ShopeevnOID()
        query.campaign_name = request.data.get('camp_name','shopeevntauto')
        query.id = request.data.get('order_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = ShopeevnOID.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'order_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = ShopeevnOID.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
    def post(self, request):
        query = ShopeevnOID.objects.order_by('-id').first()

        return Response({
            'id':query.id,
        })
 
class PoppoliveAPI(APIView):
    def put(self, request):
        query = Poppolive()
        query.campaign_name = request.data.get('camp_name','poppolivetmodd')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = Poppolive.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = Poppolive.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })

    def post(self, request):
        query = Poppolive.objects.order_by('-id').first()

        return Response({
            'id':query.id,
        })

class ShopeemyuidAPI(APIView):
    def put(self, request):
        query = ShopeemyUID()
        query.campaign_name = request.data.get('camp_name','shoppemytauto')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = ShopeemyUID.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = ShopeemyUID.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
    def post(self, request):
        query = ShopeemyUID.objects.order_by('-id').first()

        return Response({
            'id':query.id,
        })
 
class ShopeemyoidAPI(APIView):
    def put(self, request):
        query = ShopeemyOID()
        query.campaign_name = request.data.get('camp_name','shoppemytauto')
        query.id = request.data.get('order_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = ShopeemyOID.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'order_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = ShopeemyOID.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
    def post(self, request):
        query = ShopeemyOID.objects.order_by('-id').first()

        return Response({
            'id':query.id,
        })
 
class ShiprocketAPI(APIView):
    def put(self, request):
        query = Shiprocket()
        query.campaign_name = request.data.get('camp_name','shiprocketcouriert')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = Shiprocket.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = Shiprocket.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })

    def post(self, request):
        query = Shiprocket.objects.order_by('-id').first()

        return Response({
            'id':query.id,
        })

class NovawaterAPI(APIView):
    def put(self, request):
        query = Novawater()
        query.campaign_name = request.data.get('camp_name','novawateriosmodd')
        query.id = request.data.get('order_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = Novawater.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'order_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = Novawater.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })

    def post(self, request):
        query = Novawater.objects.order_by('-id').first()

        return Response({
            'id':query.id,
        })
    
class MoglixAPI(APIView):
    def put(self, request):
        query = Moglix()
        query.campaign_name = request.data.get('camp_name','moglixauto')
        query.id = request.data.get('order_id')
        query.extra_details = request.data.get('extra_details',{})
        query.price = request.data.get('price')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = Moglix.objects.filter(used_at=None, price__gte=Decimal('100.0'), price__lte=Decimal('30000.0')).order_by('-created_at')[0:50].first()
        
        data = {
                'order_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = Moglix.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })

    def post(self, request):
        query = Moglix.objects.order_by('-id').first()

        return Response({
            'id':query.id,
        })

class ViuAPI(APIView):
    def put(self, request):
        query = Viu()
        query.campaign_name = request.data.get('camp_name','viuhkmodd')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = Viu.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = Viu.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })

    def post(self, request):
        query = Viu.objects.order_by('-id').first()

        return Response({
            'id':query.id,
        })
    
   
class BetrAPI(APIView):
    def put(self, request):
        query = Betr()
        query.campaign_name = request.data.get('camp_name','betrmodd')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Betr.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = Betr.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })
    
class ShopeeidUIDAPI(APIView):
    def put(self, request):
        query = ShopeeidUID()
        query.campaign_name = request.data.get('camp_name','shopeeno1tauto')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = ShopeeidUID.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = ShopeeidUID.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
    def post(self, request):
        query = ShopeeidUID.objects.order_by('-id').first()

        return Response({
            'id':query.id,
        })
 
class DupoinAPI(APIView):
    def put(self, request):
        query = Dupoin()
        query.campaign_name = request.data.get('camp_name','dupoin')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = Dupoin.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = Dupoin.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
    def post(self, request):
        query = Dupoin.objects.order_by('-id').first()

        return Response({
            'id':query.id,
        })
 
class ShopeephUIDAPI(APIView):
    def put(self, request):
        query = ShopeephUID()
        query.campaign_name = request.data.get('camp_name','shopeeno1tauto')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = ShopeephUID.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = ShopeephUID.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
    def post(self, request):
        query = ShopeephUID.objects.order_by('-id').first()

        return Response({
            'id':query.id,
        })
    
class EpikoddAPI(APIView):
    def put(self, request):
        query = Epikodd()
        query.campaign_name = request.data.get('camp_name','epikoddiosmodd')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = Epikodd.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = Epikodd.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
    def post(self, request):
        query = Epikodd.objects.order_by('-id').first()

        return Response({
            'id':query.id,
        })
 
class StolotoAPI(APIView):
    def put(self, request):
        query = Stoloto()
        query.campaign_name = request.data.get('camp_name','stolototmodd')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.payment_data = request.data.get('extra_details',{}).get('payoutDate')
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = Stoloto.objects.filter(used_at=None).order_by('-payment_data')[0:50].first()
        
        data = {
                'user_id':query.id,
                # 'extra_details':query.extra_details, 
        }
        if setUsed:
            query = Stoloto.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
class CasinoplussAPI(APIView):
    def put(self, request):
        query = Casinopluss()
        query.campaign_name = request.data.get('camp_name','casinoplussmodd')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Casinopluss.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = Casinopluss.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })
    
class StorylandAPI(APIView):
    def put(self, request):
        query = Storyland()
        query.campaign_name = request.data.get('camp_name','storylandappmetrica')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Storyland.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = Storyland.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })
    
class HomiedevAPI(APIView):
    def put(self, request):
        query = Homiedev()
        query.campaign_name = request.data.get('camp_name','homiedevmodd')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Homiedev.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = Homiedev.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })
    
class TikettOIDAPI(APIView):
    def put(self, request):
        pass
        query = TikettOID()
        query.campaign_name = request.data.get('camp_name','tikettmodd')
        query.id = request.data.get('order_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        # time.sleep(random.randint(15,40))
        # setUsed = request.GET.get('set_used',True)
        # if setUsed and (setUsed == 'False' or setUsed == 'false'):
        #     setUsed = False

        with transaction.atomic():
            time.sleep(random.randint(10,30))
            query = TikettOID.objects.select_for_update().filter(used_at=None).order_by('-created_at').first()

            data = {'order_id':query.id}
            next_id = int(query.id) + random.randint(1,2)

            query = TikettOID.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

            

            new_ticket = TikettOID.objects.create(id=next_id,campaign_name=request.data.get('camp_name', 'tikettmodd'),used_at=None)

            return Response({
                'body':data,
            })
    
class ApnaTimeAPI(APIView):
    def put(self, request):
        query = ApnaTime()
        query.campaign_name = request.data.get('camp_name','apnatimeauto')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = ApnaTime.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = ApnaTime.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })
    
class MotiLalAPI(APIView):
    def put(self, request):
        query = MotiLal()
        query.campaign_name = request.data.get('camp_name','motilaloswaltmodd')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = MotiLal.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = MotiLal.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })
    
class FrendipayAPI(APIView):
    def put(self, request):
        query = Frendipay()
        query.campaign_name = request.data.get('camp_name','frendipayautoios')
        query.id = request.data.get('order_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Frendipay.objects.latest('created_at')
        
        data = {
                'order_id':query.id,
        }
        if setUsed:
            query = Frendipay.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })
   
class MagiclandAPI(APIView):
    def put(self, request):
        query = Magicland()
        query.campaign_name = request.data.get('camp_name','magiclandmodd')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = Magicland.objects.filter(used_at=None).first()
        
        data = {
                'user_id':query.id,
                # 'extra_details':query.extra_details, 
        }
        if setUsed:
            query = Magicland.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
   
class FoxtaleMiningAPI(APIView):
    def put(self, request):
        query = FoxtaleOrderId()
        query.campaign_name = request.data.get('camp_name','foxtalemodd')
        query.id = request.data.get('id')
        query.price = request.data.get('price')
        query.extra_details=request.data.get('extra_details',{})
        query.order_placed_date = request.data.get('order_placed_date', "")
        query.is_new = request.data.get('is_new', 0)
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

        date_ = datetime.now().strftime('%Y-%m-%d')

        if offer_id and random.randint(1,100)<=30:
            
            query = FoxtaleOrderId.objects.filter(created_at__lte=str(date_),offer_id=offer_id)
            print ("*"*100)
            print ("*"*100)
            if query:
                print ("old offer_id")

                from datetime import timedelta
                today = datetime.now().date()
                yesterday = today - timedelta(days=1)

                start_of_yesterday = datetime.combine(yesterday, datetime.min.time())
                end_of_yesterday = datetime.combine(yesterday, datetime.max.time())

                print (start_of_yesterday)
                print (end_of_yesterday)


                query = FoxtaleOrderId.objects.filter(order_placed_date__range=(start_of_yesterday, end_of_yesterday),used_at=None, price__gte=Decimal('1000.0'),**filter_dict).order_by('-created_at')[0:50].first()
                print ("*"*100)
                print ("Success")
                print (query)
                print ("*"*100)
        if not query:
            query = FoxtaleOrderId.objects.filter(order_placed_date__gte=str(date_),used_at=None, price__gte=Decimal('1000.0'),**filter_dict).order_by('-created_at')[0:50].first()
        
        data = {
                'id':query.id,
                'used_at':query.used_at,
                'extra_details':query.extra_details,
                'price': query.price
        }
        if setUsed:
            query = FoxtaleOrderId.objects.filter(id=data.get('id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })

    def post(self, request):
        query = FoxtaleOrderId.objects.order_by('-id').first()

        return Response({
            'id':query.id,
        })

class HoteltonightAPI(APIView):
    def put(self, request):
        query = Hoteltonight()
        query.campaign_name = request.data.get('camp_name','hoteltonightautoios')
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
        
        query = Hoteltonight.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'id':query.id,
                'used_at':query.used_at,
                'extra_details':query.extra_details,
        }
        if setUsed:
            query = Hoteltonight.objects.filter(id=data.get('id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })

    def post(self, request):
        query = Hoteltonight.objects.order_by('-id').first()

        return Response({
            'id':query.id,
        })
    
class stolotoCIFAPI(APIView):

    def get(self, request):
        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        user_id = request.GET.get('user_id', '')
        payment_date = request.GET.get('payment_date', '')

        query = stolotoCIF.objects.filter(id=user_id)

        if query:
            return Response({
            'body':False,
        })

        else:
            query = stolotoCIF()
            query.campaign_name = "stoloto"
            query.channel = channel
            query.network = network
            query.offer_id = offer_id
            query.id = user_id
            query.payment_date=payment_date
            try:
                query.save()
                return Response({'body':True})
            except Exception as e:
                import traceback
                traceback.print_exc()
                return Response({
                })

class YesmadamAPI(APIView):
    def put(self, request):
        query = Yesmadam()
        query.campaign_name = request.data.get('camp_name','yesmadammodd')
        query.id = request.data.get('id')
        query.price = request.data.get('price')
        query.extra_details=request.data.get('extra_details',{})
        query.booking_date = request.data.get('booking_date', "")
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

        today = datetime.now().strftime('%Y-%m-%d')
        r = random.randint(1,100)
        if r<= 20:
            min_price = '250.0'
            max_price = '500.0'
        elif r<= 50:
            min_price = '500.0'
            max_price = '1000.0'
        else:
            min_price = '1000.0'
            max_price = '10000.0'

        query = Yesmadam.objects.filter(used_at=None, price__gte=Decimal(min_price), price__lte=Decimal(max_price),**filter_dict).order_by('-created_at')[0:50].first()

        if not query:
            query = Yesmadam.objects.filter(used_at=None, **filter_dict).order_by('-created_at')[0:50].first()
        
        data = {
                'id':query.id,
                'used_at':query.used_at,
                'extra_details':query.extra_details,
                'price': query.price
        }
        if setUsed:
            query = Yesmadam.objects.filter(id=data.get('id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })

    def post(self, request):
        query = Yesmadam.objects.order_by('-id').first()

        return Response({
            'id':query.id,
        })

class BeymenAPI(APIView):
    def put(self, request):
        query = Beymen()
        query.campaign_name = request.data.get('camp_name','beymenclubiosauto')
        query.id = request.data.get('order_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Beymen.objects.latest('created_at')
        
        data = {
                'order_id':query.id,
        }
        if setUsed:
            query = Beymen.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })

class BncAPI(APIView):
    def put(self, request):
        query = Bncauto()
        query.campaign_name = request.data.get('camp_name','bncauto')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Bncauto.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = Bncauto.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })

class KfcAPI(APIView):
    def put(self, request):
        query = Kfcmexico()
        query.campaign_name = request.data.get('camp_name','kfcmexicotmodd')
        query.id = request.data.get('order_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Kfcmexico.objects.latest('created_at')
        
        data = {
                'order_id':query.id,
        }
        if setUsed:
            query = Kfcmexico.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })

class JazzcashAPI(APIView):

    def put(self, request):
        query = Jazzcash()
        query.campaign_name = request.data.get('camp_name','jazzcashmodd')
        query.id = request.data.get('user_id')
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
        channel = request.GET.get('channel',True)
        network = request.GET.get('network',True)
        offer_id = request.GET.get('offer_id',True)
        if offer_id.isdecimal():
            return Response({'body':'error','message':'panel offer not allowed'})

        
        # if not channel or not network or not offer_id:
        #     return Response({
        #                 'body':'error',
        #                 'message':'channel,offer_id,network id missing.'
        #             })
        
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        exclude_dict = {}
        exclude_dict['channel_list__contains'] = channel
        # exclude_dict['network_list__contains'] = network
        # exclude_dict['offer_id_list__contains'] = offer_id

        exclude_dict_1 = {}

        query_list = Jazzcash.objects.filter(used_at=None).exclude(**exclude_dict_1).order_by('-created_at')[0:25].all()        
        if not query_list:
            query_list = Jazzcash.objects.exclude(**exclude_dict).order_by('-created_at')[0:25].all()
        
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
                        'user_id':query.id,
                }
                if setUsed:
                    query = Jazzcash.objects.filter(id=data.get('user_id')).update(
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

class PetbookAPI(APIView):
    def put(self, request):
        query = Petbook()
        query.campaign_name = request.data.get('camp_name','petbookappmetrica')
        query.id = request.data.get('order_id')
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
        
        query = Petbook.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'order_id':query.id,
                'used_at':query.used_at,
        }
        if setUsed:
            query = Petbook.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })

    def post(self, request):
        query = Petbook.objects.order_by('-id').first()

        return Response({
            'id':query.id,
        })


class tejimaandiAPI(APIView):
    def put(self, request):
        query = tejimaandi()
        query.campaign_name = request.data.get('camp_name','tejimaandiauto')
        query.id = request.data.get('user_id')
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
        
        query = tejimaandi.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'used_at':query.used_at,
        }
        if setUsed:
            query = tejimaandi.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })

    def post(self, request):
        query = tejimaandi.objects.order_by('-id').first()

        return Response({
            'id':query.id,
        })


class TejimaandinewAPI(APIView):

    def put(self, request):
        query = Tejimaandinew()
        query.campaign_name = request.data.get('camp_name','tejimaandiauto')
        query.id = request.data.get('user_id')
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
        channel = request.GET.get('channel',True)
        network = request.GET.get('network',True)
        offer_id = request.GET.get('offer_id',True)
        if offer_id.isdecimal():
            return Response({'body':'error','message':'panel offer not allowed'})

        
        # if not channel or not network or not offer_id:
        #     return Response({
        #                 'body':'error',
        #                 'message':'channel,offer_id,network id missing.'
        #             })
        
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        exclude_dict = {}
        exclude_dict['channel_list__contains'] = channel
        # exclude_dict['network_list__contains'] = network
        # exclude_dict['offer_id_list__contains'] = offer_id

        exclude_dict_1 = {}

        query_list = Tejimaandinew.objects.filter(used_at=None).exclude(**exclude_dict_1).order_by('-created_at')[0:25].all()        
        if not query_list:
            query_list = Tejimaandinew.objects.exclude(**exclude_dict).order_by('-created_at')[0:25].all()
        
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
                        'user_id':query.id,
                }
                if setUsed:
                    query = Tejimaandinew.objects.filter(id=data.get('user_id')).update(
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


class PaytmmoneytAPI(APIView):
    def put(self, request):
        query = Paytmmoneyt()
        query.campaign_name = request.data.get('camp_name','paytmmoneytmodd')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Paytmmoneyt.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = Paytmmoneyt.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })

class AnqgoldrewardsAPI(APIView):
    def put(self, request):
        query = Anqgoldrewards()
        query.campaign_name = request.data.get('camp_name','anqgoldrewardsmodd')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Anqgoldrewards.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = Anqgoldrewards.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })

class AnqgoldrewardscuidAPI(APIView):
    def put(self, request):
        query = Anqgoldrewardscuid()
        query.campaign_name = request.data.get('camp_name','anqgoldrewardsmodd')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Anqgoldrewardscuid.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = Anqgoldrewardscuid.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })

class AnqgoldrewardsoidAPI(APIView):
    def put(self, request):
        query = Anqgoldrewardsoid()
        query.campaign_name = request.data.get('camp_name','anqgoldrewardsmodd')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Anqgoldrewardsoid.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = Anqgoldrewardsoid.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })

class OkeyvipAPI(APIView):
    def put(self, request):
        query = OkeyvipMining()
        query.campaign_name = request.data.get('camp_name','okeyvipmodd')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None

        try:
            query.save()
        except Exception as e:
            print (e)
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = OkeyvipMining.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = OkeyvipMining.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
    def post(self, request):
        query = OkeyvipMining.objects.order_by('-id').first()

        return Response({
            'id':query.id,
        })

class MoneymetmodduidAPI(APIView):
    def put(self, request):
        query = Moneymetmodduid()
        query.campaign_name = request.data.get('camp_name','anqgoldrewardsmodd')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Moneymetmodduid.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = Moneymetmodduid.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })

class ImagineartAPI(APIView):
    def put(self, request):
        query = Imagineart()
        query.campaign_name = request.data.get('camp_name','anqgoldrewardsmodd')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Imagineart.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = Imagineart.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })



class ParimatchthAPI(APIView):
    def put(self, request):
        query = Parimatchth()
        query.campaign_name = request.data.get('camp_name','parimatchthmodd')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = Parimatchth.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = Parimatchth.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
    def post(self, request):
        query = Parimatchth.objects.order_by('-id').first()

        return Response({
            'id':query.id,
        })

class MeliveAPI(APIView):
    def put(self, request):
        query = Melive()
        query.campaign_name = request.data.get('camp_name','melivemodd')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = Melive.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = Melive.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
    def post(self, request):
        query = Melive.objects.order_by('-id').first()

        return Response({
            'id':query.id,
        })

class MetliveAPI(APIView):
    def put(self, request):
        query = Metlive()
        query.campaign_name = request.data.get('camp_name','metlivemodd')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = Metlive.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = Metlive.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
    def post(self, request):
        query = Metlive.objects.order_by('-id').first()

        return Response({
            'id':query.id,
        })
    
class MetliveUidAPI(APIView):
    def put(self, request):
        query = MetliveUID()
        query.campaign_name = request.data.get('camp_name','metlivemodd')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.country =  request.data.get('country')
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = MetliveUID.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = MetliveUID.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
    def post(self, request):
        query = MetliveUID.objects.order_by('-id').first()

        return Response({
            'id':query.id,
        })
    
class MeliveUidAPI(APIView):
    def put(self, request):
        query = MeliveUID()
        query.campaign_name = request.data.get('camp_name','melivemodd')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.country =  request.data.get('country')
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = MeliveUID.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = MeliveUID.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
    def post(self, request):
        query = MeliveUID.objects.order_by('-id').first()

        return Response({
            'id':query.id,
        })

class OpayAPI(APIView):

    def put(self, request):
        query = Opay()
        query.campaign_name = request.data.get('camp_name','opaymodd')
        query.id = request.data.get('user_id')
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
        channel = request.GET.get('channel',True)
        network = request.GET.get('network',True)
        offer_id = request.GET.get('offer_id',True)
        if offer_id.isdecimal():
            return Response({'body':'error','message':'panel offer not allowed'})

        
        # if not channel or not network or not offer_id:
        #     return Response({
        #                 'body':'error',
        #                 'message':'channel,offer_id,network id missing.'
        #             })
        
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        exclude_dict = {}
        exclude_dict['channel_list__contains'] = channel
        # exclude_dict['network_list__contains'] = network
        # exclude_dict['offer_id_list__contains'] = offer_id

        exclude_dict_1 = {}

        query_list = Opay.objects.filter(used_at=None).exclude(**exclude_dict_1).order_by('-created_at')[0:25].all()        
        if not query_list:
            query_list = Opay.objects.exclude(**exclude_dict).order_by('-created_at')[0:25].all()
        
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
                        'user_id':query.id,
                }
                if setUsed:
                    query = Opay.objects.filter(id=data.get('user_id')).update(
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


class BevietnamesAPI(APIView):
    def put(self, request):
        query = Bevietnames()
        query.campaign_name = request.data.get('camp_name','bevietnamesmodd')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Bevietnames.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = Bevietnames.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })
    
class BoostAPI(APIView):

    def put(self, request):
        query = Boost()
        query.campaign_name = request.data.get('camp_name','boostappmyauto')
        query.id = request.data.get('user_id')
        query.phone = request.data.get('phone')
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
        channel = request.GET.get('channel',True)
        network = request.GET.get('network',True)
        offer_id = request.GET.get('offer_id',True)
        if offer_id.isdecimal():
            return Response({'body':'error','message':'panel offer not allowed'})

        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        exclude_dict = {}
        exclude_dict['channel_list__contains'] = channel
        # exclude_dict['network_list__contains'] = network
        # exclude_dict['offer_id_list__contains'] = offer_id

        exclude_dict_1 = {}

        query_list = Boost.objects.filter(used_at=None).exclude(**exclude_dict_1).order_by('-created_at')[0:25].all()        
        if not query_list:
            query_list = Boost.objects.exclude(**exclude_dict).order_by('-created_at')[0:25].all()
        
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
                        'user_id':query.id,
                }
                if setUsed:
                    query = Boost.objects.filter(id=data.get('user_id')).update(
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

class CimbthaiAPI(APIView):
    def put(self, request):
        query = Cimbthai()
        query.campaign_name = request.data.get('camp_name','cimbthaimodd')
        query.id = request.data.get('order_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Cimbthai.objects.latest('created_at')
        
        data = {
                'order_id':query.id,
        }
        if setUsed:
            query = Cimbthai.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })

class MyauchanAPI(APIView):
    def put(self, request):
        query = Myauchan()
        query.campaign_name = request.data.get('camp_name','myauchanappmetrica')
        query.id = request.data.get('order_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Myauchan.objects.latest('created_at')
        
        data = {
                'order_id':query.id,
        }
        if setUsed:
            query = Myauchan.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })


class IkeaAPI(APIView):
    def put(self, request):
        query = Ikea()
        query.campaign_name = request.data.get('camp_name','cimbthaimodd')
        query.id = request.data.get('order_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Ikea.objects.latest('created_at')
        
        data = {
                'order_id':query.id,
        }
        if setUsed:
            query = Ikea.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })

class ShopeebrUIDAPI(APIView):
    def put(self, request):
        query = ShopeebrUID()
        query.campaign_name = request.data.get('camp_name','shopeeno1tauto')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = ShopeebrUID.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = ShopeebrUID.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
    def post(self, request):
        query = ShopeebrUID.objects.order_by('-id').first()

        return Response({
            'id':query.id,
        })

class ShopeethUIDAPI(APIView):
    def put(self, request):
        query = ShopeethUID()
        query.campaign_name = request.data.get('camp_name','shopeet')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = ShopeethUID.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = ShopeethUID.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
    def post(self, request):
        query = ShopeethUID.objects.order_by('-id').first()

        return Response({
            'id':query.id,
        })

class ShopeethiosUIDAPI(APIView):
    def put(self, request):
        query = ShopeethiosUID()
        query.campaign_name = request.data.get('camp_name','shopeetiosmodd')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = ShopeethiosUID.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = ShopeethiosUID.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
    def post(self, request):
        query = ShopeethiosUID.objects.order_by('-id').first()

        return Response({
            'id':query.id,
        })


class AnqgoldrewardsnewAPI(APIView):
    def put(self, request):
        query = Anqgoldrewardsnew()
        query.campaign_name = request.data.get('camp_name','anqgoldrewardsmodd')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = Anqgoldrewardsnew.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = Anqgoldrewardsnew.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
    def post(self, request):
        query = Anqgoldrewardsnew.objects.order_by('-id').first()

        return Response({
            'id':query.id,
        })


class MyfriendUIDAPI(APIView):
    def put(self, request):
        query = MyfriendUID()
        query.campaign_name = request.data.get('camp_name','myfriendauto')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = MyfriendUID.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = MyfriendUID.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
    def post(self, request):
        query = MyfriendUID.objects.order_by('-id').first()

        return Response({
            'id':query.id,
        })

class MyfriendOIDAPI(APIView):
    def put(self, request):
        query = MyfriendOID()
        query.campaign_name = request.data.get('camp_name','myfriendauto')
        query.id = request.data.get('order_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = MyfriendOID.objects.latest('created_at')
        
        data = {
                'order_id':query.id,
        }
        if setUsed:
            query = MyfriendOID.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })


class MambaUIDAPI(APIView):
    def put(self, request):
        query = MambaUID()
        query.campaign_name = request.data.get('camp_name','mambamodd')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = MambaUID.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = MambaUID.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
    def post(self, request):
        query = MambaUID.objects.order_by('-id').first()

        return Response({
            'id':query.id,
        })

class GalaxyChatAPI(APIView):

    def put(self, request):
        query = GalaxyChat()
        query.campaign_name = request.data.get('camp_name','galaxychatappmetrica')
        query.id = request.data.get('user_id')
        query.username = request.data.get('user_name')
        query.city =  request.data.get('city')
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
        channel = request.GET.get('channel',True)
        network = request.GET.get('network',True)
        offer_id = request.GET.get('offer_id',True)
        if offer_id.isdecimal():
            return Response({'body':'error','message':'panel offer not allowed'})
        

        if channel in ['adshustle', 'appsfollowing', 'vestaapps', "appsatiate"]:
            BT = "BT2"
            other_BT = "BT3"
        elif channel in ['mobpine', '77ads', 'appamplify']:
            BT = "BT3"
            other_BT = "BT2"
        
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        # exclude_dict = {}
        # exclude_dict_1 = {}
        # # exclude_dict['channel_list__contains'] = channel
        # # exclude_dict['network_list__contains'] = network
        # # exclude_dict['offer_id_list__contains'] = offer_id
        # exclude_dict['bt_list__contains'] = BT
        # exclude_dict_1['bt_list__contains'] = other_BT

        # exclude_dict_1 = {}
            
        # total_ids_used = GalaxyChat.objects.filter(used_at__startswith=datetime.now().strftime('%Y-%m-%d')).exclude(**exclude_dict_1).count()     

        # russian_cities = ['Abakan', 'Abaza', 'Abdulino', 'Abinsk', 'Achinsk', 'Adygeysk', 'Agidel', 'Agryz', 'Ak-Dovurak', 'Akhtubinsk', 'Aksay', 'Alagir', 'Alapayevsk', 'Alatyr', 'Aldan', 'Aleksin', 'Alexandrov', 'Alexandrovsk', 'Alexandrovsk-Sakhalinsky', 'Alexeyevka', 'Aleysk', 'Almetyevsk', 'Alzamay', 'Amursk', 'Anadyr', 'Anapa', 'Andreapol', 'Angarsk', 'Aniva', 'Anzhero-Sudzhensk', 'Apatity', 'Aprelevka', 'Apsheronsk', 'Aramil', 'Ardatov', 'Ardon', 'Argun', 'Arkadak', 'Arkhangelsk', 'Armavir', 'Arsenyev', 'Arsk', 'Artyom', 'Artyomovsk', 'Artyomovsky', 'Arzamas', 'Asbest', 'Asha', 'Asino', 'Astrakhan', 'Atkarsk', 'Aznakayevo', 'Azov', 'Babayevo', 'Babushkin', 'Bagrationovsk', 'Bakal', 'Baksan', 'Balabanovo', 'Balakhna', 'Balakovo', 'Balashikha', 'Balashov', 'Baley', 'Baltiysk', 'Barabinsk', 'Barnaul', 'Barysh', 'Bataysk', 'Bavly', 'Baykalsk', 'Baymak', 'Belaya Kalitva', 'Belaya Kholunitsa', 'Belebey', 'Belgorod', 'Belinsky', 'Belogorsk', 'Belokurikha', 'Belomorsk', 'Belorechensk', 'Beloretsk', 'Belousovo', 'Belovo', 'Beloyarsky', 'Belozersk', 'Bely', 'Belyov', 'Berdsk', 'Berezniki', 'Berezovsky', 'Beslan', 'Bezhetsk', 'Bikin', 'Bilibino', 'Birobidzhan', 'Birsk', 'Biryuch', 'Biryusinsk', 'Biysk', 'Blagodarny', 'Blagoveshchensk', 'Bobrov', 'Bodaybo', 'Bogdanovich', 'Bogoroditsk', 'Bogorodsk', 'Bogotol', 'Boguchar', 'Boksitogorsk', 'Bolgar', 'Bolkhov', 'Bologoye', 'Bolokhovo', 'Bolotnoye', 'Bolshoy Kamen', 'Bor', 'Borisoglebsk', 'Borodino', 'Borovichi', 'Borovsk', 'Borzya', 'Bratsk', 'Bronnitsy', 'Bryansk', 'Budyonnovsk', 'Bugulma', 'Buguruslan', 'Buinsk', 'Buturlinovka', 'Buy', 'Buynaksk', 'Buzuluk', 'Chadan', 'Chapayevsk', 'Chaplygin', 'Chaykovsky', 'Chebarkul', 'Cheboksary', 'Chegem', 'Chekalin', 'Chekhov', 'Chelyabinsk', 'Cherdyn', 'Cheremkhovo', 'Cherepanovo', 'Cherepovets', 'Cherkessk', 'Chernogolovka', 'Chernogorsk', 'Chernushka', 'Chernyakhovsk', 'Chistopol', 'Chita', 'Chkalovsk', 'Chudovo', 'Chukhloma', 'Chulym', 'Chusovoy', 'Chyormoz', 'Dagestanskiye Ogni', 'Dalmatovo', 'Dalnegorsk', 'Dalnerechensk', 'Danilov', 'Dankov', 'Davlekanovo', 'Dedovsk', 'Degtyarsk', 'Demidov', 'Derbent', 'Desnogorsk', 'Digora', 'Dimitrovgrad', 'Divnogorsk', 'Dmitriyev', 'Dmitrov', 'Dmitrovsk', 'Dno', 'Dobryanka', 'Dolgoprudny', 'Dolinsk', 'Domodedovo', 'Donetsk', 'Donskoy', 'Dorogobuzh', 'Drezna', 'Dubna', 'Dubovka', 'Dudinka', 'Dukhovshchina', 'Dyatkovo', 'Dyurtyuli', 'Dzerzhinsk', 'Dzerzhinsky', 'Elektrogorsk', 'Elektrostal', 'Elektrougli', 'Elista', 'Engels', 'Ertil', 'Fatezh', 'Fokino', 'Frolovo', 'Fryazino', 'Furmanov', 'Gadzhiyevo', 'Gagarin', 'Galich', 'Gatchina', 'Gavrilov Posad', 'Gavrilov-Yam', 'Gay', 'Gdov', 'Gelendzhik', 'Georgiyevsk', 'Glazov', 'Golitsyno', 'Gorbatov', 'Gorno-Altaysk', 'Gornozavodsk', 'Gornyak', 'Gorodets', 'Gorodishche', 'Gorodovikovsk', 'Gorokhovets', 'Goryachy Klyuch', 'Grayvoron', 'Gremyachinsk', 'Grozny', 'Gryazi', 'Gryazovets', 'Gubakha', 'Gubkin', 'Gubkinsky', 'Gudermes', 'Gukovo', 'Gulkevichi', 'Guryevsk', 'Gus-Khrustalny', 'Gusev', 'Gusinoozyorsk', 'Gvardeysk', 'Igarka', 'Ilansky', 'Innopolis', 'Insar', 'Inta', 'Inza', 'Ipatovo', 'Irbit', 'Irkutsk', 'Ishim', 'Ishimbay', 'Isilkul', 'Iskitim', 'Istra', 'Ivangorod', 'Ivanovo', 'Ivanteyevka', 'Ivdel', 'Izberbash', 'Izhevsk', 'Izobilny', 'Kachkanar', 'Kadnikov', 'Kalach', 'Kalach-na-Donu', 'Kalachinsk', 'Kaliningrad', 'Kalininsk', 'Kaltan', 'Kaluga', 'Kalyazin', 'Kambarka', 'Kamen-na-Obi', 'Kamenka', 'Kamennogorsk', 'Kamensk-Shakhtinsky', 'Kamensk-Uralsky', 'Kameshkovo', 'Kamyshin', 'Kamyshlov', 'Kamyzyak', 'Kanash', 'Kandalaksha', 'Kansk', 'Karabanovo', 'Karabash', 'Karabulak', 'Karachayevsk', 'Karachev', 'Karasuk', 'Kargat', 'Kargopol', 'Karpinsk', 'Kartaly', 'Kashin', 'Kashira', 'Kasimov', 'Kasli', 'Kaspiysk', 'Katav-Ivanovsk', 'Kataysk', 'Kazan', 'Kedrovy', 'Kem', 'Kemerovo', 'Khabarovsk', 'Khadyzhensk', 'Khanty-Mansiysk', 'Kharabali', 'Kharovsk', 'Khasavyurt', 'Khilok', 'Khimki', 'Kholm', 'Kholmsk', 'Khotkovo', 'Khvalynsk', 'Kimovsk', 'Kimry', 'Kinel', 'Kineshma', 'Kingisepp', 'Kirensk', 'Kireyevsk', 'Kirillov', 'Kirishi', 'Kirov', 'Kirovgrad', 'Kirovo-Chepetsk', 'Kirovsk', 'Kirs', 'Kirsanov', 'Kirzhach', 'Kiselyovsk', 'Kislovodsk', 'Kizel', 'Kizilyurt', 'Kizlyar', 'Klimovsk', 'Klin', 'Klintsy', 'Knyaginino', 'Kodinsk', 'Kogalym', 'Kokhma', 'Kola', 'Kolchugino', 'Kologriv', 'Kolomna', 'Kolpashevo', 'Kolpino', 'Kommunar', 'Komsomolsk', 'Komsomolsk-on-Amur', 'Konakovo', 'Kondopoga', 'Kondrovo', 'Konstantinovsk', 'Kopeysk', 'Korablino', 'Korenovsk', 'Korkino', 'Korocha', 'Korolyov', 'Vokhma', 'Korsakov', 'Koryazhma', 'Kosteryovo', 'Kostomuksha', 'Kostroma', 'Kotelnich', 'Kotelniki', 'Kotelnikovo', 'Kotlas', 'Kotovo', 'Kotovsk', 'Kovdor', 'Kovrov', 'Kovylkino', 'Kozelsk', 'Kozlovka', 'Kozmodemyansk', 'Krasavino', 'Krasnoarmeysk', 'Krasnodar', 'Krasnogorsk', 'Krasnokamensk', 'Krasnokamsk', 'Krasnoslobodsk', 'Krasnoturyinsk', 'Krasnoufimsk', 'Krasnouralsk', 'Krasnovishersk', 'Krasnoyarsk', 'Krasnoye Selo', 'Krasnozavodsk', 'Krasnoznamensk', 'Krasny Kholm', 'Krasny Kut', 'Krasny Sulin', 'Kremyonki', 'Kronstadt', 'Kropotkin', 'Krymsk', 'Kstovo', 'Kubinka', 'Kudymkar', 'Kulebaki', 'Kumertau', 'Kungur', 'Kupino', 'Kurchatov', 'Kurgan', 'Kurganinsk', 'Kurilsk', 'Kurlovo', 'Kurovskoye', 'Kursk', 'Kurtamysh', 'Kusa', 'Kushva', 'Kuvandyk', 'Kuvshinovo', 'Kuybyshev', 'Kuznetsk', 'Kyakhta', 'Kyshtym', 'Kyzyl', 'Labinsk', 'Labytnangi', 'Ladushkin', 'Lagan', 'Laishevo', 'Lakhdenpokhya', 'Lakinsk', 'Langepas', 'Lebedyan', 'Leninogorsk', 'Leninsk', 'Leninsk-Kuznetsky', 'Lensk', 'Lermontov', 'Lesnoy', 'Lesosibirsk', 'Lesozavodsk', 'Lgov', 'Likhoslavl', 'Likino-Dulyovo', 'Lipetsk', 'Lipki', 'Liski', 'Livny', 'Lobnya', 'Lodeynoye Pole', 'Lomonosov', 'Losino-Petrovsky', 'Luga', 'Lukhovitsy', 'Lukoyanov', 'Luza', 'Lyantor', 'Lyskovo', 'Lysva', 'Lytkarino', 'Lyuban', 'Lyubertsy', 'Lyubim', 'Lyudinovo', 'Magadan', 'Magas', 'Magnitogorsk', 'Makarov', 'Makaryev', 'Makhachkala', 'Makushino', 'Malaya Vishera', 'Malgobek', 'Malmyzh', 'Maloarkhangelsk', 'Maloyaroslavets', 'Mamadysh', 'Mamonovo', 'Manturovo', 'Mariinsk', 'Mariinsky Posad', 'Marks', 'Maykop', 'Maysky', 'Mednogorsk', 'Medvezhyegorsk', 'Medyn', 'Megion', 'Melenki', 'Meleuz', 'Mendeleyevsk', 'Menzelinsk', 'Meshchovsk', 'Mezen', 'Mezhdurechensk', 'Mezhgorye', 'Mglin', 'Miass', 'Michurinsk', 'Mikhaylov', 'Mikhaylovka', 'Mikhaylovsk', 'Mikun', 'Millerovo', 'Mineralnye Vody', 'Minusinsk', 'Minyar', 'Mirny', 'Mogocha', 'Monchegorsk', 'Morozovsk', 'Morshansk', 'Mosalsk', 'Moscow', 'Moskovsky', 'Mozdok', 'Mozhaysk', 'Mozhga', 'Mtsensk', 'Murashi', 'Muravlenko', 'Murmansk', 'Murom', 'Myshkin', 'Myski', 'Mytishchi', 'Naberezhnye Chelny', 'Nadym', 'Nakhodka', 'Nalchik', 'Narimanov', 'Naro-Fominsk', 'Nartkala', 'Naryan-Mar', 'Naukan', 'Navashino', 'Navoloki', 'Nazarovo', 'Nazran', 'Nazyvayevsk', 'Neftegorsk, Samara Oblast', 'Neftekamsk', 'Neftekumsk', 'Nefteyugansk', 'Nelidovo', 'Neman', 'Nerchinsk', 'Nerekhta', 'Neryungri', 'Nesterov', 'Nevel', 'Nevelsk', 'Nevinnomyssk', 'Nevyansk', 'Neya', 'Nikolayevsk', 'Nikolayevsk-on-Amur', 'Nikolsk', 'Nikolskoye', 'Nizhnekamsk', 'Nizhneudinsk', 'Nizhnevartovsk', 'Nizhniye Sergi', 'Nizhny Lomov', 'Nizhny Novgorod', 'Nizhny Tagil', 'Nizhnyaya Salda', 'Nizhnyaya Tura', 'Noginsk', 'Nolinsk', 'Norilsk', 'Novaya Ladoga', 'Novaya Lyalya', 'Novoalexandrovsk', 'Novoaltaysk', 'Novoanninsky', 'Novocheboksarsk', 'Novocherkassk', 'Novodvinsk', 'Novokhopyorsk', 'Novokubansk', 'Novokuybyshevsk', 'Novokuznetsk', 'Novomichurinsk', 'Novomoskovsk', 'Novopavlovsk', 'Novorossiysk', 'Novorzhev', 'Novoshakhtinsk', 'Novosibirsk', 'Novosil', 'Novosokolniki', 'Novotroitsk', 'Novoulyanovsk', 'Novouralsk', 'Novouzensk', 'Novovoronezh', 'Novozybkov', 'Novy Oskol', 'Novy Urengoy', 'Noyabrsk', 'Nurlat', 'Nyagan', 'Nyandoma', 'Nyazepetrovsk', 'Nytva', 'Nyurba', 'Ob', 'Obluchye', 'Obninsk', 'Oboyan', 'Ochyor', 'Odintsovo', 'Okha', 'Okhansk', 'Oktyabrsk', 'Oktyabrsky', 'Okulovka', 'Olenegorsk', 'Olonets', 'Olyokminsk', 'Omsk', 'Omutninsk', 'Onega', 'Opochka', 'Orekhovo-Zuyevo', 'Orenburg', 'Orlov', 'Orsk', 'Oryol', 'Osa', 'Osinniki', 'Ostashkov', 'Ostrogozhsk', 'Ostrov', 'Ostrovnoy', 'Otradnoye', 'Otradny', 'Ozherelye', 'Ozyorsk', 'Ozyory', 'Pallasovka', 'Partizansk', 'Pavlovo', 'Pavlovsk', 'Pavlovsky Posad', 'Pechora', 'Pechory', 'Penza', 'Pereslavl-Zalessky', 'Peresvet', 'Perevoz', 'Perm', 'Pervomaysk', 'Pervouralsk', 'Pestovo', 'Petergof', 'Petropavlovsk-Kamchatsky', 'Petrov Val', 'Petrovsk', 'Petrovsk-Zabaykalsky', 'Petrozavodsk', 'Petukhovo', 'Petushki', 'Pevek', 'Pikalyovo', 'Pionersky', 'Pitkyaranta', 'Plast', 'Plavsk', 'Plyos', 'Pochep', 'Pochinok', 'Podolsk', 'Podporozhye', 'Pokachi', 'Pokhvistnevo', 'Pokrov', 'Pokrovsk', 'Polessk', 'Polevskoy', 'Polyarny', 'Polyarnye Zori', 'Polysayevo', 'Porkhov', 'Poronaysk', 'Poshekhonye', 'Povorino', 'Pravdinsk', 'Primorsk', 'Primorsko-Akhtarsk', 'Priozersk', 'Privolzhsk', 'Prokhladny', 'Prokopyevsk', 'Proletarsk', 'Protvino', 'Pskov', 'Puchezh', 'Pudozh', 'Pugachyov', 'Pushchino', 'Pushkin', 'Pushkino', 'Pustoshka', 'Pyatigorsk', 'Pyt-Yakh', 'Pytalovo', 'Raduzhny', 'Ramenskoye', 'Rasskazovo', 'Raychikhinsk', 'Reutov', 'Revda', 'Rezh', 'Rodniki', 'Roshal', 'Roslavl', 'Rossosh', 'Rostov', 'Rostov-on-Don', 'Rtishchevo', 'Rubtsovsk', 'Rudnya', 'Ruza', 'Ruzayevka', 'Ryazan', 'Ryazhsk', 'Rybinsk', 'Rybnoye', 'Rylsk', 'Rzhev', 'Safonovo', 'Saint Petersburg', 'Salair', 'Salavat', 'Salekhard', 'Salsk', 'Samara', 'Saransk', 'Sarapul', 'Saratov', 'Sarov', 'Sasovo', 'Satka', 'Sayanogorsk', 'Sayansk', 'Sebezh', 'Segezha', 'Seltso', 'Semikarakorsk', 'Semiluki', 'Semyonov', 'Sengiley', 'Serafimovich', 'Serdobsk', 'Sergach', 'Sergiyev Posad', 'Serov', 'Serpukhov', 'Sertolovo', 'Sestroretsk', 'Severo-Kurilsk', 'Severobaykalsk', 'Severodvinsk', 'Severomorsk', 'Severouralsk', 'Seversk', 'Sevsk', 'Shadrinsk', 'Shagonar', 'Shakhty', 'Shakhtyorsk', 'Shakhunya', 'Shali', 'Sharya', 'Sharypovo', 'Shatsk', 'Shatura', 'Shcherbinka', 'Shchigry', 'Shchuchye', 'Shchyokino', 'Shchyolkovo', 'Shebekino', 'Shelekhov', 'Shenkursk', 'Shikhany', 'Shilka', 'Shimanovsk', 'Shlisselburg', 'Shumerlya', 'Shumikha', 'Shuya', 'Sibay', 'Sim', 'Skopin', 'Skovorodino', 'Slantsy', 'Slavgorod', 'Slavsk', 'Slavyansk-na-Kubani', 'Slobodskoy', 'Slyudyanka', 'Smolensk', 'Snezhinsk', 'Snezhnogorsk', 'Sobinka', 'Sochi', 'Sokol', 'Sokolniki', 'Sol-Iletsk', 'Soligalich', 'Solikamsk', 'Solnechnogorsk', 'Soltsy', 'Solvychegodsk', 'Sorochinsk', 'Sorsk', 'Sortavala', 'Sosensky', 'Sosnogorsk', 'Sosnovka', 'Sosnovoborsk', 'Sosnovy Bor', 'Sovetsk', 'Sovetskaya Gavan', 'Sovetsky', 'Spas-Demensk', 'Spas-Klepiki', 'Spassk', 'Spassk-Dalny', 'Spassk-Ryazansky', 'Srednekolymsk', 'Sredneuralsk', 'Sretensk', 'Staraya Kupavna', 'Staraya Russa', 'Staritsa', 'Starodub', 'Stary Oskol', 'Stavropol', 'Sterlitamak', 'Strezhevoy', 'Stroitel', 'Strunino', 'Stupino', 'Sudogda', 'Sudzha', 'Sukhinichi', 'Sukhoy Log', 'Suoyarvi', 'Surazh', 'Surgut', 'Surovikino', 'Sursk', 'Susuman', 'Suvorov', 'Suzdal', 'Svetlogorsk', 'Svetlograd', 'Svetly', 'Svetogorsk', 'Svirsk', 'Svobodny', 'Syasstroy', 'Sychyovka', 'Syktyvkar', 'Sysert', 'Syzran', 'Taganrog', 'Taldom', 'Talitsa', 'Tambov', 'Tara', 'Tarko-Sale', 'Tarusa', 'Tashtagol', 'Tatarsk', 'Tavda', 'Tayga', 'Tayshet', 'Teberda', 'Temnikov', 'Temryuk', 'Terek', 'Tetyushi', 'Teykovo', 'Tikhoretsk', 'Tikhvin', 'Timashyovsk', 'Tobolsk', 'Toguchin', 'Tolyatti', 'Tomari', 'Tommot', 'Tomsk', 'Topki', 'Toropets', 'Torzhok', 'Tosno', 'Totma', 'Troitsk', 'Trubchevsk', 'Tryokhgorny', 'Tsimlyansk', 'Tsivilsk', 'Tuapse', 'Tula', 'Tulun', 'Turan', 'Turinsk', 'Tutayev', 'Tuymazy', 'Tver', 'Tynda', 'Tyrnyauz', 'Tyukalinsk', 'Tyumen', 'Uchaly', 'Udachny', 'Udomlya', 'Ufa', 'Uglegorsk', 'Uglich', 'Ukhta', 'Ulan-Ude', 'Ulyanovsk', 'Unecha', 'Uray', 'Uren', 'Urus-Martan', 'Uryupinsk', 'Urzhum', 'Usinsk', 'Usman', 'Usolye', 'Usolye-Sibirskoye', 'Ussuriysk', 'Ust-Dzheguta', 'Ust-Ilimsk', 'Ust-Katav', 'Ust-Kut', 'Ust-Labinsk', 'Ustyuzhna', 'Uvarovo', 'Uyar', 'Uzhur', 'Uzlovaya', 'Valday', 'Valuyki', 'Velikiye Luki', 'Veliky Novgorod', 'Veliky Ustyug', 'Velizh', 'Velsk', 'Venyov', 'Vereshchagino', 'Vereya', 'Verkhneuralsk', 'Verkhny Tagil', 'Verkhny Ufaley', 'Verkhnyaya Pyshma', 'Verkhnyaya Salda', 'Verkhnyaya Tura', 'Verkhoturye', 'Verkhoyansk', 'Vesyegonsk', 'Vetluga', 'Vichuga', 'Vidnoye', 'Vikhorevka', 'Vilyuchinsk', 'Vilyuysk', 'Vladikavkaz', 'Vladimir', 'Vladivostok', 'Volchansk', 'Volgodonsk', 'Volgograd', 'Volgorechensk', 'Volkhov', 'Volodarsk', 'Vologda', 'Volokolamsk', 'Volosovo', 'Volsk', 'Volzhsk', 'Volzhsky', 'Vorkuta', 'Voronezh', 'Vorsma', 'Voskresensk', 'Votkinsk', 'Vsevolozhsk', 'Vuktyl', 'Vyatskiye Polyany', 'Vyazemsky', 'Vyazma', 'Vyazniki', 'Vyborg', 'Vyksa', 'Vyshny Volochyok', 'Vysokovsk', 'Vysotsk', 'Vytegra', 'Yadrin', 'Yakhroma', 'Yakutsk', 'Yalutorovsk', 'Yanaul', 'Yaransk', 'Yaroslavl', 'Yarovoye', 'Yartsevo', 'Yasnogorsk', 'Yasny', 'Yefremov', 'Yegoryevsk', 'Yekaterinburg', 'Yelabuga', 'Yelets', 'Yelizovo', 'Yelnya', 'Yemanzhelinsk', 'Yemva', 'Yeniseysk', 'Yermolino', 'Yershov', 'Yessentuki', 'Yeysk', 'Yoshkar-Ola', 'Yubileyny', 'Yugorsk', 'Yukhnov', 'Yurga', 'Yuryev-Polsky', 'Yuryevets', 'Yuryuzan', 'Yuzha', 'Yuzhno-Sakhalinsk', 'Yuzhno-Sukhokumsk', 'Yuzhnouralsk', 'Zadonsk', 'Zainsk', 'Zakamensk', 'Zaozyorny', 'Zaozyorsk', 'Zapadnaya Dvina', 'Zapolyarny', 'Zaraysk', 'Zarechny', 'Zarinsk', 'Zavitinsk', 'Zavodoukovsk', 'Zavolzhsk', 'Zavolzhye', 'Zelenodolsk', 'Zelenogorsk', 'Zelenograd', 'Zelenogradsk', 'Zelenokumsk', 'Zernograd', 'Zeya', 'Zheleznodorozhny', 'Zheleznogorsk', 'Zheleznogorsk-Ilimsky', 'Zheleznovodsk', 'Zherdevka', 'Zhigulyovsk', 'Zhirnovsk', 'Zhizdra', 'Zhukov', 'Zhukovka', 'Zhukovsky', 'Zima', 'Zlatoust', 'Zlynka', 'Zmeinogorsk', 'Znamensk', 'Zubtsov', 'Zuyevka', 'Zvenigorod', 'Zvenigovo', 'Zverevo']

        # if total_ids_used >= 300:
        #     print ("If condition Galaxy total ids are", total_ids_used)
        #     # exclude_dict['city__in'] = russian_cities
        #     query_list = GalaxyChat.objects.filter(used_at=None).exclude(**exclude_dict).order_by('-created_at')[0:25].all()
        # else:
        #     print ("Else condition Galaxy total ids are", total_ids_used)
        #     query_list = GalaxyChat.objects.filter(used_at=None, city__in=russian_cities).exclude(**exclude_dict).order_by('-created_at')[0:25].all()

                
        # if not query_list:
        #     print ("Galaxy no query found")
        #     query_list = GalaxyChat.objects.exclude(**exclude_dict).order_by('-created_at')[0:25].all()


        exclude_dict = {}
        exclude_dict['channel_list__contains'] = channel
        # exclude_dict['network_list__contains'] = network
        # exclude_dict['offer_id_list__contains'] = offer_id

        exclude_dict_1 = {}

        query_list = GalaxyChat.objects.filter(used_at=None).exclude(**exclude_dict_1).order_by('-created_at')[0:25].all()        
        if not query_list:
            print ("Galaxy in not function")
            query_list = GalaxyChat.objects.exclude(**exclude_dict).order_by('-created_at')[0:25].all()

        if query_list:
            print ("Galzxy found query")
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

                if not query.bt_list:
                    new_bt_list = [BT]
                else:
                    if offer_id in query.bt_list:
                        continue
                    new_bt_list = query.bt_list
                    new_bt_list.append(BT)

                data = {
                        'user_id':query.id,
                        'username': query.username,
                        'city': query.city
                }
                if setUsed:
                    print ("galaxy success")
                    query = GalaxyChat.objects.filter(id=data.get('user_id')).update(
                        used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        channel_list=new_channel_list,
                        network_list=new_network_list,
                        offer_id_list=new_offer_id_list,
                        bt_list =  new_bt_list
                        )
                return Response({
                    'body':data,
                })

        return Response({
            'body':'error',
            'message':'no id found'
        })


class GalaxyChatCountryAPI(APIView):

    def put(self, request):
        query = GalaxyChatCountry()
        query.campaign_name = request.data.get('camp_name','galaxychatappmetrica')
        query.id = request.data.get('user_id')
        query.username = request.data.get('user_name')
        query.city =  request.data.get('city')
        query.from_selfcall =  request.data.get('from_selfcall','false')
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
        channel = request.GET.get('channel',True)
        network = request.GET.get('network',True)
        offer_id = request.GET.get('offer_id',True)
        if offer_id.isdecimal():
            return Response({'body':'error','message':'panel offer not allowed'})
        

        if channel in ['adshustle', 'appsfollowing', 'vestaapps', "appsatiate"]:
            BT = "BT2"
            other_BT = "BT3"
        elif channel in ['mobpine', '77ads', 'appamplify']:
            BT = "BT3"
            other_BT = "BT2"
        
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        
        exclude_dict = {}
        exclude_dict['channel_list__contains'] = channel
        # exclude_dict['network_list__contains'] = network
        # exclude_dict['offer_id_list__contains'] = offer_id

        exclude_dict_1 = {}

        query_list = GalaxyChatCountry.objects.filter(used_at=None,from_selfcall = 'false').exclude(**exclude_dict_1).order_by('-created_at')[0:25].all()        
        if not query_list:
            print ("Galaxy in not function")
            query_list = GalaxyChatCountry.objects.exclude(**exclude_dict).order_by('-created_at')[0:25].all()

        if query_list:
            print ("Galzxy found query")
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

                if not query.bt_list:
                    new_bt_list = [BT]
                else:
                    if offer_id in query.bt_list:
                        continue
                    new_bt_list = query.bt_list
                    new_bt_list.append(BT)

                data = {
                        'user_id':query.id,
                        'username': query.username,
                        'city': query.city
                }
                if setUsed:
                    print ("galaxy success")
                    query = GalaxyChatCountry.objects.filter(id=data.get('user_id')).update(
                        used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        channel_list=new_channel_list,
                        network_list=new_network_list,
                        offer_id_list=new_offer_id_list,
                        bt_list =  new_bt_list
                        )
                return Response({
                    'body':data,
                })

        return Response({
            'body':'error',
            'message':'no id found'
        })


class GalaxyChatRUAPI(APIView):

    def put(self, request):
        query = GalaxyChatRU()
        query.campaign_name = request.data.get('camp_name','galaxychatappmetrica')
        query.id = request.data.get('user_id')
        query.username = request.data.get('user_name')
        query.city =  request.data.get('city')
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
        channel = request.GET.get('channel',True)
        network = request.GET.get('network',True)
        offer_id = request.GET.get('offer_id',True)
        if offer_id.isdecimal():
            return Response({'body':'error','message':'panel offer not allowed'})
        

        if channel in ['adshustle', 'appsfollowing', 'vestaapps', "appsatiate"]:
            BT = "BT2"
            other_BT = "BT3"
        elif channel in ['mobpine', '77ads', 'appamplify']:
            BT = "BT3"
            other_BT = "BT2"
        
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        
        exclude_dict = {}
        exclude_dict['channel_list__contains'] = channel
        # exclude_dict['network_list__contains'] = network
        # exclude_dict['offer_id_list__contains'] = offer_id

        exclude_dict_1 = {}

        query_list = GalaxyChatRU.objects.filter(used_at=None).exclude(**exclude_dict_1).order_by('-created_at')[0:25].all()        
        if not query_list:
            print ("Galaxy in not function")
            query_list = GalaxyChatRU.objects.exclude(**exclude_dict).order_by('-created_at')[0:25].all()

        if query_list:
            print ("Galzxy found query")
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

                if not query.bt_list:
                    new_bt_list = [BT]
                else:
                    if offer_id in query.bt_list:
                        continue
                    new_bt_list = query.bt_list
                    new_bt_list.append(BT)

                data = {
                        'user_id':query.id,
                        'username': query.username,
                        'city': query.city
                }
                if setUsed:
                    print ("galaxy success")
                    query = GalaxyChatRU.objects.filter(id=data.get('user_id')).update(
                        used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        channel_list=new_channel_list,
                        network_list=new_network_list,
                        offer_id_list=new_offer_id_list,
                        bt_list =  new_bt_list
                        )
                return Response({
                    'body':data,
                })

        return Response({
            'body':'error',
            'message':'no id found'
        })
        
class AlphacapitalAPI(APIView):

    def put(self, request):
        query = Alphacapital()
        query.campaign_name = request.data.get('camp_name','alphacapitalmodd')
        query.id = request.data.get('user_id')
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
        channel = request.GET.get('channel',True)
        network = request.GET.get('network',True)
        offer_id = request.GET.get('offer_id',True)
        if offer_id.isdecimal():
            return Response({'body':'error','message':'panel offer not allowed'})

        
        # if not channel or not network or not offer_id:
        #     return Response({
        #                 'body':'error',
        #                 'message':'channel,offer_id,network id missing.'
        #             })
        
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        exclude_dict = {}
        exclude_dict['channel_list__contains'] = channel
        # exclude_dict['network_list__contains'] = network
        # exclude_dict['offer_id_list__contains'] = offer_id

        exclude_dict_1 = {}

        query_list = Alphacapital.objects.filter(used_at=None).exclude(**exclude_dict_1).order_by('-created_at')[0:25].all()        
        if not query_list:
            query_list = Alphacapital.objects.exclude(**exclude_dict).order_by('-created_at')[0:25].all()
        
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
                        'user_id':query.id,
                }
                if setUsed:
                    query = Alphacapital.objects.filter(id=data.get('user_id')).update(
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
    

class ReminderAPI(APIView):
    def get(self, request):

        message = {
        "text": "<users/all> Pls check if there is any cust pending",
        "annotations": [
            {
            "type": "USER_MENTION",
            "startIndex": 0,
            "length": 11,
            "userMention": {
                "user": {
                "name": "users/all"
                }
            }
            }
        ]
        }

        from data_tracking.util import googleChatBot_send_message

        googleChatBot_send_message(space_name="AAQAVUzsCsk",message=message)

        return Response({"status": "success"})

class bigloanAPI(APIView):
    def put(self, request):
        query = Bigloan()
        query.campaign_name = request.data.get('camp_name','bigloanmodd')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Bigloan.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = Bigloan.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })

class CoinmenaAPI(APIView):
    def put(self, request):
        query = Coinmena()
        query.campaign_name = request.data.get('camp_name','coinmenaauto')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Coinmena.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = Coinmena.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })
    
class TikettUIDAPI(APIView):
    def put(self, request):
        query = TikettUID()
        query.campaign_name = request.data.get('camp_name','tikettmodd')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = TikettUID.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = TikettUID.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })


class Cabst13API(APIView):
    def put(self, request):
        query = Cabst13()
        query.campaign_name = request.data.get('camp_name','13cabstauto')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Cabst13.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = Cabst13.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })

class R888casinoAPI(APIView):
    def put(self, request):
        query = R888casino()
        query.campaign_name = request.data.get('camp_name','r888casinomodd')
        query.id = request.data.get('user_id')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = R888casino.objects.filter(used_at=None).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                # 'extra_details':query.extra_details,
        }
        if setUsed:
            query = R888casino.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
    def post(self, request):
        query = R888casino.objects.order_by('-id').first()

        return Response({
            'id':query.id,
        })


class JoybuyAPI(APIView):
    def put(self, request):
        query = Joybuy()
        query.campaign_name = request.data.get('camp_name','joybuymodd')
        query.id = request.data.get('order_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Joybuy.objects.latest('created_at')
        
        data = {
                'order_id':query.id,
        }
        if setUsed:
            query = Joybuy.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })

class Atomepht2uidAPI(APIView):
    def put(self, request):
        query = Atomepht2uid()
        query.campaign_name = request.data.get('camp_name','atomepht2modd')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Atomepht2uid.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = Atomepht2uid.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })

class Atomepht2aidAPI(APIView):
    def put(self, request):
        query = Atomepht2aid()
        query.campaign_name = request.data.get('camp_name','atomepht2modd')
        query.id = request.data.get('agent_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Atomepht2aid.objects.latest('created_at')
        
        data = {
                'agent_id':query.id,
        }
        if setUsed:
            query = Atomepht2aid.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })

class ClubeextraAPI(APIView):
    def put(self, request):
        query = Clubeextra()
        query.campaign_name = request.data.get('camp_name','clubeextraamodd')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Clubeextra.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = Clubeextra.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })

class ClubeextracidAPI(APIView):
    def put(self, request):
        query = Clubeextracid()
        query.campaign_name = request.data.get('camp_name','clubeextraamodd')
        query.id = request.data.get('user_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Clubeextracid.objects.latest('created_at')
        
        data = {
                'user_id':query.id,
        }
        if setUsed:
            query = Clubeextracid.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })
        
class MyshiftAPI(APIView):

    def put(self, request):
        query = Myshift()
        query.campaign_name = request.data.get('camp_name','myshiftappmetricat')
        query.id = request.data.get('user_id')
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
        channel = request.GET.get('channel',True)
        network = request.GET.get('network',True)
        offer_id = request.GET.get('offer_id',True)
        if offer_id.isdecimal():
            return Response({'body':'error','message':'panel offer not allowed'})

        
        # if not channel or not network or not offer_id:
        #     return Response({
        #                 'body':'error',
        #                 'message':'channel,offer_id,network id missing.'
        #             })
        
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        exclude_dict = {}
        exclude_dict['channel_list__contains'] = channel
        # exclude_dict['network_list__contains'] = network
        # exclude_dict['offer_id_list__contains'] = offer_id

        exclude_dict_1 = {}

        query_list = Myshift.objects.filter(used_at=None).exclude(**exclude_dict_1).order_by('-created_at')[0:25].all()        
        if not query_list:
            query_list = Myshift.objects.exclude(**exclude_dict).order_by('-created_at')[0:25].all()
        
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
                        'user_id':query.id,
                }
                if setUsed:
                    query = Myshift.objects.filter(id=data.get('user_id')).update(
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


class RevenueHelperBackupView(APIView):
    def post(self, request):
        now = timezone.now()
        first_day_this_month = now.replace(day=1)
        last_month_end = first_day_this_month - timedelta(days=1)
        last_month_start = last_month_end.replace(day=1)

        queryset = RevenueHelper.objects.filter(
            created_at__gte=last_month_start,
            created_at__lte=last_month_end,
        )

        # objs = []
        # for obj in queryset:
        #     objs.append(
        #         RevenueHelperBackup(
        #             campaign_name=obj.campaign_name,
        #             created_at=obj.created_at,
        #             c_day=obj.c_day,
        #             updated_at=obj.updated_at,
        #             channel=obj.channel,
        #             network=obj.network,
        #             offer_id=obj.offer_id,
        #             id=obj.id,
        #             revenue=obj.revenue,
        #             currency=obj.currency,
        #             adid=obj.adid,
        #             event_name=obj.event_name,
        #             event_value=obj.event_value,
        #             app_version=obj.app_version,
        #             script_version=obj.script_version,
        #         )
        #     )

        # RevenueHelperBackup.objects.bulk_create(objs)

        # serializer = RevenueHelperBackupSerializer(objs, many=True)
        # return Response(
        #     {
        #         "message": f"Backed up {len(objs)} rows from {last_month_start.date()} to {last_month_end.date()}",
        #         "data": serializer.data,
        #     },
        #     status=status.HTTP_201_CREATED,
        # )

        return Response(
            {
                "message": f"rows from {last_month_start.date()} to {last_month_end.date()}",
                "data": {},
            },
        )

class HeringAPI(APIView):
    def put(self, request):
        query = Hering()
        query.campaign_name = request.data.get('camp_name','heringmodd')
        query.id = request.data.get('order_id')
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = Hering.objects.latest('created_at')
        
        data = {
                'order_id':query.id,
        }
        if setUsed:
            query = Hering.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })


class Babytrackeruid(APIView):

    def put(self, request):
        query = Babytracker()
        query.campaign_name = request.data.get('camp_name','babytrackermodd')
        query.id = request.data.get('user_id')
        query.is_premium = request.data.get('is_premium')
        query.extra_details = request.data.get('extra_details',{})
        query.used_at = None
        query.save()
        return Response({
        })

    def get(self, request):

        channel = request.GET.get('channel', '')
        network = request.GET.get('network', '')
        offer_id = request.GET.get('offer_id', '')
        setUsed = request.GET.get('set_used',True)
        is_premium = request.GET.get('is_premium', False)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False

        query = Babytracker.objects.filter(used_at=None, is_premium=is_premium).order_by('-created_at')[0:50].first()
        
        data = {
                'user_id':query.id,
                'extra_details':query.extra_details, 
        }
        if setUsed:
            query = Babytracker.objects.filter(id=data.get('user_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), channel=channel, network=network, offer_id=offer_id)
        return Response({
            'body':data,
        })
    
    def post(self, request):
        query = Babytracker.objects.order_by('-id').first()

        return Response({
            'id':query.id,
        })