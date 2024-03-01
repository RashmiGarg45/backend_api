from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

from django.db.models import Sum
from django.shortcuts import render

import json
from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
import gspread
from datetime import datetime,timedelta
from operator import itemgetter

from data_tracking.models import revenueReport,installReport
from data_tracking.serializer import revenueReportSerializer

from data_tracking.util import get_list_data_from_raw,googleChatBot_send_message

class Report6Stats(APIView):
    def get(self, request):        
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')


        filter_dict = {
            'date__gte':start_date,
            'date__lte':end_date, 
        }
        for item in ['campaign','package_name']:
            if request.GET.get(item):
                if ',' in request.GET.get(item):
                    filter_dict[item+'__in'] =  request.GET.get(item).split(',')
                else:
                    filter_dict[item] =  request.GET.get(item)

        annotation_dict = {
            'total_revenue':Sum(F'revenue'),
            'i2_count':Sum('r_install')
        }

        r6_data = {}
        for env in ['1','2','3']:
            campaign_list = []
            data = revenueReport.objects.filter(**filter_dict).values('date','channel','network','offer_id','campaign').annotate(**annotation_dict).using('cm-env{}'.format(env))
            for item in data:
                if item.get('channel').lower() not in ['vestaapps','77ads','appamplify','offersinfinite']:
                    item['total_revenue'] = item.get('total_revenue')/0.7
                
                campaign_name = item.get('campaign')
                date = str(item.get('date'))
                if not r6_data.get(campaign_name):
                    r6_data[campaign_name] = {
                        'i1_count_range':0,
                        'i2_count_range':0,
                        'total_revenue_range':0
                    }
                if not r6_data.get(campaign_name).get(date):
                    r6_data[campaign_name][date] = {
                        'i1_count':0,
                        'i2_count':0,
                        'total_revenue':0
                    }
                
                r6_data[campaign_name][date]['i2_count']+=item.get('i2_count')
                r6_data[campaign_name][date]['total_revenue']+=item.get('total_revenue')

                r6_data[campaign_name]['i2_count_range']+=item.get('i2_count')
                r6_data[campaign_name]['total_revenue_range']+=item.get('total_revenue')

                if campaign_name not in campaign_list:
                    campaign_list.append(campaign_name)

            ## CREATING I1 Data
            if filter_dict.get('package_name'):
                del filter_dict['package_name']
                if filter_dict.get('package_name__in'):
                    del filter_dict['package_name__in']

                filter_dict['campaign__in'] = campaign_list

            i1_annotation_dict = {
                'i1_count':Sum('count'),
            }
            i1_data = installReport.objects.filter(**filter_dict).values('date','campaign').annotate(**i1_annotation_dict).using('at-env{}'.format(env))
            for item in i1_data:
                campaign_name = item.get('campaign')
                date = str(item.get('date'))
                if not r6_data.get(campaign_name):
                    r6_data[campaign_name] = {
                        'i1_count_range':0,
                        'i2_count_range':0,
                        'total_revenue_range':0
                    }
                if not r6_data.get(campaign_name).get(date):
                    r6_data[campaign_name][date] = {
                        'i1_count':0,
                        'i2_count':0,
                        'total_revenue':0
                    }
                
                r6_data[campaign_name][date]['i1_count']+=item.get('i1_count')
                r6_data[campaign_name]['i1_count_range']+=item.get('i1_count')


        return HttpResponse(json.dumps({
            'data':r6_data,
        }))

class ChatBotNotRunLastTwoMonthLevel2(APIView):
    def get(self,request):
        # This Api will send a message to Chatbot where we can see which Apps have not been runned by BT.
        # data = {}
        # resp_dict = {}
        # total_row = {}
        # work_data_map = get_list_data_from_raw(data)
        # start_date = '2024-01-01'
        # end_date = '2024-02-29'
        # done_data = list(filter(lambda element: ((element.get('Work Category').replace(' ','').replace('\t','').lower()=='lvl2' or element.get('Work Category').replace(' ','').replace('\t','').lower()=='lvl1') and (element.get('Working Status').replace(' ','').replace('\t','').lower()=='done' or element.get('Working Status').replace(' ','').replace('\t','').lower()=='doneconditionaly') and element.get('Done-Date').replace(' ','').replace('\t','').lower()>=start_date and element.get('Done-Date').replace(' ','').replace('\t','').lower()<=end_date),work_data_map))
        # dict__ = {}
        # camp_data_dict = {}
        # for i in done_data:
        #     camp_name = i.get('AppName').strip()
        #     month = str(datetime.strptime(i.get('Done-Date'),'%Y-%m-%d').strftime('%Y-%m'))
        #     if not dict__.get(month):
        #         dict__[month] = []
        #     dict__[month].append(camp_name)
        #     camp_data_dict[camp_name] = i

        # for month,campaigns in dict__.items():
        #     if not resp_dict.get(month):
        #         resp_dict[month] = {}
        #     if not total_row.get(month):
        #         total_row[month] = {'scriptname':'Total','total-TR':0}
        #     for month_next in dict__.keys():
        #         if month_next>=month:

        #             import calendar
        #             strt_end = calendar.monthrange(int(month_next.split('-')[0]), int(month_next.split('-')[1]))
        #             start_date_month = '{}-{}'.format(month_next,'01')
        #             end_date_month = '{}-{}'.format(month_next,strt_end[1])
        #             request.GET = {
        #                 'start_date':start_date_month,
        #                 'end_date':end_date_month,
        #                 'campaign':",".join(campaigns)
        #             }
                    
        #             r6_obj = Report6Stats()
        #             resp_data = json.loads(r6_obj.get(request).content)
        #             raw_data = resp_data.get('data')
        #             for scriptname,scriptdata in raw_data.items():
        #                 if not resp_dict.get(month).get(scriptname):
        #                     resp_dict[month][scriptname] = {
        #                                                 'scriptname':scriptname,
        #                                                 'subteam':camp_data_dict.get(scriptname,{}).get('Dev-Team'),
        #                                                 'done_date':camp_data_dict.get(scriptname,{}).get('Done-Date'),
        #                                                 'level':camp_data_dict.get(scriptname,{}).get('Work Category'),
        #                                                 'total-TR':0,
        #                                             }
                        
                        
        #                 resp_dict[month][scriptname]['{}-TR'.format(month_next)] = scriptdata.get('total_revenue_range')
        #                 resp_dict[month][scriptname]['{}-TR'.format('total')]+=float(scriptdata.get('total_revenue_range',0))
                        
        #                 if not total_row.get(month).get('{}-TR'.format(month_next)):
        #                     total_row[month]['{}-TR'.format(month_next)] = 0
        #                 total_row[month]['{}-TR'.format(month_next)] += float(scriptdata.get('total_revenue_range',0))
        #                 total_row[month]['{}-TR'.format('total')] += float(scriptdata.get('total_revenue_range',0))

        xx = {
                "data": {
                    "2024-01": {
                        "mimilivemodd": {
                            "scriptname": "mimilivemodd",
                            "subteam": "Udit",
                            "done_date": "2024-01-29",
                            "level": "LVL2",
                            "total-TR": 2326.6153029948473,
                            "2024-01-TR": 1241.4900012697492,
                            "2024-02-TR": 1085.1253017250983
                        },
                        "flexsalaryauto": {
                            "scriptname": "flexsalaryauto",
                            "subteam": "Umair",
                            "done_date": "2024-01-17",
                            "level": "LVL2",
                            "total-TR": 2735.799983637674,
                            "2024-01-TR": 2714.799983637674,
                            "2024-02-TR": 21.0
                        },
                        "zigbangmodd": {
                            "scriptname": "zigbangmodd",
                            "subteam": "Umair",
                            "done_date": "2024-01-04",
                            "level": "LVL1",
                            "total-TR": 183.3006283534425,
                            "2024-01-TR": 124.22920012686934,
                            "2024-02-TR": 59.07142822657315
                        },
                        "euninemodd": {
                            "scriptname": "euninemodd",
                            "subteam": "Umair",
                            "done_date": "2024-01-04",
                            "level": "LVL1",
                            "total-TR": 2026.9130730341599,
                            "2024-01-TR": 116.27800325091398,
                            "2024-02-TR": 1910.6350697832459
                        },
                        "surfsharkmodd": {
                            "scriptname": "surfsharkmodd",
                            "subteam": "Umair",
                            "done_date": "2024-01-06",
                            "level": "LVL2",
                            "total-TR": 1683.000035967146,
                            "2024-01-TR": 1683.000035967146
                        },
                        "macplusmodd": {
                            "scriptname": "macplusmodd",
                            "subteam": "Umair",
                            "done_date": "2024-01-02",
                            "level": "LVL1",
                            "total-TR": 213.9957135255847,
                            "2024-01-TR": 213.9957135255847
                        },
                        "dicedreamsmodd": {
                            "scriptname": "dicedreamsmodd",
                            "subteam": "Udit",
                            "done_date": "2024-01-15",
                            "level": "LVL1",
                            "total-TR": 711.4380245059729,
                            "2024-01-TR": 585.9900215012686,
                            "2024-02-TR": 125.44800300470422
                        },
                        "zeeplivemodd": {
                            "scriptname": "zeeplivemodd",
                            "subteam": "Udit",
                            "done_date": "2024-01-19",
                            "level": "LVL1",
                            "total-TR": 1031.926081486046,
                            "2024-01-TR": 551.4519922956822,
                            "2024-02-TR": 480.47408919036394
                        },
                        "unicardsauto": {
                            "scriptname": "unicardsauto",
                            "subteam": "Udit",
                            "done_date": "2024-01-20",
                            "level": "LVL2",
                            "total-TR": 105.11200132753167,
                            "2024-01-TR": 105.11200132753167
                        },
                        "myown3kingdomauto": {
                            "scriptname": "myown3kingdomauto",
                            "subteam": "Udit",
                            "done_date": "2024-01-17",
                            "level": "LVL2",
                            "total-TR": 673.8409923613073,
                            "2024-01-TR": 641.6449915468694,
                            "2024-02-TR": 32.196000814437866
                        },
                        "traininpinkauto": {
                            "scriptname": "traininpinkauto",
                            "subteam": "Udit",
                            "done_date": "2024-01-18",
                            "level": "LVL1",
                            "total-TR": 141.00957166084223,
                            "2024-01-TR": 133.40957168809007,
                            "2024-02-TR": 7.599999972752163
                        },
                        "puzzlesandchaosmodd": {
                            "scriptname": "puzzlesandchaosmodd",
                            "subteam": "Udit",
                            "done_date": "2024-01-19",
                            "level": "LVL2",
                            "total-TR": 1640.7599793161664,
                            "2024-01-TR": 1316.9999858311244,
                            "2024-02-TR": 323.759993485042
                        },
                        "viocommodd": {
                            "scriptname": "viocommodd",
                            "subteam": "Udit",
                            "done_date": "2024-01-17",
                            "level": "LVL2",
                            "total-TR": 537.822009078094,
                            "2024-01-TR": 537.822009078094
                        },
                        "samcostockmarkettradingmodd": {
                            "scriptname": "samcostockmarkettradingmodd",
                            "subteam": "Udit",
                            "done_date": "2024-01-23",
                            "level": "LVL2",
                            "total-TR": 86.90320027726038,
                            "2024-01-TR": 86.90320027726038,
                            "2024-02-TR": 0
                        },
                        "cbdauto": {
                            "scriptname": "cbdauto",
                            "subteam": "Umair",
                            "done_date": "2024-01-23",
                            "level": "LVL2",
                            "total-TR": 1402.9999997956413,
                            "2024-01-TR": 817.999993801117,
                            "2024-02-TR": 585.0000059945244
                        },
                        "rabbitmodd": {
                            "scriptname": "rabbitmodd",
                            "subteam": "Umair",
                            "done_date": "2024-01-29",
                            "level": "LVL2",
                            "total-TR": 757.5341970920564,
                            "2024-01-TR": 149.299998155662,
                            "2024-02-TR": 608.2341989363944
                        },
                        "solitaireclassicauto": {
                            "scriptname": "solitaireclassicauto",
                            "subteam": "Udit",
                            "done_date": "2024-01-16",
                            "level": "LVL1",
                            "total-TR": 458.53399854259834,
                            "2024-01-TR": 10.03399997310979,
                            "2024-02-TR": 448.4999985694885
                        },
                        "petbookappmetrica": {
                            "scriptname": "petbookappmetrica",
                            "subteam": "Udit",
                            "done_date": "2024-01-02",
                            "level": "LVL1",
                            "total-TR": 0.20000000298023224,
                            "2024-01-TR": 0.20000000298023224,
                            "2024-02-TR": 0
                        },
                        "bluerewardsauto": {
                            "scriptname": "bluerewardsauto",
                            "subteam": "Umair",
                            "done_date": "2024-01-03",
                            "level": "LVL2",
                            "total-TR": 0.0,
                            "2024-01-TR": 0,
                            "2024-02-TR": 0
                        },
                        "edamamaautoios": {
                            "scriptname": "edamamaautoios",
                            "subteam": "Udit",
                            "done_date": "2024-01-22",
                            "level": "LVL2",
                            "total-TR": 44.99999795641218,
                            "2024-01-TR": 44.99999795641218,
                            "2024-02-TR": 0
                        },
                        "sologameauto": {
                            "scriptname": "sologameauto",
                            "subteam": "Umair",
                            "done_date": "2024-01-13",
                            "level": "LVL2",
                            "total-TR": 3373.6000698634557,
                            "2024-01-TR": 1463.200014931815,
                            "2024-02-TR": 1910.4000549316406
                        },
                        "gentlerstreakios": {
                            "scriptname": "gentlerstreakios",
                            "subteam": "Umair",
                            "done_date": "2024-01-19",
                            "level": "LVL1",
                            "total-TR": 191.9999987738473,
                            "2024-01-TR": 191.9999987738473,
                            "2024-02-TR": 0
                        },
                        "spinjoymodd": {
                            "scriptname": "spinjoymodd",
                            "subteam": "Udit",
                            "done_date": "2024-01-24",
                            "level": "LVL2",
                            "total-TR": 1604.8167260853309,
                            "2024-01-TR": 373.0571363653455,
                            "2024-02-TR": 1231.7595897199853
                        },
                        "weightsmodd": {
                            "scriptname": "weightsmodd",
                            "subteam": "Udit",
                            "done_date": "2024-01-24",
                            "level": "LVL2",
                            "total-TR": 2082.49101132048,
                            "2024-01-TR": 625.521001781736,
                            "2024-02-TR": 1456.970009538744
                        },
                        "gujaratimatrimonymodd": {
                            "scriptname": "gujaratimatrimonymodd",
                            "subteam": "Umair",
                            "done_date": "2024-01-25",
                            "level": "LVL2",
                            "total-TR": 1669.4999149867467,
                            "2024-01-TR": 1669.4999149867467
                        },
                        "tamilmatrimonybysangammodd": {
                            "scriptname": "tamilmatrimonybysangammodd",
                            "subteam": "Udit",
                            "done_date": "2024-01-26",
                            "level": "LVL2",
                            "total-TR": 1338.3999520710538,
                            "2024-01-TR": 1338.3999520710538
                        },
                        "betfrombrmodd": {
                            "scriptname": "betfrombrmodd",
                            "subteam": "Udit",
                            "done_date": "2024-01-29",
                            "level": "LVL2",
                            "total-TR": 99.7085690498352,
                            "2024-01-TR": 70.12285607201713,
                            "2024-02-TR": 29.585712977818083
                        },
                        "foreverindiamodd": {
                            "scriptname": "foreverindiamodd",
                            "subteam": "Umair",
                            "done_date": "2024-01-30",
                            "level": "LVL2",
                            "total-TR": 177.35500051081178,
                            "2024-01-TR": 18.999999985098842,
                            "2024-02-TR": 158.35500052571294
                        },
                        "moregoldmodd": {
                            "scriptname": "moregoldmodd",
                            "subteam": "Umair",
                            "done_date": "2024-01-30",
                            "level": "LVL2",
                            "total-TR": 335.5460001996585,
                            "2024-01-TR": 45.0,
                            "2024-02-TR": 290.5460001996585
                        },
                        "theimpmodd": {
                            "scriptname": "theimpmodd",
                            "subteam": "Umair",
                            "done_date": "2024-01-29",
                            "level": "LVL2",
                            "total-TR": 219.6999969482422,
                            "2024-01-TR": 148.1999969482422,
                            "2024-02-TR": 71.5
                        },
                        "chispadatingmodd": {
                            "scriptname": "chispadatingmodd",
                            "subteam": "Udit",
                            "done_date": "2024-01-12",
                            "level": "LVL1",
                            "total-TR": 86.56400123664312,
                            "2024-02-TR": 86.56400123664312
                        },
                        "tripsygamesmodd": {
                            "scriptname": "tripsygamesmodd",
                            "subteam": "Umair",
                            "done_date": "2024-01-31",
                            "level": "LVL2",
                            "total-TR": 2195.275957541806,
                            "2024-02-TR": 2195.275957541806
                        },
                        "uiuxmobileauto": {
                            "scriptname": "uiuxmobileauto",
                            "subteam": "Udit",
                            "done_date": "2024-01-23",
                            "level": "LVL1",
                            "total-TR": 464.344007917813,
                            "2024-02-TR": 464.344007917813
                        },
                        "turofindyourdrivemodd": {
                            "scriptname": "turofindyourdrivemodd",
                            "subteam": "Udit",
                            "done_date": "2024-02-06",
                            "level": "LVL2",
                            "total-TR": 719.1771289280483,
                            "2024-02-TR": 719.1771289280483
                        }
                    },
                    "2024-02": {
                        "adikuauto": {
                            "scriptname": "adikuauto",
                            "subteam": "Udit",
                            "done_date": "2024-02-01",
                            "level": "LVL1",
                            "total-TR": 358.56269812903236,
                            "2024-02-TR": 358.56269812903236
                        },
                        "mysfmodd": {
                            "scriptname": "mysfmodd",
                            "subteam": "Umair",
                            "done_date": "2024-02-03",
                            "level": "LVL2",
                            "total-TR": 2.1700000699077338,
                            "2024-02-TR": 2.1700000699077338
                        },
                        "tiktokmusicmodd": {
                            "scriptname": "tiktokmusicmodd",
                            "subteam": "Umair",
                            "done_date": "2024-02-01",
                            "level": "LVL1",
                            "total-TR": 127.29599707680089,
                            "2024-02-TR": 127.29599707680089
                        },
                        "chargeupappmetrica": {
                            "scriptname": "chargeupappmetrica",
                            "subteam": "Umair",
                            "done_date": "2024-02-07",
                            "level": "LVL2",
                            "total-TR": 836.4835626408454,
                            "2024-02-TR": 836.4835626408454
                        },
                        "destinymmodd": {
                            "scriptname": "destinymmodd",
                            "subteam": "Umair",
                            "done_date": "2024-02-06",
                            "level": "LVL2",
                            "total-TR": 2155.9612072663645,
                            "2024-02-TR": 2155.9612072663645
                        },
                        "physicswallahmodd": {
                            "scriptname": "physicswallahmodd",
                            "subteam": "Umair",
                            "done_date": "2024-02-07",
                            "level": "LVL2",
                            "total-TR": 1122.425598380821,
                            "2024-02-TR": 1122.425598380821
                        },
                        "nobodysadventurmodd": {
                            "scriptname": "nobodysadventurmodd",
                            "subteam": "Udit",
                            "done_date": "2024-02-08",
                            "level": "LVL1",
                            "total-TR": 66.8664997981063,
                            "2024-02-TR": 66.8664997981063
                        },
                        "stablemoney": {
                            "scriptname": "stablemoney",
                            "subteam": "Udit",
                            "done_date": "2024-02-14",
                            "level": "LVL2",
                            "total-TR": 870.6474839443609,
                            "2024-02-TR": 870.6474839443609
                        },
                        "senhengmodd": {
                            "scriptname": "senhengmodd",
                            "subteam": "Udit",
                            "done_date": "2024-02-20",
                            "level": "LVL2",
                            "total-TR": 388.0229977230941,
                            "2024-02-TR": 388.0229977230941
                        },
                        "gcskinsmodd": {
                            "scriptname": "gcskinsmodd",
                            "subteam": "Umair",
                            "done_date": "2024-02-12",
                            "level": "LVL1",
                            "total-TR": 462.69976609785647,
                            "2024-02-TR": 462.69976609785647
                        },
                        "garantiauto": {
                            "scriptname": "garantiauto",
                            "subteam": "Udit",
                            "done_date": "2024-02-05",
                            "level": "LVL2",
                            "total-TR": 972.9498290621806,
                            "2024-02-TR": 972.9498290621806
                        },
                        "eroskimodd": {
                            "scriptname": "eroskimodd",
                            "subteam": "Udit",
                            "done_date": "2024-02-09",
                            "level": "LVL2",
                            "total-TR": 1647.0800224734212,
                            "2024-02-TR": 1647.0800224734212
                        },
                        "quickcashonlinemodd": {
                            "scriptname": "quickcashonlinemodd",
                            "subteam": "Udit",
                            "done_date": "2024-02-20",
                            "level": "LVL2",
                            "total-TR": 1049.5699210975854,
                            "2024-02-TR": 1049.5699210975854
                        },
                        "uobtmrwmodd": {
                            "scriptname": "uobtmrwmodd",
                            "subteam": "Udit",
                            "done_date": "2024-02-20",
                            "level": "LVL2",
                            "total-TR": 4314.099999746042,
                            "2024-02-TR": 4314.099999746042
                        },
                        "sololearnmodd": {
                            "scriptname": "sololearnmodd",
                            "subteam": "Udit",
                            "done_date": "2024-02-19",
                            "level": "LVL1",
                            "total-TR": 155.34100180438588,
                            "2024-02-TR": 155.34100180438588
                        },
                        "express24auto": {
                            "scriptname": "express24auto",
                            "subteam": "Udit",
                            "done_date": "2024-02-21",
                            "level": "LVL2",
                            "total-TR": 969.9999652590072,
                            "2024-02-TR": 969.9999652590072
                        },
                        "eternaleramodd": {
                            "scriptname": "eternaleramodd",
                            "subteam": "Umair",
                            "done_date": "2024-02-22",
                            "level": "LVL1",
                            "total-TR": 21.5,
                            "2024-02-TR": 21.5
                        },
                        "allofreshmodd": {
                            "scriptname": "allofreshmodd",
                            "subteam": "Udit",
                            "done_date": "2024-02-23",
                            "level": "LVL2",
                            "total-TR": 566.9080014335258,
                            "2024-02-TR": 566.9080014335258
                        },
                        "slayingdemonsmodd": {
                            "scriptname": "slayingdemonsmodd",
                            "subteam": "Udit",
                            "done_date": "2024-02-23",
                            "level": "LVL2",
                            "total-TR": 517.2449922923532,
                            "2024-02-TR": 517.2449922923532
                        },
                        "toonsutramodd": {
                            "scriptname": "toonsutramodd",
                            "subteam": "Udit",
                            "done_date": "2024-02-22",
                            "level": "LVL2",
                            "total-TR": 235.7006095541375,
                            "2024-02-TR": 235.7006095541375
                        },
                        "puzzlechaosmodd": {
                            "scriptname": "puzzlechaosmodd",
                            "subteam": "Udit",
                            "done_date": "2024-02-27",
                            "level": "LVL2",
                            "total-TR": 159.19289938254016,
                            "2024-02-TR": 159.19289938254016
                        },
                        "guessmonstervoicemodd": {
                            "scriptname": "guessmonstervoicemodd",
                            "subteam": "Udit",
                            "done_date": "2024-02-27",
                            "level": "LVL2",
                            "total-TR": 13.500000187328883,
                            "2024-02-TR": 13.500000187328883
                        },
                        "pocketbrokermodd": {
                            "scriptname": "pocketbrokermodd",
                            "subteam": "Udit",
                            "done_date": "2024-02-23",
                            "level": "LVL2",
                            "total-TR": 410.55999994277954,
                            "2024-02-TR": 410.55999994277954
                        },
                        "nobitreasuryauto": {
                            "scriptname": "nobitreasuryauto",
                            "subteam": "Udit",
                            "done_date": "2024-02-27",
                            "level": "LVL2",
                            "total-TR": 38.819999422345845,
                            "2024-02-TR": 38.819999422345845
                        },
                        "fancodemodd": {
                            "scriptname": "fancodemodd",
                            "subteam": "Umair",
                            "done_date": "2024-02-27",
                            "level": "LVL2",
                            "total-TR": 165.99999803304672,
                            "2024-02-TR": 165.99999803304672
                        },
                        "trubitbitcoinmodd": {
                            "scriptname": "trubitbitcoinmodd",
                            "subteam": "Udit",
                            "done_date": "2024-02-07",
                            "level": "LVL2",
                            "total-TR": 1711.9999817439489,
                            "2024-02-TR": 1711.9999817439489
                        },
                        "ozeesalonauto": {
                            "scriptname": "ozeesalonauto",
                            "subteam": "Udit",
                            "done_date": "2024-02-07",
                            "level": "LVL2",
                            "total-TR": 2078.7999984366556,
                            "2024-02-TR": 2078.7999984366556
                        },
                        "flipmodd": {
                            "scriptname": "flipmodd",
                            "subteam": "Udit",
                            "done_date": "2024-02-12",
                            "level": "LVL2",
                            "total-TR": 3.827999968613897,
                            "2024-02-TR": 3.827999968613897
                        },
                        "tamashamodd": {
                            "scriptname": "tamashamodd",
                            "subteam": "Udit",
                            "done_date": "2024-02-14",
                            "level": "LVL2",
                            "total-TR": 0.0,
                            "2024-02-TR": 0
                        },
                        "easypesomodd": {
                            "scriptname": "easypesomodd",
                            "subteam": "Umair",
                            "done_date": "2024-02-02",
                            "level": "LVL2",
                            "total-TR": 1485.0,
                            "2024-02-TR": 1485.0
                        },
                        "turofindyourdrivemodd": {
                            "scriptname": "turofindyourdrivemodd",
                            "subteam": "Udit",
                            "done_date": "2024-02-06",
                            "level": "LVL2",
                            "total-TR": 719.1771289280483,
                            "2024-02-TR": 719.1771289280483
                        },
                        "miufmpartymodd": {
                            "scriptname": "miufmpartymodd",
                            "subteam": "Udit",
                            "done_date": "2024-02-08",
                            "level": "LVL2",
                            "total-TR": 154.4029207719224,
                            "2024-02-TR": 154.4029207719224
                        },
                        "dragonpowmodd": {
                            "scriptname": "dragonpowmodd",
                            "subteam": "Udit",
                            "done_date": "2024-02-07",
                            "level": "LVL2",
                            "total-TR": 159.0,
                            "2024-02-TR": 159.0
                        },
                        "gpbetmodd": {
                            "scriptname": "gpbetmodd",
                            "subteam": "Umair",
                            "done_date": "2024-02-12",
                            "level": "LVL2",
                            "total-TR": 451.6700005744184,
                            "2024-02-TR": 451.6700005744184
                        },
                        "treebot2modd": {
                            "scriptname": "treebot2modd",
                            "subteam": "Udit",
                            "done_date": "2024-02-15",
                            "level": "LVL2",
                            "total-TR": 1009.3500171388899,
                            "2024-02-TR": 1009.3500171388899
                        },
                        "spreedlmodd": {
                            "scriptname": "spreedlmodd",
                            "subteam": "Umair",
                            "done_date": "2024-02-20",
                            "level": "LVL2",
                            "total-TR": 124.86427852085659,
                            "2024-02-TR": 124.86427852085659
                        },
                        "lionsgateplayteam2modd": {
                            "scriptname": "lionsgateplayteam2modd",
                            "subteam": "Umair",
                            "done_date": "2024-02-19",
                            "level": "LVL2",
                            "total-TR": 160.49999509538924,
                            "2024-02-TR": 160.49999509538924
                        },
                        "pokachatmodd": {
                            "scriptname": "pokachatmodd",
                            "subteam": "Udit",
                            "done_date": "2024-02-24",
                            "level": "LVL2",
                            "total-TR": 406.8000136784145,
                            "2024-02-TR": 406.8000136784145
                        },
                        "visorymodd": {
                            "scriptname": "visorymodd",
                            "subteam": "Udit",
                            "done_date": "2024-02-28",
                            "level": "LVL1",
                            "total-TR": 33.99999921662467,
                            "2024-02-TR": 33.99999921662467
                        },
                        "tenbetmxauto": {
                            "scriptname": "tenbetmxauto",
                            "subteam": "Udit",
                            "done_date": "2024-02-10",
                            "level": "LVL2",
                            "total-TR": 0.0,
                            "2024-02-TR": 0
                        }
                    }
                },
                "total_row": {
                    "2024-01": {
                        "scriptname": "Total",
                        "total-TR": 31321.18312634954,
                        "2024-01-TR": 17019.66157312904,
                        "2024-02-TR": 14301.521553220495
                    },
                    "2024-02": {
                        "scriptname": "Total",
                        "total-TR": 26128.995384891645,
                        "2024-02-TR": 26128.995384891645
                    }
                }
            }
        resp_dict = xx.get('data')
        total_row = xx.get('total_row')
        message = {
                        "cardsV2": [
                            {
                                "cardId": "reminderCard",
                                "card": {
                                        "header": {
                                            "title": "{} CT Apps TR Summary {}".format('-'*25,'-'*25),
                                        },
                                        "sections": [
                                            
                                        ]
                                    },
                            },
                        ]
                }
        
        for month,monthdata in resp_dict.items():
            header_items = [
                                {
                                    "title": "Script Name",
                                    "textAlignment": "START"
                                },
                                # {
                                #     "title": "SubTeam",
                                #     "textAlignment": "START"
                                # },
                                {
                                    "title": "Total TR",
                                    "textAlignment": "END"
                                },
                            ]
            for month_next in resp_dict.keys():
                if month<=month_next:
                    print(month_next)
                    header_items.append({
                                            "title": "{} TR".format(datetime.strptime(month_next,'%Y-%m').strftime('%b')),
                                            "textAlignment": "END"
                                        })
            
            scriptname = total_row.get(month).get('scriptname')
            header_items.append({
                                "title":"{}".format(scriptname),
                                "textAlignment": "START"
                            })
            header_items.append({
                                "title":"{}".format(round(float(total_row.get(month).get('total-TR')),2)),
                                "textAlignment": "END"
                            })
            
            for month_next in resp_dict.keys():
                if month<=month_next:
                    try:
                        tr = round(float(total_row.get(month).get('{}-TR'.format(month_next))),2)
                    except:
                        tr = 0
                    header_items.append({
                                            "title": "{}".format(tr),
                                            "textAlignment": "END"
                                        })
            
            section_data = {
                                "header": "{} Apps".format(datetime.strptime(month,'%Y-%m').strftime('%B')),
                                "collapsible": True,
                                "uncollapsibleWidgetsCount": 7,
                                "widgets": [
                                    {
                                        "decoratedText":{
                                            "text":"Total New CT Apps : {}".format(len(monthdata.keys()))
                                        }
                                    },
                                    {
                                    "grid": {
                                        "columnCount": len(header_items)/2,
                                        "items": header_items
                                    }
                                    },
                                ]
                            }
            

            scriptdata_list = []
            for scriptname,scriptdata in monthdata.items():
                scriptdata_list.append(scriptdata)

            # for month_next in resp_dict.keys():
            #     if month<=month_next:
            #         scriptdata_list = sorted(scriptdata_list,key=lambda e: e.get('{}-TR'.format(month_next),0))

            scriptdata_list = sorted(scriptdata_list,key=lambda e: e.get('{}-TR'.format('total'),0))
            for scriptdata in scriptdata_list:
                scriptname = scriptdata.get('scriptname')
                row_items = [
                                {
                                    "title":"{}".format(scriptname),
                                    "textAlignment": "START"
                                },
                                # {
                                #     "subtitle":"{}".format(scriptdata.get('subteam')),
                                #     "textAlignment": "START"
                                # },
                                {
                                    "title":"{}".format(round(float(scriptdata.get('total-TR')),2)),
                                    "textAlignment": "END"
                                },
                            ]
                
                for month_next in resp_dict.keys():
                    if month<=month_next:
                        try:
                            tr = round(float(scriptdata.get('{}-TR'.format(month_next))),2)
                        except:
                            tr = 0
                        row_items.append({
                                                "title": "{}".format(tr),
                                                "textAlignment": "END"
                                            })
                section_data['widgets'].append({
                                                    "grid": {
                                                        "columnCount": len(row_items),
                                                        "items": row_items
                                                    }
                                                    })
            message['cardsV2'][0]['card']['sections'].append(section_data)
            
        googleChatBot_send_message('AAAAmJxziIo',message=message)    
        return Response({
            'data':resp_dict,
            'total_row':total_row
        })
