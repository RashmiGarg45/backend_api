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

from data_tracking.models import revenueReport,installReport,combined_app_data
from data_tracking.serializer import revenueReportSerializer
from data_tracking.helper.sheetbot import google_sheet
from data_tracking.util import get_credential

from data_tracking.util import get_list_data_from_raw,googleChatBot_send_message

from team2b.models import WatchoOrderIdsMining


class Report6Stats(APIView):
    def get(self, request):        
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        team = request.GET.get('team')
        bt_team = request.GET.get('bt_team')

        get_total_only =  request.GET.get('get_total_only',False)
        combined_app_data_map = {}
        other_data = request.GET.copy()
        if team:
            team_data = {
                '1':['Pushkal','Pawan'],
                '2':['Udit','Umair'],
                '3':['Shikha','Aniket'],
            }
            apps = combined_app_data.objects.filter(qa_upperlevel__in = team_data.get(team)).using('cm-env{}'.format(team))
            if not other_data.get('campaign'):
                list_apps = []               
                for item in apps:
                    combined_app_data_map[item.filename] = {
                        'package_name':item.pckname,
                        'qa_upperlevel':item.qa_upperlevel,
                    }
                    list_apps.append(item.filename)
                other_data['campaign'] = ",".join(list_apps)
        
        if get_total_only and get_total_only.lower() == 'false':
            get_total_only = False

        filter_dict = {
            'date__gte':start_date,
            'date__lte':end_date, 
        }
        for item in ['campaign','package_name']:
            if other_data.get(item):
                if ',' in other_data.get(item):
                    filter_dict[item+'__in'] =  other_data.get(item).split(',')
                else:
                    filter_dict[item] =  other_data.get(item)

        annotation_dict = {
            'total_revenue':Sum(F'revenue'),
            'i2_count':Sum('r_install')
        }

        r6_data = {}
        for env in ['1','2','3']:
            if not bt_team or bt_team==env:
                campaign_list = []
                data = revenueReport.objects.filter(**filter_dict).values('date','channel','network','offer_id','campaign').annotate(**annotation_dict).using('cm-env{}'.format(env))
                for item in data:
                    if item.get('channel').lower() not in ['vestaapps','77ads','offersinfinite']:
                        item['total_revenue'] = item.get('total_revenue')/0.7
                    
                    campaign_name = item.get('campaign')
                    date = str(item.get('date'))
                    if not r6_data.get(campaign_name):
                        r6_data[campaign_name] = {
                            'i1_count_range':0,
                            'i2_count_range':0,
                            'total_revenue_range':0,
                            'combined_data':combined_app_data_map.get(campaign_name,{})
                        }

                    r6_data[campaign_name]['i2_count_range']+=item.get('i2_count')
                    r6_data[campaign_name]['total_revenue_range']+=item.get('total_revenue')

                    if not get_total_only:
                        if not r6_data.get(campaign_name).get(date):
                            r6_data[campaign_name][date] = {
                                'i1_count':0,
                                'i2_count':0,
                                'total_revenue':0,
                            }
                        
                        r6_data[campaign_name][date]['i2_count']+=item.get('i2_count')
                        r6_data[campaign_name][date]['total_revenue']+=item.get('total_revenue')

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
                            'total_revenue_range':0,
                            'combined_data':combined_app_data_map.get(campaign_name,{})
                        }
                    r6_data[campaign_name]['i1_count_range']+=item.get('i1_count')

                    if not get_total_only:
                        if not r6_data.get(campaign_name).get(date):
                            r6_data[campaign_name][date] = {
                                'i1_count':0,
                                'i2_count':0,
                                'total_revenue':0
                            }
                        r6_data[campaign_name][date]['i1_count']+=item.get('i1_count')


        return HttpResponse(json.dumps({
            'data':r6_data,
        }))

class Report6UpdateOnSheet(APIView):
    def get(self,request):
        r6_obj = Report6Stats()
        sheet_url = request.GET.get('sheet_url','https://docs.google.com/spreadsheets/d/1hWMKvd3_uWyMn0dUFg04jT4XEyLr8MZUWiNHoYOiKVk/edit#gid=0')
        sheet_name = request.GET.get('sheet_name','Report 6')
        team = request.GET.get('team')
        bt_team = request.GET.get('bt_team')
        sheetname_update_not_allowed = request.GET.get('sheetname_update_not_allowed',False)

        if sheetname_update_not_allowed:
            pass
        else:
            if bt_team:
                sheet_name += '({}) {} {}'.format(datetime.utcnow().strftime('%b,%y'), team, 'BT-{}'.format(bt_team))
            else:
                sheet_name += '({})'.format(datetime.utcnow().strftime('%b,%y'))
        # request.GET['end_date'] = datetime.utcnow().strftime('%Y-%m-%d')
        resp_data = json.loads(r6_obj.get(request).content)
        rows_length = len(resp_data.get('data').keys())+10
        gs = google_sheet(sheet_url)
        try:
            worksheet = gs.add_worksheet(name=sheet_name,rows=rows_length,cols=26)
        except:
            worksheet = gs.open_worksheet(sheet_name)
        
        end_date = int(datetime.strptime(request.GET.get('end_date'),'%Y-%m-%d').strftime('%d'))
        no_of_days = (datetime.strptime(request.GET.get('end_date'),'%Y-%m-%d') - datetime.strptime(request.GET.get('start_date'),'%Y-%m-%d')).days
        new_rows = []
        new_rows.append(['Script Name','Package Name','Subteam', 'Total TR'])
        row_no=1
        for scriptname,scriptdata in resp_data.get('data').items():
            if scriptname:
                row_no+=1
                rr = [
                    scriptname,
                    scriptdata.get('combined_data',{}).get('package_name'),
                    scriptdata.get('combined_data',{}).get('qa_upperlevel'),
                    '=SUM(E{}:AZ{})'.format(row_no,row_no)
                ]
                for i in reversed(range(no_of_days+1+1)):
                    if i == 0:
                        pass
                    else:
                        dddd = (datetime.strptime(request.GET.get('end_date'),'%Y-%m-%d') - timedelta(days = (no_of_days-i))).strftime('%Y-%m-%d')

                        if dddd:
                            if dddd not in new_rows[0]:
                                new_rows[0].append(dddd)
                                
                            dd = scriptdata.get(dddd)
                            if dd:
                                rr.append(dd.get('total_revenue'))
                            else:
                                rr.append(0)

                new_rows.append(rr)

        worksheet.update('A1:CZZ{}'.format(len(new_rows)), new_rows, raw=False)

        return HttpResponse(json.dumps({
            'result':'updated',
        }))






class ChatBotNotRunLastTwoMonthLevel2(APIView):
    def get(self,request):
        # This Api will send a message to Chatbot where we can see which Apps have not been runned by BT.
        data = {}
        resp_dict = {}
        total_row = {}
        work_data_map = get_list_data_from_raw(data)
        start_date = '2024-01-01'
        end_date = '2024-03-20'
        done_data = list(filter(lambda element: ((element.get('Work Category').replace(' ','').replace('\t','').lower()=='lvl2' or element.get('Work Category').replace(' ','').replace('\t','').lower()=='lvl1') and (element.get('Working Status').replace(' ','').replace('\t','').lower()=='done' or element.get('Working Status').replace(' ','').replace('\t','').lower()=='doneconditionaly') and element.get('Done-Date').replace(' ','').replace('\t','').lower()>=start_date and element.get('Done-Date').replace(' ','').replace('\t','').lower()<=end_date),work_data_map))
        dict__ = {}
        camp_data_dict = {}
        for i in done_data:
            camp_name = i.get('AppName').strip()
            month = str(datetime.strptime(i.get('Done-Date'),'%Y-%m-%d').strftime('%Y-%m'))
            if not dict__.get(month):
                dict__[month] = []
            dict__[month].append(camp_name)
            camp_data_dict[camp_name] = i

        for month,campaigns in dict__.items():
            if not resp_dict.get(month):
                resp_dict[month] = {}
            if not total_row.get(month):
                total_row[month] = {'scriptname':'Total','total-TR':0}
            for month_next in dict__.keys():
                if month_next>=month:

                    import calendar
                    strt_end = calendar.monthrange(int(month_next.split('-')[0]), int(month_next.split('-')[1]))
                    start_date_month = '{}-{}'.format(month_next,'01')
                    end_date_month = '{}-{}'.format(month_next,strt_end[1])
                    request.GET = {
                        'start_date':start_date_month,
                        'end_date':end_date_month,
                        'campaign':",".join(campaigns)
                    }
                    
                    r6_obj = Report6Stats()
                    resp_data = json.loads(r6_obj.get(request).content)
                    raw_data = resp_data.get('data')
                    for scriptname,scriptdata in raw_data.items():
                        if not resp_dict.get(month).get(scriptname):
                            resp_dict[month][scriptname] = {
                                                        'scriptname':scriptname,
                                                        'subteam':camp_data_dict.get(scriptname,{}).get('Dev-Team'),
                                                        'done_date':camp_data_dict.get(scriptname,{}).get('Done-Date'),
                                                        'level':camp_data_dict.get(scriptname,{}).get('Work Category'),
                                                        'total-TR':0,
                                                    }
                        
                        
                        resp_dict[month][scriptname]['{}-TR'.format(month_next)] = scriptdata.get('total_revenue_range')
                        resp_dict[month][scriptname]['{}-TR'.format('total')]+=float(scriptdata.get('total_revenue_range',0))
                        
                        if not total_row.get(month).get('{}-TR'.format(month_next)):
                            total_row[month]['{}-TR'.format(month_next)] = 0
                        total_row[month]['{}-TR'.format(month_next)] += float(scriptdata.get('total_revenue_range',0))
                        total_row[month]['{}-TR'.format('total')] += float(scriptdata.get('total_revenue_range',0))

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
        
        space_name = request.GET.get('space_name','AAAA7sIzS9Q')
        googleChatBot_send_message(space_name=space_name,message=message)   

        for month,monthdata in resp_dict.items():
            header_row = ['ScriptName','SubTeam','Done Date','Level','Total TR']
            header_key_row = ['scriptname','subteam','done_date','level','total-TR']
            rows = [[],['']]
            for scriptname,scriptdata in monthdata.items():
                row = []
                for key in sorted(scriptdata.keys()):
                    if key not in header_key_row:
                        header_row.append(key)
                        header_key_row.append(key)

                for item in header_key_row:
                    row.append(scriptdata.get(item))
                rows.append(row)
            rows[0] = header_row
            sheet_url = request.GET.get('sheet_url','https://docs.google.com/spreadsheets/d/1hWMKvd3_uWyMn0dUFg04jT4XEyLr8MZUWiNHoYOiKVk/edit#gid=0')
            sheet_name = request.GET.get('sheet_name','Newapp Data')
            sheet_name += '({})'.format(month)
            gs = google_sheet(sheet_url)
            try:
                worksheet = gs.add_worksheet(name=sheet_name,rows=1000,cols=26)
            except:
                worksheet = gs.open_worksheet(sheet_name) 
            
            worksheet.update('A1:CZZ{}'.format(len(rows)), rows, raw=False)

        

        
        return Response({
            'data':resp_dict,
            'total_row':total_row
        })


class WatchoUpdateSheet(APIView):
    def get(self,request):
        sheet_url = 'https://docs.google.com/spreadsheets/d/1Wwzxg1wIsrnr1FD74DYIgzissUlziGcZJ8H2xsbpnt4/edit?gid=0#gid=0'
        subsheet_name = 'OrderIDs'

        credentials = get_credential()

        Sheet_credential = gspread.service_account_from_dict(credentials)
        spreadsheet = Sheet_credential.open_by_url(sheet_url)
        worksheet = spreadsheet.worksheet(subsheet_name)
        
        data = WatchoOrderIdsMining.objects.values_list("created_at", "id", "used_at", "spdn")

        headers = ["created_at", "id", "used_at", "spdn"]
        worksheet.update("A1", [headers]) 

        worksheet.update(f"A2", list(data))


        return HttpResponse(json.dumps({
            'result':'updated',
        }))
