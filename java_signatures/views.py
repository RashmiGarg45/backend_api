from django.http import HttpResponse
import subprocess
import json
from subprocess import STDOUT, PIPE
import sqlite3
import random
import execjs
import time
import requests
import mysql.connector as mysql
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from collections import defaultdict
from datetime import datetime, timedelta
from django.utils import timezone

from java_signatures.models import InstallData, EventInfo, ExchangeRate, InstallDataTZ, EventInfoTZ
from rest_framework.response import Response
from django.db import connections

def get_signtaure(request):
    data = json.loads(request.body)
    args_list = data.get("args")
    script_name = data.get("script_name")
    encrypted_data = execute_java(script_name, argument_list=args_list)
    return HttpResponse(encrypted_data)

def execute_java(java_file, argument_list=[]):
    cmd = ['java', java_file]
    for item in argument_list:
        cmd.append(str(item))
    proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    stdout, stderr = proc.communicate(b'1')
    if stderr:
        print (stderr)
    return stdout


@api_view(['POST'])
def add_install_count(request):
    request_data = json.loads(request.body)
    campaign_name = request_data.get("name")
    channel = request_data.get("channel", "*")
    network = request_data.get("network", "*")
    offer_id = request_data.get("offer_id", "*")

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()

        created_at = datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
        cursor.execute('''INSERT INTO check_event_count (created_at, campaign_name, channel, network, offer_id)
                        VALUES ('{}', '{}', '{}', '{}', '{}')'''.format(created_at, campaign_name, channel, network, offer_id))
        conn.commit()

        response_code = 200
        message = "success"
        data = {"created_at": str(created_at)}

    except Exception as e:
        response_code = 500
        message = str(e)
        data = {}

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "data": data}))

def is_event_allowed(request):
    request_data = json.loads(request.body)
    campaign_name = request_data.get("name")
    event_type = request_data.get("event_type")
    current_date = request_data.get("current_date")
    channel = request_data.get("channel", "*")
    network = request_data.get("network", "*")
    offer_id = request_data.get("offer_id", "*")
    required_percentage = request_data.get("required_percentage")

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()

        cursor.execute('''SELECT COUNT(*) FROM check_event_count WHERE campaign_name ='{}' AND channel='{}' AND network='{}' AND offer_id='{}' AND created_at LIKE '{}%';'''.format(campaign_name, channel, network, offer_id, current_date))
        result = cursor.fetchall()
        install_count = result[0][0]

        cursor.execute('''SELECT COUNT(*) FROM check_event_count WHERE campaign_name ='{}' AND channel='{}' AND network='{}' AND offer_id='{}' AND created_at LIKE '{}%' AND {} = 1;'''.format(campaign_name, channel, network, offer_id,current_date, event_type))
        result = cursor.fetchall()
        event_count = result[0][0]

        current_percentage = (event_count/install_count)*100
        if current_percentage < required_percentage.get(event_type):
            is_allowed = True
        else:
            is_allowed = False 
        
        response_code = 200
        message = "success"
        data = {"is_allowed": is_allowed, "install_count": install_count, "event_count": event_count, "current_percentage": current_percentage}

    except Exception as e:
        response_code = 500
        message = str(e)
        data = {}   

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "data": data}))

@api_view(['POST'])
def update_event_count(request):
    request_data = json.loads(request.body)
    campaign_name = request_data.get("name")
    created_at = request_data.get("created_at")
    event_origin = request_data.get("event_origin")
    channel = request_data.get("channel", "*")
    network = request_data.get("network", "*")
    offer_id = request_data.get("offer_id", "*")

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()
        cursor.execute('''UPDATE check_event_count SET {} = 1 WHERE created_at = '{}' AND campaign_name ='{}' AND channel='{}' AND network='{}' AND offer_id='{}';'''.format(event_origin, created_at, campaign_name, channel, network, offer_id))
        conn.commit()

        response_code = 200
        message = "success"

    except Exception as e:
        response_code = 500
        message = str(e)

    return HttpResponse(json.dumps({"response_code": response_code, "message": message}))


def cipher(decrypted_text=None,encrypted_text=None, _key="iGvRAL5CpW4cp#LCDF2T"):
    code = '''
    "use strict";

    var n = require('crypto-js');

    var o = {
        stringify: function(f) {
            var _ = n.enc.Hex.parse(f.salt.toString()).toString(n.enc.Latin1),
                d = f.ciphertext.toString(n.enc.Latin1);
            return n.enc.Latin1.parse("Salted__" + _ + d).toString(n.enc.Base64);
        },
        parse: function(_) {
            if ("Salted__" !== (_ = n.enc.Base64.parse(_).toString(n.enc.Latin1)).substr(0, 8)) {
                throw new Error("Error parsing salt");
            }
            // console.log(_);
            var p = _.substr(8, 8),
                y = _.substr(16);

            // console.log(p);
            // console.log(y);

            return n.lib.CipherParams.create({
                ciphertext: n.enc.Latin1.parse(y),
                salt: n.enc.Latin1.parse(p)
            });
        }
    };

    module.exports = {
        encrypt: function(f, _) {
            return n.AES.encrypt(f, _, { format: o }).toString();
        },
        decrypt: function(f, _) {
            return n.AES.decrypt(f, _, { format: o }).toString(n.enc.Utf8);
        }
    };

    var key = "iGvRAL5CpW4cp#LCDF2T";

    var plaintext = '{"versao":"3.1.4"}';

    var encryptedText = module.exports.encrypt(plaintext, key);
    console.log('Encrypted:', encryptedText);

    var decryptedText = module.exports.decrypt(encryptedText, key);
    console.log('Decrypted:', decryptedText);
    '''
    ctx = execjs.compile(code)
    
    key = _key

    if encrypted_text:
        # encrypted_text = "U2FsdGVkX18XhGeLwLLRzruAHaVzBtzCwKhCaONA6H4+LRIW8qbr1f2UkGQaFhbFTZWyp5RX8M4t5rsEpbMKBQ9lMHy+z88oXYePL2KeaUaSF2zcHK9lRWgMEoebcRg4vme5/aE98V3N9P1Gys00VYKl01jYxd7cYLn3mdz4iEy9LiobAMpXAQHBvpmmdPqfsKEnbpPD09QJrBKLwUZVhSDiUFjoV4lhD/6uH9uAwwQaX9ubzsC4yoet9A/nKSUIsm/mWpPj/uV06sAolSPFkjmOYKxJgB6U2aCaE4aXL8zcSkfCVjaTNvRs8KJ01uA36RY0VCu7EXaNutaehVt5NldqiZDCviI2X2Ggovn74/qfTQ0APiIJgli095UDd6AhS8N010F4dWxTOZuufBeXn1niAhHALTmtpcrsEMqT0yM1Vs+lzyvEoti7bB5YxPF+b7kAQgL64I6hEtHiAuBSIw=="
        decrypted_text = ctx.call('module.exports.decrypt', encrypted_text, key)
        return decrypted_text

    if decrypted_text:
        # decrypted_text='{"carrinho_id":"96173802","forma_pagamento":"offline","deviceData":null,"dinheiro":0,"forma_pagamento_offline":"5","observacoes":"","latitude":null,"longitude":null,"dispositivo":{"dispositivo":"03c7d8269e2a41f8","plataforma":"Android","modelo":"Redmi K20 Pro","versao_app":"3.1.4","versao":"10"},"pagamento_via_pix":false}'
        encrypted_text=decrypted_text = ctx.call('module.exports.encrypt', decrypted_text, key)
        return encrypted_text
        
def ragazzo_signature(request):
    data = json.loads(request.body)
    encrypted_string = data.get("encrypted_string")
    decrypted_string = data.get("decrypted_string")
    key = data.get("key", "iGvRAL5CpW4cp#LCDF2T")

    try:       
        if encrypted_string:
            output = cipher(encrypted_text=encrypted_string, _key=key)
        if decrypted_string:
            output = json.dumps(cipher(decrypted_text=decrypted_string, _key=key))

        response_code = 200
        message = "success"

    except Exception as e:
        response_code = 500
        message = str(e)
        output = ""

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "data": output}))


@api_view(['PUT'])
def put_data(request):
    request_data = json.loads(request.body)
    camp_name = request_data.get("camp_name")
    data = request_data.get("data")
    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor() 

        if camp_name == "pocket52":
            cursor.execute('''SELECT DISTINCT user_id FROM pocket52_userId''')
            sql_data = cursor.fetchall()

            already_present_user_ids = []
            for row in sql_data:
                already_present_user_ids.append(str(row[0]))

            for user_id in data:
                if str(user_id) not in already_present_user_ids:
                    created_at = datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
                    cursor.execute('''INSERT INTO pocket52_userId (user_id, created_at, isUsed)
                                        VALUES ('{}','{}', 0)'''.format(user_id ,created_at ))
                    conn.commit()

        elif camp_name == "muthoot":
            cursor.execute('''SELECT DISTINCT user_id FROM muthootfino_userId''')
            sql_data = cursor.fetchall()

            already_present_user_ids = []
            for row in sql_data:
                already_present_user_ids.append(str(row[0]))

            for user_id in data:
                if str(user_id) not in already_present_user_ids:
                    created_at = datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
                    cursor.execute('''INSERT INTO muthootfino_userId (user_id, created_at, isUsed)
                                        VALUES ('{}','{}', 0)'''.format(user_id ,created_at ))
                    conn.commit()

        elif camp_name == "sportsbaazi":
            cursor.execute('''SELECT DISTINCT user_id FROM sportbaazi_userId''')
            sql_data = cursor.fetchall()

            already_present_user_ids = []
            for row in sql_data:
                already_present_user_ids.append(str(row[0]))

            for user_id in data:
                if str(user_id) not in already_present_user_ids:
                    created_at = datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
                    cursor.execute('''INSERT INTO sportbaazi_userId (user_id, created_at, isUsed)
                                        VALUES ('{}','{}', 0)'''.format(user_id ,created_at ))
                    conn.commit()

        elif camp_name == "toonsutra":
            cursor.execute('''SELECT DISTINCT user_id FROM toonsutra_user_data''')
            sql_data = cursor.fetchall()

            already_present_user_ids = []
            for row in sql_data:
                already_present_user_ids.append(str(row[0]))

            for d in data:
                user_id = d.get("user_id")
                details = d.get("details")
                if str(user_id) not in already_present_user_ids:
                    created_at = datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
                    cursor.execute('''INSERT INTO toonsutra_user_data (user_id, extra_details, createdAt, isUsed)
                                        VALUES ('{}','{}', '{}', 0)'''.format(user_id , json.dumps(details),created_at ))
                    conn.commit()

        elif camp_name == "bottles":
            cursor.execute('''SELECT DISTINCT order_id FROM bottles_order_data''')
            sql_data = cursor.fetchall()

            already_present_user_ids = []
            for row in sql_data:
                already_present_user_ids.append(str(row[0]))

            for d in data:
                order_id = d.get("order_id")
                order_total = d.get("order_total")
                order_date = d.get("order_date")
                if str(order_id) not in already_present_user_ids:
                    created_at = datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
                    cursor.execute('''INSERT INTO bottles_order_data (order_id, order_total, order_date, createdAt, isUsed)
                                        VALUES ('{}','{}','{}', '{}', 0)'''.format(order_id , order_total, order_date,created_at ))
                    conn.commit()

        elif camp_name == "lenskart":
            cursor.execute('''SELECT DISTINCT order_id FROM lenskart_orderId''')
            sql_data = cursor.fetchall()

            already_present_user_ids = []
            for row in sql_data:
                already_present_user_ids.append(str(row[0]))

            for order_id in data:
                if str(order_id) not in already_present_user_ids:
                    created_at = datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
                    cursor.execute('''INSERT INTO lenskart_orderId (order_id, created_at, isUsed)
                                        VALUES ('{}','{}', 0)'''.format(order_id, created_at ))
                    conn.commit()

        elif camp_name == "derma":
            cursor.execute('''SELECT DISTINCT order_id FROM derma_user_data''')
            sql_data = cursor.fetchall()

            already_present_user_ids = []
            for row in sql_data:
                already_present_user_ids.append(str(row[0]))

            for d in data:
                order_id = d.get("order_id")
                order_total = d.get("order_total")
                order_date = d.get("order_date")
                system_order_id = d.get("system_order_id")
                AWB = d.get("AWB")
                if str(order_id) not in already_present_user_ids:
                    created_at = datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
                    cursor.execute('''INSERT INTO derma_user_data (order_id, order_total, order_date, system_order_id, createdAt, isUsed, AWB)
                              VALUES ('{}', '{}', '{}', '{}','{}', 0, '{}')'''.format(order_id, order_total, order_date, system_order_id ,created_at , AWB))
                    conn.commit()

        elif camp_name == "flappdeals":
            cursor.execute('''SELECT DISTINCT order_id FROM flappdeals_orderIds''')
            sql_data = cursor.fetchall()

            already_present_user_ids = []
            for row in sql_data:
                already_present_user_ids.append(str(row[0]))

            for user_id in data:
                if str(user_id) not in already_present_user_ids:
                    created_at = datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
                    cursor.execute('''INSERT INTO flappdeals_orderIds (created_at, isUsed, order_id)
                                                     VALUES ('{}',0, '{}')'''.format(created_at, json.dumps(user_id)))
                    conn.commit()

        elif camp_name == "finimize":
            cursor.execute('''SELECT DISTINCT user_id FROM finimizeios_user_data''')
            sql_data = cursor.fetchall()

            already_present_user_ids = []
            for row in sql_data:
                already_present_user_ids.append(str(row[0]))

            for d in data:
                user_id = d.get("user_id")
                subs_type = d.get("subs_type")
                os_type = d.get("os_type")
                user_details = d.get("user_details")
                if str(user_id) not in already_present_user_ids:
                    created_at = datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
                    cursor.execute('''INSERT INTO finimizeios_user_data (createdAt, isUsed, user_id,extra_details,subs_type,os_type)
                                                                     VALUES ('{}',0,'{}','{}','{}','{}')'''.format(created_at,user_id,json.dumps(user_details),subs_type,os_type))
                    conn.commit()

        elif camp_name == "tajrummy":
            cursor.execute('''SELECT DISTINCT user_id FROM tajrummey_userId''')
            sql_data = cursor.fetchall()

            already_present_user_ids = []
            for row in sql_data:
                already_present_user_ids.append(str(row[0]))

            for user_id in data:
                if str(user_id) not in already_present_user_ids:
                    created_at = datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
                    cursor.execute('''INSERT INTO tajrummey_userId (user_id, created_at, isUsed)
                                        VALUES ('{}','{}', 0)'''.format(user_id ,created_at ))
                    conn.commit()

        conn.close()
        response_code = 200
        message = "success"

    except Exception as e:
        response_code = 500
        message = str(e)
        data = {}

    return HttpResponse(json.dumps({"response_code": response_code, "message": message}))

def get_event_info(request):
    campaign_name = request.GET.get('campaign_name')
    channel = request.GET.get('channel')
    network = request.GET.get('network')
    offer_id = request.GET.get('offer_id')
    date_ = datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d")
    event_name = request.GET.get('event_name')

    try:
        conn = mysql.connect(host="t2-services-mysql.cjiqfqhzkajl.ap-south-1.rds.amazonaws.com", user="admin", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()

        cursor.execute('''SELECT COUNT(*) FROM team2b_revenuehelper WHERE event_name = "Install" AND campaign_name = "{}" AND channel ="{}" AND network = "{}" AND offer_id= "{}" AND created_at > "{}"'''.format(campaign_name, channel, network, offer_id, date_))
        data = cursor.fetchall()
        install_count = data[0][0]


        cursor.execute('''SELECT SUM(revenue), COUNT(revenue) FROM team2b_revenuehelper WHERE event_name = "{}" AND campaign_name = "{}" AND channel ="{}" AND network = "{}" AND offer_id= "{}" AND created_at > "{}"'''.format(event_name, campaign_name, channel, network, offer_id, date_))
        data = cursor.fetchall()
        
        total_revenue = data[0][0]
        event_count = data[0][1]

        response_code = 200
        message = "success"

        if total_revenue is None:
            total_revenue = 0.00001
        if install_count is None:
            install_count = 0
        if event_count is None:
            event_count = 0

        # query = '''
        #     SELECT 
        #         SUM(CASE WHEN event_name = "Install" THEN 1 ELSE 0 END) AS install_count,
        #         SUM(CASE WHEN event_name = %s THEN 1 ELSE 0 END) AS event_count,
        #         COALESCE(SUM(revenue), 0.00001) AS total_revenue
        #     FROM team2b_revenuehelper
        #     WHERE campaign_name = %s
        #     AND channel = %s
        #     AND network = %s
        #     AND offer_id = %s
        #     AND created_at > %s
        # '''

        # params = (event_name, campaign_name, channel, network, offer_id, date_)
        # cursor.execute(query, params)
        # data = cursor.fetchone()

        # install_count, event_count, total_revenue = data

        cursor.close()
        conn.close()

        data = {"install_count": install_count , "event_count": event_count , "total_revenue": total_revenue }

    except Exception as e:
        response_code = 500
        message = str(e)
        data = {"install_count": 0, "event_count": 0, "total_revenue": 0.00001}

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "data": data}))


def get_data(request):
    campaign_name = request.GET.get('campaign_name')
    date_ = request.GET.get('date')

    try:
        conn = mysql.connect(host="t2-services-mysql.cjiqfqhzkajl.ap-south-1.rds.amazonaws.com", user="admin", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM team2b_revenuehelper WHERE campaign_name = "{}" AND DATE(created_at) = "{}"'''.format(campaign_name, date_))
        data = cursor.fetchall()  

        entry_data = {"installs": 0, "event_stats": {}}

        for d in data:
            campaign_name, date, _, _, channel, network, offer_id, _, revenue, _, _, event_name,_,_,_,_ = d

            if event_name == "Install":
                entry_data["installs"] += 1

            event_data = entry_data["event_stats"].setdefault(event_name, {"count": 0, "revenue": 0})
            event_data["count"] += 1
            event_data["revenue"] += revenue

        final_output = {
            "campaign_name": campaign_name,
            "date": date,
            "channel": channel,
            "network": network,
            "offer_id": offer_id,
            "entry_data": entry_data
        }   



        response_code = 200
        message = "success"

        cursor.close()
        conn.close()

        data = {"data": data }

    except Exception as e:
        response_code = 500
        message = str(e)
        data = {"data": {}}

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "data": data}))


class TrackInstalls(APIView):
    def put(self, request):
        campaign_name = request.GET.get('campaign_name')
        channel = request.GET.get("channel")
        network = request.GET.get("network")
        offer_id = request.GET.get("offer_id")
        currency = request.GET.get("currency", "USD")
        required_timezone = request.GET.get("required_timezone")
        

        date = datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d")      

        if not all([campaign_name, channel, network, offer_id]):
            return Response({"status": 400,"message": "Missing required parameters","data": {}})
        
        install_data = InstallData.objects.filter(campaign_name=campaign_name, created_at=date, channel=channel, network=network, offer_id=offer_id)            

        if not install_data:
            install_details = InstallData(created_at=date, campaign_name=campaign_name, channel=channel, network=network, offer_id=offer_id, currency=currency, installs=1)
        else:
            install_details = install_data.get()
            install_details.installs += 1
        install_details.save()

        return Response({"status": 200, "message": "Install Tracked", "data": {"count": install_details.installs, "serial": install_details.serial}})

class TrackEvents(APIView):
    def put(self, request):
        campaign_name = request.GET.get('campaign_name')
        event_name = request.GET.get("event_name")
        offer_serial = request.GET.get("offer_serial")
        event_day = request.GET.get("event_day")
        event_value = request.GET.get("event_value")
        revenue = float(request.GET.get("revenue", 0))
        required_timezone = request.GET.get("required_timezone")

        if not all([campaign_name, event_name, offer_serial, event_day]):
            return Response({"status": 400,"message": "Missing required parameters","data": {}})
        
        if required_timezone:
            try:
                import pytz
                print (required_timezone)
                tz = pytz.timezone(required_timezone)
                date = datetime.now(tz).date()
                print ("kfc", date)
            except Exception as e:
                print (e)
                date = datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d")
        else:
            date = datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d")
        
        # if required_timezone: 
        #     offer_serial = InstallDataTZ(offer_serial)
        # else:       
        offer_serial = InstallData(offer_serial)

        # if required_timezone:
        #     event_data = EventInfoTZ.objects.filter(created_at=date,campaign_name=campaign_name, offer_serial=offer_serial, event_name=event_name, event_day=event_day)
        # else:
        event_data = EventInfo.objects.filter(campaign_name=campaign_name, offer_serial=offer_serial, event_name=event_name, event_day=event_day)

        if not event_data:
            # if required_timezone:
            #     event_details = EventInfoTZ(created_at=date, campaign_name=campaign_name, offer_serial=offer_serial, event_name=event_name, event_count=1, event_day=event_day, revenue=revenue)
            # else:
            event_details = EventInfo(campaign_name=campaign_name, offer_serial=offer_serial, event_name=event_name, event_count=1, event_day=event_day, revenue=revenue)
        else:
            event_details = event_data.get()
            event_details.event_count += 1
            event_details.revenue += revenue
        event_details.save()
        
        return Response({"status": 200, "message": "Event Tracked", "status": 200, "data": {"count": event_details.event_count, "revenue": event_details.revenue}})

def events_per_day_stats(campaign_name, event_name, channel, network, offer_id):

    if campaign_name == "kfcmexicotmodd" and offer_id in ["kfcaosneommp", "kfcmxneommp", "kfcneomacmmp", "kfcneozigmmp", "kfcdormmp", 'test']:
        return 11

    if campaign_name == "kfcmexicotmodd" and offer_id in ["kfcnapmmp", "kfcnopmmp", "test_new"]:
        return 12
    
    elif campaign_name == "kfcmexicotmodd":
        return 17 #percentage
    
    elif campaign_name == "netshoesmodd" and offer_id in ["nesmetmmp", "test"]:
        return 24
    
    elif campaign_name == "netshoesmodd" and offer_id in ["dope-netshoes-251030"]:
        return 1
    
    elif campaign_name == "williamhillsportiosmodd" and offer_id in ["apps-whsports.ios", "wiladummp"]:
        return 1
    
    elif campaign_name == "lottermxiosmodd"  and channel in ["mobpine", "77ads", "appamplify"]:
        return 3
    
    elif campaign_name == "williamhillsportiosmodd" and offer_id in ["ahwilkspmmp", "test"] and event_name =="FTD":
        return 15
    
def get_stats(campaign_name):
    STATS = {
        "quickcashonlinemodd": {
            "approvals_cnt_server": {0: 41, 1:24, 2:19, 3:16.6}
            },

        "moomootrademodd": {
            "af_ss_event_202": {1: 41, 2:33, 3:23},
            "af_ss_event_81": {0: 24, 1: 14, 2:11, 3:9.5}
            },

        "bd678auto": {
            "8jcdcl": {0:14.28, 1:11.11, 2:9.09, 3: 8.33}
            },

        "fb77auto": {
           "f80wwq" : {0:14.28, 1:12.5, 2:11.11, 3:10}
            },

        "ragnarokmodd": {
            "revenue_490": {0: 40, 2:30},
            "revenue_1500": {0: 15},
            "revenue_1000": {1: 40, 4:30},
            "revenue_100": {3: 40, 5:30}
            },

        "moovauto": {
            "xgivki":  {
                "vestaapps::vkmdigital::movkmvammpdup": {0: 4, 1:4}
                },
            "ld4kw6":  {
                "vestaapps::vkmdigital::movkmvammpdup": {0: 19, 1:19},
                "*::*::*": {0:11, 1:8.3 , 2: 6.6, 3: 6.6}
                },

            "ggjyhe": {0:20, 1:14.28, 2:11.11, 3: 9}
            },

        "boylesportstmodd": {
            "n_ftd": {0:43, 1:25, 2:20},
            "n_reg_confirm": {0: 25, 1:16.6, 2: 10}

            },

        "singamodd": {
            "risk-control": {0: 43, 1: 27},
            "loanapplied": {0: 43, 1: 43}
            },

        "leonrutmodd": {
            "af_first_deposit": {0: 27, 1: 22, 2: 18}
            },

        "ikukuruuiosauto": {
            "mcaw45": {0: 6, 1: 6},
            "wvzrbc": {0: 12, 1: 12}
            },

        "juanhandmodd": {
            "af_fst_insbrw_suss": {
                "mobpine::*::*": {0: 33, 1: 20, 2: 14.28, 3: 12.5},
                "77ads::*::*": {0: 33, 1: 20, 2: 14.28, 3: 12.5},
                "appamplify::*::*": {0: 33, 1: 20, 2: 14.28, 3: 12.5},
                "*::*::*": {0: 45, 1: 35, 2: 25, 3: 20, 4: 16}
            },
            "af_tzmx_10": {0: 47, 1: 33, 2: 24, 3: 20, 4: 15}
            },

        "ucuzabiletauto": {
            "vnc85a": {0: 20, 1: 12.5, 2: 10, 3: 8.7}
            },

        "profit2modd": {
            "ActionNewOrder": {0: 10, 1: 8.3, 2: 7.14, 3: 6.6}
            },

        "dupoiniosauto": {
            "7py4mn": {0: 23, 1: 16.6, 2: 12.5, 3: 10}
            },

        "loveparadaiseauto": {
            "revenue_199": {0: 25, 1: 20, 2: 16.6, 3: 14.2, 4: 12.5, 5: 11.11},
            "revenue_499": {0: 68, 1: 45, 2: 30}
            },

        "cashroyaleauto": {
            "revenue_599": {0: 20, 1: 16.66, 3: 14.28},
            "revenue_999": {1: 80, 2: 41, 4: 30}
            },

        "moneycolorauto": {
            "revenue_199": {0: 10, 1: 6.6, 2: 5.5, 3: 4.76, 4: 4.16, 5: 3.84, 6: 3.44, 7: 3.22},
            "revenue_499": {0: 16.6, 1: 11.11, 2: 8.33, 3: 7.14, 4: 6.25, 5: 5.5, 6: 5, 7: 4.54}
            },

        "dailysolitaremodd": {
            "revenue_099": {0: 13, 1: 10, 3: 7.5, 4: 6, 6: 4, 7: 3.5},
            "revenue_599": {0: 7.5, 1: 7.5, 2: 7, 3: 6, 4: 5, 5: 4.28}
            },

        "tikettmodd": {
            "af_purchase": {0: 50, 1: 50, 2: 33.3},

            "af_purchase_toDO": {
                "77ads::dopemobi::9dope-todo": {0: 20, 1: 12.5, 2: 10, 3: 8},
                "*::*::*": {0: 14, 1: 11, 2: 10, 3: 8}
            },

            "af_purchase_hotel": {
                "77ads::dopemobi::9dope-hotel": {0: 20, 1: 12.5, 2: 10, 3: 8},
                "*::*::*": {0: 14, 1: 12, 2: 9, 3: 8}
            },

            "af_purchase_flight": {
                "77ads::dopemobi::9dope-flight": {0: 20, 1: 12.5, 2: 10, 3: 8},
                "*::*::*": {0: 16.6, 1: 12.5, 2: 11, 3: 8}
                }
            },

            "axisinvestmodd": {
                "TXN Successful": {0: 29, 1: 26, 2: 20, 3: 16.6, 4: 14.28, 5: 12.5, 6: 12.5}
            },

            "moneymetmodd": {
                "LoanApplicationV2.ApplicationSent.View": {0: 70, 1: 50, 2: 33, 3: 33}
            },

            "moneycatmxmodd": {
                "NEW_LOAN": {0: 150, 1: 150}
            },

            "signnowmodd": {
                "af_start_trial": {0: 20, 1: 14.2, 2: 11.11, 3: 10},
                "af_purchase": {2: 100, 3: 100},
                "af_subscribe": {8: 50, 9: 50}
            },

            "hoteltonightautoios": {
                "pey3pd": {
                    "adshustle::advivifymedia::21653946": {0: 12.5, 1: 9, 2: 7.14, 3: 6.25},
                    "adshustle::advivifymedia::21676889": {0: 12.5, 1: 9, 2: 7.14, 3: 6.25},
                    "adshustle::attrimob::817dup": {0: 6.6, 1: 5, 2: 4, 3: 3.33},
                    "*::*::*": {0: 16.6, 1: 11.11, 2: 8.33, 3: 7.14, 4: 6.6}
                }
            },

            "hoteltonightauto": {
                "jviyct": {0: 16.6, 1: 11.11, 2: 8.33, 3: 7.14, 4: 6.6}
            },

            "magztermodd": {
                "mg_1month_freetrial": {0: 20, 1: 14.2, 2: 11.11, 3: 10},
                "mg_1year_freetrial": {0: 20, 1: 14.2, 2: 11.11, 3: 10}
            },

            "paysettmodd": {
                "registration_success": {0: 2, 1: 1.81, 2: 1.6},
                "send_success": {0: 10, 1: 7.14, 2: 6.25, 3: 5.5}
            },

            "puntitmodd": {
                "FTD": {0: 40, 1: 25}
            },

            "friendipayomauto": {
                "lql86o": {0: 10, 1: 8, 2: 6.5}
            },

            "novawateriosmodd": {
                "af_purchase": {0: 16, 1: 12.5, 2: 10}
            },

            "dimemodd": {
                "onboardSuccess": {0: 10, 1: 7, 2: 5, 3: 4.34, 4: 3.8}
            },

            "dailynumbermatchauto": {
                "pdeipy": {0: 30, 1: 30, 2: 25, 3: 25, 4: 20, 5: 20}
            },

            "cubiosmodd": {
                "esign_View_ActivateCL": {0: 85, 1: 80, 2: 60, 3: 45, 4: 33}
            },

            "bingofrenzytmodd": {
                "1_99": {0: 7, 1: 7},
                "4_99": {4: 7, 5: 7},
                "9_99": {2: 7, 3: 7}
            },

            "imagineartautoios": {
                "h5ihok": {0: 80, 1: 33.33},
                "pdc6m9": {0: 80, 1: 50}
            },

            "betrmodd": {
                "af_purchase": {0: 80, 1: 50, 2: 33.33}
            },

            "uiuxmobileauto": {
                "rmlund": {0: 45, 1: 33.33, 2: 25, 3: 20},
                "jjww2u": {0: 80}
            },

            "bybittmodd": {
                "eftd": {0: 90, 1: 45},
                "ftd": {0: 80, 1: 16.67}
            },

            "caesarsmodd": {
                "mb_deposit.first_time_deposit": {0: 15, 1: 15}
            },

            "newdouluomodd": {
                "0_99": {0: 23, 2: 20, 4: 16.67, 5: 14.28, 6: 12.5, 7: 14.28},
                "4_99": {0: 29, 1: 25, 3: 20, 5: 16.6, 6: 14.28, 7: 12.5},
                "9_99": {1: 41, 3: 33, 5: 25, 7: 20},
                "14_99": {2: 41, 4: 33, 6: 25}
            },

            "caesarscasinoiosmodd": {
                "mb_deposit.first_time_deposit": {
                    "*::*::caednommp": {0: 15},  # specific offer_id
                    "adshustle::*::*": {0: 20},  # specific channels
                    "vestaapps::*::*": {0: 20},
                    "appsfollowing::*::*": {0: 20},
                    "appsatiate::*::*": {0: 20},
                    "*::*::*": {0: 55, 1: 50}    # fallback
                }
            },

            "mullerauto": {
                "x2mrfw": {0: 1.5, 1: 1.2},
                "fihqvn": {0: 1.8, 1: 1.6}
            },

            "13cabstauto": {
                "swtdbc": {0: 1.5, 1: 1.5}
            },

            "13cabsiosauto": {
                "swtdbc": {0: 1.5, 1: 1.5}
            },

            "khiladiaddamodd": {
                "af_complete_registration": {0: 1.8, 1: 1.53, 2: 1.42, 3: 1.33}
            },

            "boylesportsiostmodd": {
                "n_ftd": {0: 43, 1: 25, 2: 20},
                "n_reg_confirm": {0: 25, 1: 16.6, 2: 10}
            },

            "bcsinvestmenttmodd": {
                "93441_Onboard_OpenAcc_SignDocsSmsTap": {0: 6.2, 1: 5, 2: 4.34, 3: 4, 4: 3.84},
                "28500_Instr_Bid_Success": {
                    "adshustle::*::bcsmnditvammp": {0: 9},
                    "adshustle::*::bcsmicovammp": {0: 9},
                    "*::*::*": {0: 45, 1: 23}
                }
            },

            "bcsinvestiosmodd": {
                "93441_Onboard_OpenAcc_SignDocsSmsTap": {0: 6.2, 1: 5, 2: 4.34, 3: 4, 4: 3.84},
                "28500_Instr_Bid_Success": {0: 19, 1: 12, 2: 9.6, 3: 8}
            },

            "opaymodd": {
                "signup_success": {
                    "77ads::dopemobi::7dope-opayy": {0: 3.7, 1: 3.3, 2: 3, 3: 2.85},
                    "77ads::dopemobi::7dope-opayy2": {0: 3.7, 1: 3.3, 2: 3, 3: 2.85},
                    "77ads::dopemobi::7dope-opayy3": {0: 3.7, 1: 3.3, 2: 3, 3: 2.85},
                    "77ads::dopemobi::7dope-opayy4": {0: 3.7, 1: 3.3, 2: 3, 3: 2.85},
                    "77ads::dopemobi::7dope-opayy5": {0: 3.7, 1: 3.3, 2: 3, 3: 2.85},
                    "77ads::dopemobi::7dope-opayy6": {0: 3.7, 1: 3.3, 2: 3, 3: 2.85},
                    "77ads::dopemobi::7dope-opayy7": {0: 3.7, 1: 3.3, 2: 3, 3: 2.85},
                    "*::*::*": {0: 3.7, 1: 3.44, 2: 3.3}  # fallback
                },

                "first_transaction": {
                    "adshustle::leanmobi::noplenmmp": {0: 7.14, 1: 6.25, 2: 5.67, 3: 5},
                    "*::*::*": {0: 16.6, 1: 11, 2: 7.14}  # fallback
                },

                "total_transaction": {0: 15, 1: 10, 2: 6}
                },

            "indigomoddteam2modd": {
                "af_purchase": {
                    "mobpine::*::*": {0: 12, 1: 10, 2: 9},
                    "77ads::*::*": {0: 12, 1: 10, 2: 9},
                    "appamplify::*::*": {0: 12, 1: 10, 2: 9},
                    "*::*::*": {0: 8, 1: 7.33, 2: 6.14}  # fallback
                }
            },

        "cloneindigomoddteam2modd": {
                "af_purchase": {0: 9, 1: 8.33, 2: 7.14}
            },

        "clone2indigomoddteam2modd": {
                "af_purchase": {0: 9, 1: 8.33, 2: 7.14}
            },

        "breakthroughkingdommodd": {
                "1_09": {0:10, 1:20, 4:16.67, 5:14.28, 6:12.5, 7:14.28},
                "2_19": {0:10, 1:25, 3:20, 5:16.6, 6:14.28, 7:12.5},
                "5_47": {0:10, 1:8.3, 2:7.14, 3:6.25, 4:5.88, 5:5.5, 6:5, 7:4.54},
                "21_89": {1:33, 2:25, 3:16.67, 4:12.5, 5:10, 6:9, 7:7.69}
            },

        "kriptoauto": {
                "lpfhv5": {0:9, 3:5}
            },

        "homiedevmodd": {
                "af_subscribe": {0:10, 1:5, 2:4}
            },

        "homieiosmodd": {
                "af_subscribe": {0:10, 1:7.5, 2:5}
            },

        "dimeiosmodd": {
                "onboardSuccess": {0:10, 1:7, 2:5, 3:4.34, 4:3.8}
            },

        "kfcmexicotmodd": {
                "first_purchase": {0:5, 3:5}
            },

        "tejimaandiauto": {
                "csqfum": {0:20, 1:16.6, 2:14.28, 3:12.5}
            },

        "teenpatiauto": {
                "0_36": {0:20},
                "1_08": {0:38},
                "3_6": {0:41, 1:29},
                "10_79": {1:41, 3:41}
                },

        "alphabetoftastemodd": {
            "purchase_start": {0:19, 1:11.25, 2:10}
        },

        "kafimodd": {
            "stock_order_matching": {0:41, 1:33, 2:25, 3:20}
        },

        "kafitradeiosmodd": {
            "stock_order_matching": {0:41, 1:33, 2:25, 3:20}
        },

        "mcdeliverymodd": {
            "af_purchase_delivery": {
                "mobs-mcd::*::*": {0:5, 1:4, 2:3.3},
                "*::*::*": {0:6.6, 1:5.5, 2:5}
            }
        },

        "clonemcdeliverymodd": {
            "af_purchase_to_be_delivered": {0:6.6, 1:5.5, 2:5}
        },

        "raisinggoblinmodd": {
            "First_Purchase": {0:6.67, 1:20}
        },

        "rummytimemodd": {
            "user_first_add_cash": {0:25, 1:16.67, 2:12.5}
        },

        "toponemarketauto": {
            "6uwnyv": {0:65, 1:40}
        },

        "toponemarketiosauto": {
            "f3a4ks": {0:65, 1:40}
        },

        "vpnpantheriosmodd": {
            "trial converted": {3:33, 4:20, 5:14.28, 6:12.5, 7:11.1},
            "af_trial_started": {0:14, 1:10, 2:7.5, 3:6.5}
        },

        "zeptodeliverymodd": {
            "first_order_delivered": {0:12, 1:9, 2:7.69, 3:6.6}
        },

        "dupointmodd": {
            "yh7wzr": {
                "adshustle::refrevenue::duphurmmp": {0:55},
                "*::*::*": {0:33, 1:22, 2:18, 3:16}
            }
        },

        "youset2modd": {
            "generate_proposal_auto": {0:33, 1:22, 2:18},
            "generate_proposal_home": {0:41, 1:33}
        },

        "yesmadammodd": {
            "af_complete_registration": {0:2, 1:1.78, 2:1.66},
            "af_purchase": {0:12.5, 1:10, 2:7.14}
        },

        "bigloanmodd": {
            "issueNewCPA": {1:90, 2:30, 3:20, 4:16, 5:14},
            "minconditionsapprove": {
                "bigldopvammp::*::*": {0:12.5, 1:7.14, 2:6.6, 3:5},
                "*::*::*": {0:12.5, 1:8.3, 2:7.14, 3:6.6}
            }
        },

        "otpbankappmetrica": {
            "screen__dc_success_courier": {1:70, 2:23, 3:14, 4:11, 5:10}
        },

        "byutmodd": {
            "purchase_iJoin": {0:20, 1:14.28, 2:12.5, 3:11.11, 4:10}
        },

        "comparemodd": {
            "mfoDealConfirmed": {0:33.33, 1:20, 2:16.66, 3:14.28, 4:12.25}
        },

        "melivemodd": {
            "af_revenue": {0:26, 1:20, 2:16}
        },

        "metlivemodd": {
            "af_revenue": {0:26, 1:20, 2:16}
        },

        "globusappmetrica": {
            "purchaseEvent": {0:45, 1:30}
        },

        "parimatchthmodd": {
            "Deposit Successful First": {0:25, 1:20, 2:16}
        },

        "myntmodd": {
            "af_deposit": {0:23, 1:20, 2:16.6, 3:14.28}
        },

        "spinnytauto": {
            "cqjxvf": {
                "adshustle::*::*": {0:33, 1:20, 2:15.38},
                "vestaapps::*::*": {0:33, 1:20, 2:15.38},
                "appsfollowing::*::*": {0:33, 1:20, 2:15.38},
                "appsatiate::*::*": {0:33, 1:20, 2:15.38},
                "*::*::*": {0:45, 1:30, 2:25}
            }
        },

        "shienindiamodd": {
            "af_purchase": {0:30, 1:20, 2:14.28, 3:12.5}
        },

        "digitalbankmodd": {
            "upgrade2SA": {0:45, 1:16.6, 2:11.1}
        },

        "woolsocksmodd": {
            "3ts38m": {0:15, 1:11, 2:10, 3:9}
        },

        "cimbthaimodd": {
            "NTB_Deposit_Open_Speed-d-plus_Success_Viewed": {0:45, 1:30, 2:25},
            "NTB_Deposit_Open_Chill-d_Success_Viewed": {0:47, 1:32, 2:26},
            "NTB_Mutual_Fund_Open_Deposit_And_MF_Success": {0:70, 1:50, 2:33}
        },

        "robotzaimerrmodd": {
            "signContractFirst": {0:45, 1:30, 2:25}
        },

        "stockitymodd": {
            "payment.deposit_first_new": {0:45, 1:25, 2:20}
        },

        "heliummobilemodd": {
            "app_purchase_free": {
                "*::*::*": {0:30, 1:20, 2:16},
                "*::offer_id_isdecimal::*": {0:5, 1:3}
            },
            "purchase": {0:45, 1:30, 2:25}
        },

        "abhibusauto": {
            "cukuuk": {
                "*::offer_id_isdecimal::*": {0:5, 1:3},
                "*::*::*": {0:14, 1:8.33}
            }
        },

        "duittmodd": {
            "Successful_loan": {0:90, 1:30, 2:20, 3:16}
        },

        "r888casinomodd": {
            "MB_First_Deposit": {0:70, 1:50}
        },

        "istanbulairportauto": {
            "duf9j9": {0:4.4, 1:3.8, 2:3.5},
            "pykeub": {0:2.2, 1:2, 2:1.8}
        },

        "sliceauto": {
            "ksdh0l": {0:80, 1:33, 2:25},
            "ghmq8p": {0:80, 1:25, 2:20, 3:16.6}
        },

        "instamoneyquickmodd": {
            "AF_RF_Paid": {0:45, 1:20, 2:14, 3:11, 4:10},
            "AF_RF_LOAN_DISBURSED": {1:45, 2:30, 3:24}
        },

        "coinmenaauto": {
            "aj5y08": {0:41, 1:19, 2:14, 3:11, 4:9}
        },

        "smilesauto": {
            "a6ou21": {0:45, 1:20, 2:14, 3:11}
        },

        "netshoesmodd": {
            "af_purchase": {
                "appamplify::dopemobi::dope-netshoes-251030": {0:100},
                "*::*::*": {0:25, 1:17, 2:14}
            }
        },

        "bingoplustmodd": {
            "BINGOPLUS_EVENT_REGIST": {0:3, 1:2.36, 2:2.09, 3:1.91},
            "bingoplus_first_deposit": {0:90, 1:45, 2:30}
        },

        "myshiftappmetricat": {
            "ShiftCatalogShiftDetails_shift_booked": {0:45, 1:25, 2:20}
        },

        "shorttvtmodd": {
            "revenue_3499": {0:45},
            "revenue_4999": {0:30},
            "revenue_9999": {0:16},
            "revenue_349": {1:90},
            "revenue_499": {2:90},
            "revenue_999": {3:90}
        },

        "etomomodd": {
            "loan_requested": {
                "*::offer_id_isdecimal::*": {0:7},
                "*::*::*": {0:25, 1:14.28, 2:11}
            }
        },

        "cryptocomtmodd": {
            "mktg:kyc_approved_push_sent": {0:4, 1:3}
        },

        "megogot2modd": {
            "af_purchase": {0:6.66, 1:5.26, 2:4.76, 3:4.54}
        },

        "wiomodd": {
            "view_screen_onboarding_app_submitted": {0:80}
        },

        "paisayaarauto": {
            "jbjcze": {1:30, 2:20, 3:16}
        },

        "gsmtmodd": {
            "sign_up": {0:3.33, 1:2.85, 2:2.63, 3:2.5},
            "order_completed_1st_time": {0:10, 1:8, 2:7, 3:6}
        },

        "bollingerauto": {
            "purchase": {0:18, 1:9}
        },

        "joybuymodd": {
            "PURCHASE": {0:25, 1:20, 2:16.6}
        },

        "soulchilltmodd": {
            "revenue_049": {1:35, 3:25, 5:15},
            "revenue_099": {2:40, 5:25, 6:17, 7:9},
            "revenue_499": {0:40, 3:25, 4:16},
            "revenue_999": {1:40}
        },

        "kotak811mbtmodd": {
            "AccountOTP_OTP_Acq": {0:30}
        },

        "mylingueautoios": {
            "y3ahlf": {
                "*::offer_id_isdecimal::*": {0:2, 1:1.81, 2:1.63, 3:1.49},
                "*::*::*": {0:3.33, 1:2.77, 2:2.43, 3:2.22}
            }
        },

        "omniheroesmodd": {
            "revenue_099": {4:49},
            "revenue_499": {0:25, 4:16},
            "revenue_1499": {0:24, 1:16, 2:12, 3:8, 5:7, 6:6.25}
        },

        "nomadesimauto": {
            "5f3kzv": {0:16, 1:11.11, 2:9.09, 3:8.33}
        },

        "nouslibauto": {
            "chju3f": {0:2, 1:1.78, 2:1.6},
            "purchase": {0:21, 1:16}
        },

        "nouslibt2autoios": {
            "chju3f": {0:2, 1:1.78, 2:1.6},
            "purchase": {0:21, 1:16}
        },

        "carjammodd": {
            "revenue199": {1:15, 3:9, 4:6.6},
            "revenue799": {0:9, 2:6.6}
        },

        "fabmobilemodd": {
            "ntb_casa_account_created": {1:45, 2:30, 3:23},
            "ntb_cc_card_created": {0:45, 1:30, 2:23, 3:19}
        },

        "bbvamodd": {
            "portabilidad_nomina-app_approved": {
                "adshustle::myfunadstrack::bbvamyfmmp": {1:80},
                "*::*::*": {0:40, 1:26, 2:20, 3:18}
            },
            "afiliacion_basica-app_online_purchases": {
                "adshustle::myfunadstrack::bbvamyfmmp": {0:95, 1:48},
                "*::*::*": {0:48, 1:19, 2:14}
            }
        },

        "babytrackermodd": {
            "af_start_trial": {0:30, 1:18, 2:16},
            "af_subscribe": {0:90, 1:45},
            "af_purchase": {0:31, 1:19, 2:15, 3:12}
        },

        "glowbabytrackeriosmodd": {
            "af_start_trial": {0:30, 1:18, 2:16},
            "af_subscribe": {0:90, 1:45},
            "af_purchase": {0:31, 1:19, 2:15, 3:12}
        },

        "vogaclosetiosauto": {
            "yewk8s": {0:15, 1:9, 2:7}
        },

        "mibptmodd": {
            "FB_Mobile_complete registration": {0:1.85, 1:1.6}
        },

        "filteraiiosauto": {
            "mjq7jz": {0:30, 1:19, 2:16}
        },

        "utimamarketsmodd": {
            "P_FTD": {1:30, 2:19, 3:16}
        },

        "osagomodd": {
            "s2s-cpa-conversion": {1:24, 2:14, 3:11, 4:9}
        },

        "neobetiosmodd": {
            "af_first_purchase": {0:90, 1:45}
        },

        "qustodioparentalauto": {
            "85anak": {0:22.5, 1:15, 2:12.85},
            "g2gfaz": {0:90, 1:45, 2:30}
        },

        "mexdinmodd": {
            "first_loan_success": {0:90, 1:30, 2:25}
        },

        "underarmourauto": {
            "5uo13w": {
                "*::*::undapcmmp": {0:5},
                "*::*::*": {0:15, 1:9, 2:6.42, 3:5.62}
            }
        },

        "nuiauto": {
            "1rck55": {0:6, 1:4.5, 2:3.6, 3:3.21},
            "vcoavi": {0:45, 1:22.5, 2:18, 3:15}
        },

        "credmaxmodd": {
            "approvals_server": {0:45, 1:30, 2:22.5, 3:18},
            "tutorial_complete_server": {0:90, 1:45, 2:30, 3:22.5}
        },

        "cryptocomtmodd": {
            "mktg:buy_crypto": {0:25, 1:14, 2:11, 3:10}
        },

        "bancaauto": {
            "xnfrxy": {0:30, 1:20, 2:14}
        },

        "fiverrt2modd": {
            "FTB_BUCKET": {0:30, 1:18, 2:15}
        },

        "fiverriosmodd": {
            "FTB": {0:30, 1:18, 2:15}
        },

        "williamhillsportiosmodd": {
            "FTD": {
                "*::*::apps-whsports.ios": {0:45},
                "*::*::whuk2adgmmp": {0:45},
                "*::*::willadghubmmp": {0:50},
                "*::*::whsptadgmmp": {0:60},
                "*::*::ahwilkspmmp": {0:8},
                "*::*::wiladummp": {0:10},
                "*::*::wammobmmp": {0:22},
                "*::*::*": {0:30, 1:22.5, 2:18}
            }
        },

        "vegasiosmodd": {
            "registration": {
                "*::*::mpj-wcios": {0:6},
                "*::*::adhub-whcasinoiios-26a017260": {0:6},
                "*::*::williamhill-mpjads-jan": {0:4.5},
                "*::*::*": {0:24, 1:12, 2:10}
            },
            "FTD": {
                "*::*::mpj-wcios": {0:13},
                "*::*::adhub-whcasinoiios-26a017260": {0:13},
                "*::*::williamhill-mpjads-jan": {0:8.5},
                "*::*::wh2casdgmmp": {0:67},
                "*::*::*": {0:30, 1:20, 2:16}
            }
        },

        "cleanervpniosmodd": {
            "apphud_trial_started": {0:22.5, 1:15, 2:12.85, 3:11.25}
        },

        "adblockeriosmodd": {
            "apphud_trial_started": {0:22.5, 1:15, 2:12.85, 3:11.25}
        },

        "jyotiaiiosmodd": {
            "apphud_trial_started": {0:22.5, 1:15, 2:12.85, 3:11.25}
        },

        "moneygrammiosmodd": {
            "first_transaction": {0:22.5, 1:15, 2:12.85, 3:11.25}
        },

        "mixvpniosmodd": {
            "apphud_trial_started": {0:22.5, 1:15, 2:12.85, 3:11.25}
        },

        "plantexpertaiiosmodd": {
            "apphud_trial_started": {0:22.5, 1:15, 2:12.85, 3:11.25}
        },

        "888pokeriosmodd": {
            "MB_First_Deposit": {0:90, 1:45, 2:30}
        },

        "tataneuauto": {
            "CC_CARD_SELECTION": {0:6, 1:5, 2:4.5},
            "plm_disbursement": {0:30, 1:18, 2:15, 3:12.85}
        },

        "betfredsportsiosmodd": {
            "deposit": {0:90, 1:30, 2:22.5, 3:18}
        },

        "ajioiosmodd": {
            "first_purchase": {0:45, 1:30, 2:22.5, 3:18}
        },

        "cashmaxmodd": {
            "Successful_loan": {0:90, 1:22.5, 2:15, 3:12.85}
        },

        "idntimesmodd": {
            "Subscribe_success": {0:45, 1:18, 2:12.85, 3:11.25}
        },

        "teldaauto": {
            "ntd8cj": {0:11.25, 1:7.5, 2:6, 3:5.29}
        },

        "tenthousandmodd": {
            "revenue_099": {0:90, 1:45, 3:30, 4:22.5, 5:18, 6:15, 7:12.85},
            "revenue_499": {0:48, 2:32}
        },

        "vtb24tappmetrica": {
            "screenTap_notClient_liteData_litePasscode": {0:2.5, 1:2}
        },

        "cleanervpniosmodd": {
            "apphud_trial_started": {0:22.5, 1:15, 2:12.85, 3:11.25}
        },

        "mbbankmodd": {
            "AF_OB_SUCCESS": {
                "*::*::mbb2iwammp": {0:30, 1:20, 2:16.6, 3:14.28},
                "*::*::*": {0:12.85, 1:9, 2:7.5}
            }
        },

        "mbbankautoios": {
            "AF_OB_SUCCESS": {
                "*::*::mbbiwammp": {0:30, 1:20, 2:16.6, 3:14.28},
                "*::*::*": {0:12.85, 1:9, 2:7.5}
            }
        },

        "tawkeeltmodd": {
            "payment_completed": {0:30, 1:18, 2:12.85, 3:11.25}
        },

        "webullmodd": {
            "first_deposit_success_F": {1:23, 2:13.5, 3:11.87}
        },

        "lottermxiosmodd": {
            "FTD": {
                "mobpine::*::*": {0:12},
                "77ads::*::*": {0:12},
                "appamplify::*::*": {0:12},
                "*::*::17425": {0:13},
                "*::*::*": {0:80, 1:33}
            }
        },

        "thelotterusiosmodd": {
            "FTD": {0:80, 1:33}
        },

        "blibliiosmodd": {
            "new_customer_purchase": {0:24, 1:13.71, 2:10.66, 3:9.6}
        },

        "mtcmusiciosmodd": {
            "af_subscribe": {0:45, 1:24, 2:19}
        },

        "mtcmusicmodd": {
            "af_subscribe": {0:45, 1:24, 2:19}
        },

        "bitoasistauto": {
            "deposit": {0:45, 1:24, 2:19}
        },

        "myacuvuemodd": {
            "Registration_Success": {0:2.22, 1:2.08, 2:1.92},
            "fitting_events": {0:5.8, 1:5.26, 2:4.76}
        },

        "myfoodappmetrica": {
            "2990_rev": {0:30, 1:19, 2:16},
            "2590_rev": {0:31, 1:18, 2:15}
        },

        "myacuvueiosmodd": {
            "Registration_Success": {
                "*::*::myiosappmmp": {0:3.3, 1:2.77, 2:2.38},
                "*::*::*": {0:2.22, 1:2.08, 2:1.92}
            },
            "fitting_events": {
                "*::*::myiosappmmp": {0:12.5, 1:10, 2:7.14},
                "*::*::*": {0:5.8, 1:5.26, 2:4.76}
            }
        },

        "makebykbankiosmodd": {
            "ON2kSucceed": {0:24, 1:11, 2:8, 3:7}
        },

        "velvetvpniosmodd": {
            "apphud_trial_started": {0:22.5, 1:15, 2:12.85, 3:11.25}
        },

        "bluerewardsmodd": {
            "sign_up": {0:8, 1:6, 2:5, 3:4.75, 4:4.31}
        },

        "paymeiosauto": {
            "zgxxz1": {0:18, 1:11.25, 2:8}
        },

        "paymeauto": {
            "zgxxz1": {0:18, 1:11.25, 2:8}
        },

        "seevpniosmodd": {
            "apphud_trial_started": {0:22.5, 1:15, 2:12.85, 3:11.25}
        },

        "ajiomodd": {
            "luxe_purchase": {0:19, 1:11, 2:9},
            "ajio_purchase": {0:80, 1:40}
        },

        "octatrademodd": {
            "af_realtime_activation": {0:90, 1:45}
        },

        "action247iosmodd": {
            "af_FTD": {0:20}
        },

        "sensorvpniosmodd": {
            "apphud_trial_started": {0:22.5, 1:15, 2:12.85, 3:11.25}
        },

        "weltradeauto": {
            "kbwb07": {0:45, 1:18},
            "evpfo1": {1:89}
        },

        "vanaauto": {
            "15serm": {0:89, 1:30, 2:18, 3:15}
        },

        "sahimodd": {
            "5fno_completed": {0:89, 1:22.5, 2:18.5}
        },

        "moneymaniosmodd": {
            "NEW_CREDIT_ACTIVE_DB": {0:89, 1:30, 2:18, 3:15}
        },

        "moneyviewmodd": {
            "submit_success": {
                "mobpine::*::*": {0:45, 1:25, 2:19},
                "77ads::*::*": {0:45, 1:25, 2:19},
                "appamplify::*::*": {0:45, 1:25, 2:19},
                "*::*::*": {0:30, 1:19, 2:16, 3:14}
            },
            "upi_first_payment": {0:8.3, 1:5.55, 2:4.3, 3:4}
        },

        "viuhkmodd": {
            "subscription_payment_success": {0:30, 1:24, 2:19}
        },

        "tinkofft2modd": {
            "credit_approve_offline": {0:45, 1:30, 2:22.5, 3:18},
            "debit_utilization_offline": {0:45, 1:22.5, 2:18, 3:15, 4:12.85}
        },

        "healthifymetmodd": {
            "sp_plan_purchase": {0:31.66, 1:19, 2:15.8, 3:13.57}
        },

        "mistplayearnmoneymodd": {
            "iap_spend_all_v2": {0:90, 1:45}
        },

        "yandexrealestateiosmodd": {
            "first_call_posle-paid_s2s": {0:75, 1:41}
        },

        "popaimodd": {
            "onPurchasesUpdated": {0:90, 1:45, 2:30}
        },

        "dominosturkeyauto": {
            "yfub50": {
                "*::*::domdoummp": {0:2.85, 1:2.5, 2:2.27},
                "*::*::dom2doummp": {0:2.85, 1:2.5, 2:2.27},
                "*::*::*": {0:3.3, 1:2.85, 2:2.6}
            }
        },

        "rootcarinsurancemodd": {
            "Profile": {0:9, 1:7, 2:6}
        },

        "mcluckcasinoiosmodd": {
            "first_purchase": {0:75, 1:45}
        },

        "eternzmodd": {
            "First Purchase": {0:14, 1:10, 2:8, 3:6}
        },

        "dominoesgoldiosmodd": {
            "firstCashNPU": {0:45, 1:23, 2:18}
        },

        "unodigitalbankiosmodd": {
            "loan_disbursed": {0:90, 1:30, 2:23}
        },

        "loansonlinemodd": {
            "newloancount": {0:90, 1:45, 2:30}
        },

        "webzaimiosmodd": {
            "newloancount": {0:90, 1:45, 2:30}
        },

        "litresiosmodd": {
            "af_purchase_success_ppd": {0:22.5, 1:18, 2:15.5, 3:12.85}
        },

        "shahidmodd": {
            "evergent_server_subscription_success": {0:24, 1:16, 2:14, 3:12}
        },

        "paymayamodd": {
            "EKYC_SUCCESS": {0:16, 1:8.1, 2: 6.9},
            "WALLET_DEBIT_ACTIVE": {0:47, 1:16.6, 2:10.6, 3:  8.1}
        },

        "bajajfinauto": {
            "Lead_PROL_DR": {0:49, 1:24, 2:19},
            "Lead_PROL_CA": {0:48, 1:23, 2:18}
        },

        "maxfashionindiaauto": {
            "PURCHASE": {0:24, 1:8.3, 2:7.5}
        },

        "afriexaiosauto": {
            "opawt9": {0:45, 1:22, 2:15, 3:12}
        },

        "pointsbetsportsbookmodd": {
            "Deposit Placed First Time": {0:45, 1:22.5, 2:18}
        },

        "burgerkingbrasilt2modd": {
            "af_purchase": {0:9, 1:7.14}
        },

        "sugarworldiosmodd": {
            "sale": {0:25, 1:16.6}
        },

        "neoniosmodd": {
            "crd_pre_approved_stts": {1:29, 2:18, 3:15, 4:14.3}
        },

        "starzplayiosmodd": {
            "af_subscribe": {0:45, 1:32}
        },

        "ballmodd": {
            "ChallengeCompleted_1": {0:18, 1:11.25, 2:9}
        },

        "defactotauto": {
            "icmk9u": {0:24, 1:14, 2:12}
        },

        "defactoiosauto": {
            "icmk9u": {0:24, 1:14, 2:12}
        },

        "pulszcasinomodd": {
            "af_purchase_total_10_00": {0:95, 1:48}
        },

        "fanaticscasinoiosmodd": {
            "af_complete_registration": {0:5, 1:3.7, 2:3.2},
            "deposit_submitted": {0:24, 1:13.5, 2:12},
            "casino_game_first_launch": {0:75, 1:46}
        },

        "eaptekatmodd": {
            "af_first_order": {0:15, 1:9, 2:6.9, 3:6, 4:5.62}
        },

        "playuzuiosmodd": {
            "userFirstTimeDeposit": {0:45, 1:23}
        },

        "sofyclubauto": {
            "e7ikty": {0:2, 1:1.6, 2:1.5, 3:1.49},
            "2hekaz": {0:4.3, 1:3.4, 2:3.03, 3:2.7, 4:2.5, 5:2.32}
        },

        "viusaiosmodd": {
            "subscription_payment_success": {0:24, 1:15, 2:12.8, 3:11.8}
        },

        "wirexiosauto": {
            "s2s_first_transaction": {0:40, 1:30}
        },

        "bet22modd": {
            "first_deposit": {0:95, 1:30, 2:22.5, 3:18}
        },

        "beetlessolitairemodd": {
            "revenue_1": {1:40},
            "revenue_6": {0:11, 1:7, 2:5, 3:4, 4:12.5},
            "grt_win_858": {0:30}
        },

        "onepuchmanmodd": {
            "revenue488": {0:18, 1:14},
            "revenue103": {2:18, 3:14}
        },

        "lottolandauto": {
            "20y4ke": {0:40, 1:30, 2:23}
        },

        "playmillionmodd": {
            "FTD": {0:75, 1:30}
        },

        "foodiesizzleiosmodd": {
            "revenue_2": {1:80},
            "revenue_5": {0:45},
            "revenue_8": {3:81, 6:41},
            "revenue_10": {0:44},
            "revenue_11": {2:82},
            "revenue_16": {2:79, 3:43},
            "revenue_25": {1:78, 7:46},
            "revenue_30": {5:75}
        },

        "fibeiosmodd": {
            "total_approved": {0:23, 1:11.8, 2:9.6},
            "disbursement": {0:95, 1:47, 2:31.6, 3:23}
        },

            "caroutmodd": {
            "in_app_purchase": {0:6}
        },

        "nelopayiosauto": {
            "INFLECTION_UNDERWRITING": {0:22, 1:13, 2:10.5, 3:9.4}
        },

        "btcturkproauto": {
            "754uyc": {0:6.6, 1:5.55, 2:5, 3:4.5},
            "j19w5z": {0:24, 1:14.2, 2:11, 3:9.7}
        },

        "rakutentmodd": {
            "af_purchase": {0:10}
        },

        "moneycatiosmodd": {
            "NEW_LOAN": {1:45, 2:22.5, 3:18.3}
        },

        "whitebitiosmodd": {
            "KYC_VERIFIED": {0:9.2, 1:5.41, 2:4.3, 3:3.8},
            "FIRST_DEPOSIT": {0:19, 1:12.5, 2:8.9},
            "FIRST_TRADE": {0:95, 1:47.5, 2:31.6}
        },

        "betparxiosmodd": {
            "af_first_deposit": {0:95, 1:47}
        },

        "yangoplayiosmodd": {
            "auth.succeed": {0:10, 1:8.33, 2:6.67},
            "c0_no_cancel_3d": {0:25, 1:16.6, 2:13.3},
            "unified_subscription.purchase.completed": {0:40, 1:25, 2:16.6}
        },

        "kudusaudiarabiaauto": {
            "fen1r7": {0:5.7, 1:5.42, 2:4.84}
        },

        "myasterauto": {
            "szqveh": {0:80, 1:30}
        },

        "kubizmodd": {
            "issueNew": {1:90, 2:47, 3:31},
            "addNewBankAccountResult": {0: 31, 1: 19, 2:14.2, 3:11.8}
        },

        "dabbleiosmodd": {
            "first_deposit_completed": {0:78, 1:30}
        },

        "yourloaniosmodd": {
            "loan_accepted": {0:95, 1:31, 2:16.5}
        },

        "yourloanmodd": {
            "loan_accepted": {0:95, 1:31, 2:16.5}
        },

        "rummytwistmodd": {
            "revenue_02":  {3 : 80, 4: 39, 5: 32},
            "revenue_05": {0: 40, 1: 30, 4: 23},
            "revenue_1": {0: 83, 2: 42, 3: 31}
        },

        "lulumoneymodd": {
            "First_Transaction": {0: 16, 1: 12, 2: 11, 3: 10}
            },

        "galaxychatappmetrica": {
            "new_user_reg": {0: 2.22,1:1.88, 2: 1.81}
        },

        "todocreditmxmodd": {
            "af_first_apply_loan": {0: 19, 1: 11.5, 2: 8, 3: 6.2}
            },

        "fictionmemodd": {
            "read_10_chapters_7days": {0: 0, 1: 20, 2: 12, 3: 10}
        },

        "crecidineromxiosmodd": {
            "af_first_apply_loan": {0: 19, 1: 11.5, 2: 8, 3: 6.2}
            },

        "timonemobilemodd": {
            "KYC Completed": {0: 80, 1: 30, 3: 19}
            },

        "onmobileauto": {
            "jr95xb": {
                # "mobpine::*::*": {0:1.8, 1:1.53, 2:1.42, 3:1.33, 4:1.25},
                # "77ads::*::*": {0:1.8, 1:1.53, 2:1.42, 3:1.33, 4:1.25},
                # "appamplify::*::*": {0:1.8, 1:1.53, 2:1.42, 3:1.33, 4:1.25},
                "*::*::*": {0:1.13, 1:1.02}
            }
        },

        "onmobilautoios": {
            "jr95xb": {
                "mobpine::*::*": {0:1.53, 1:1.25, 3:1.11, 4:1.05},
                "77ads::*::*": {0:1.53, 1:1.25, 3:1.11, 4:1.05},
                "appamplify::*::*": {0:1.53, 1:1.25, 3:1.11, 4:1.05},
                "*::*::*": {0:1.13, 1:1.02}
            }
        },

        "deltamodd": {
            "kyc_success": {0: 19,1:9.6, 2:7.5 , 3: 6.5},
            "FTD": {1:23.75, 2: 16.6},
            "First Time Trade Success": {1: 33, 2: 19}
        },

        "timonemobilemodd": {
            "KYC Completed": {0: 19, 1: 11.5, 2: 8, 3: 6.2}
            },

        "timoniosmodd": {
            "KYC Completed": {0: 19, 1: 11.5, 2: 8, 3: 6.2}
            },

        "fortaprestiosmodd": {
            'AF_XHED_SJFQ_FKCG': {0: 0, 1: 50, 2: 33}
            },

        "jazzcashiosmodd": {
            "L1_registration_successful": {            
                
                "77ads::azzuremedia::azz-jazz.apr2": {0: 4.18, 1: 2.85, 2: 2.65, 3: 2.55},
                "*::*::*": {0: 2.18, 1: 1.85, 2: 1.65, 3: 1.55}
                },
            },

        "grandparimodd": {
            "first_deposit": {0: 30, 1: 20}
            },

        "picpaymodd": {
            "picpaycard_sem_lg_venda_confirmada": {0: 47,1: 31.6}
            },

        "tangledropemodd": {
            "af_purchase_199": {0: 47, 1: 24},
            "af_purchase_799": {1: 31, 2: 19, 3: 16.6},
            "af_purchase_1499": {1: 90, 2: 31, 3: 24},
        },

        "tangledropeiosmodd": {
            "af_purchase_199": {0: 47, 1: 24},
            "af_purchase_799": {1: 31, 2: 19, 3: 16.6},
            "af_purchase_1499": {1: 90, 2: 31, 3: 24},
        },
        "titanfincorpmodd": {
            "lms_loan_application_disburse": {0: 90, 1: 33, 2: 25}
        },
        "coolflymodd": {
                "Sales": {0: 25, 1: 16, 2: 12}
            },
        "fanaticsshopiosmodd": {
            "purchase": {0: 31, 1: 20, 2: 15.83}
        },
        "jarmoneyiosmodd": {
            "AUTOPAY_SETUP_COMPLETE": {0:19, 1:9.4, 2: 8.3, 3: 6.6}
        },
        "dbbetmodd": {
            "first_deposit": {0: 31, 1: 20, 2: 15.83}
        },
        "justfoodappmetrica": {
            "kf_payment_success": {0: 90, 1: 45}
        },

        "jazzcashmodd": {
            "L1_registration_successful": {0: 2.18, 1: 1.85, 2: 1.65, 3: 1.52}
        },
        "happybingoiosmodd": {
            "af_ftd": {0: 33, 1: 25, 2: 20}
        },
        "stablemoneynewmodd": {
           "sm_first_payment_success" : {0:45, 1:27}
            },

        "fxproiosdirectmodd": {
            "depositfirst_suc": {0: 31, 1: 19, 2: 14.28, 3: 11.87},
            "40_spread": {3: 90, 5: 47},
            "verification_suc": {0: 19, 1: 9.8, 2:7.5 , 3: 6.5},
            },

        "aforemodd": {
            "asg_11": {0: 18, 1: 16, 2: 14},
            "atr_08_01": {1: 45, 2: 32, 3: 26}
            },


    }

    return STATS.get(campaign_name, {})

def camp_wise_stats(campaign_name, event_name, channel, network, offer_id,Pay_out=0.0, event_day=0):

    if campaign_name == "jazzcashmodd" and event_name == "L1_registration_successful":

        if channel in ["77ads", "appamplify"] and network =='doromobile':
            return {0:2.11, 1:2, 2:1.72, 3:1.58 }

        elif channel in ["mobpine", "77ads", "appamplify"] and 0.05<=float(Pay_out)<=0.10 :
            return {0:2.22, 1:2, 2: 1.81, 3: 1.72, 4: 1.66}

    
    elif campaign_name == "onmobilautoios" and event_name == "jr95xb_login":

        if not offer_id.isdecimal():
            return {1:100}
        else:
            return {1:100}
    
    elif campaign_name == "garantiauto" and event_name == "otpgdr":
        return {0:30, 1:16.66, 2:12.5}
    
    elif campaign_name == "garantiauto" and event_name == "gr546v":
        return {0:30, 1:16.66, 2:12.5}

    elif campaign_name == "garantiauto" and event_name == "pfj58r":
        return {0:14, 1:9}
    
    elif campaign_name == "garantiauto" and event_name == "rmq154" and offer_id:
        if offer_id.isdecimal():
            return {0:2.5, 1:2.5}
        else:
            return  {0:12.5, 1:10} 

    elif campaign_name == "kfcsaudiiauto" and event_name == "cq4kxg":
        if offer_id.isdecimal():
            return {0:3.06, 1:2.45}
        return {0:4.76, 1:3.06, 2:2.45}

    elif campaign_name == "kfcsaautoios" and event_name == "cq4kxg":
        if offer_id.isdecimal():
            return {0:3.06, 1:2.45}
        return {0:4.76, 1:3.06, 2:2.45}

    elif campaign_name == "kfcgulfauto" and event_name == "ak1z7d":
        if offer_id.isdecimal():
            return {0:3.06, 1:2.45}
        
        return {0:4.76, 1:3.06, 2:2.45}

    elif campaign_name == "kfcaeautoios" and event_name == "ak1z7d":
        if offer_id.isdecimal():
            return {0:3.06, 1:2.45}
        
        return {0:4.76, 1:3.06, 2:2.45}
    
    elif campaign_name == "kfcmaauto" and event_name == "txxq1a":
        if offer_id.isdecimal():
            return {0:3.06, 1:2.45}
        
        return {0:6.6, 1:5.5, 2:4.76}
    
    elif campaign_name == "kfcmoroccoiosauto" and event_name == "txxq1a":
        if offer_id.isdecimal():
            return {0:3.06, 1:2.45}
        
        return {0:6.6, 1:5.5, 2:4.76}
    
    elif campaign_name == "kfckwautoios" and event_name == "lm9dao":
        if offer_id.isdecimal():
            return {0:3.06, 1:2.45}
        
        return {0:6.6, 1:5.5, 2:4.76}
    
    elif campaign_name == "kfckuwaitt2auto" and event_name == "lm9dao":
        if offer_id.isdecimal():
            return {0:3.06, 1:2.45}
        
        return {0:6.6, 1:5.5, 2:4.76}
    
    elif campaign_name == "kfcqatart2auto" and event_name == "9gtn52":
        if offer_id.isdecimal():
            return {0:3.06, 1:2.45}
        
        return {0:6.6, 1:5.5, 2:4.76}
    
    elif campaign_name == "kfcqatrautoios" and event_name == "9gtn52":
        if offer_id.isdecimal():
            return {0:3.06, 1:2.45}
        
        return {0:6.6, 1:5.5, 2:4.76}
    
    elif campaign_name == "pizzahutuaet2auto" and event_name == "e8nvvu":
        if offer_id.isdecimal():
            return {0:3.06, 1:2.45}
        
        return {0:6.6, 1:5.5, 2:4.76}
    
    elif campaign_name == "pizzahutuaeios" and event_name == "e8nvvu":
        if offer_id.isdecimal():
            return {0:3.06, 1:2.45}
        
        return {0:6.6, 1:5.5, 2:4.76}

    elif campaign_name == "albertbudgetauto" and event_name == 'finished_signup_flow_and_bank':
        if offer_id.isdecimal():
            return {0:14, 1:12, 2:9}

        return {0:30, 1:24, 2:19}

     # need to update

    elif campaign_name == "wetterandroidauto" and event_name == "u6z21k" and offer_id:
        if offer_id.isdecimal():
            return {0:6, 1:4.2, 2:3}

        return {0:14, 1:9.5, 2:8}
    
    elif campaign_name == "btcturktauto" and event_name == "496w0o":
        if offer_id.isdecimal():
            return {0:2.5}
        
        return {1:14, 2:10}

    elif campaign_name == "shionauto" and event_name == "10000_revenue":
        from datetime import datetime
        today = datetime.now().weekday()
        if today in [1, 5]:
            return {0:37}    
    

    elif campaign_name == "darknessmodd" and event_name == "revenue_1":
        return {0 : 12, 1: 9}

    elif campaign_name == "darknessmodd" and event_name == "revenue_5":

        if random.randint(1,100)<=5 and event_day == 1:
            return {1: 17}
        return {1:50}

    elif campaign_name == "tiletripmodd" and event_name == "revenue_6":
        return {0 : 20}

    elif campaign_name == "tiletripmodd" and event_name == "revenue_8":
        return {3: 40, 5:23}

    elif campaign_name == "tiletripmodd" and event_name == "revenue_13":
        return {1: 41, 4:22}

    elif campaign_name == "tiletripmodd" and event_name == "revenue_16":
        return {2:42, 5: 21}
    
    elif campaign_name == "tiletripmodd" and event_name == "grt_90d_levelpass_1000_v162":
        from datetime import datetime
        today = datetime.now().weekday()
        if today in [2,4]:
            return {0:40}

    elif campaign_name == "techcombankmodd" and event_name == "OnO_Success":
        if offer_id.isdecimal():
            return {0:5}
        
        return {0:19, 1: 11, 2:9, 3: 7.1}
    
    elif campaign_name == "tokiiosmodd" and event_name == "af_complete_registration":  

        if channel in  ["mobpine", "77ads", "appamplify"]:
            return {0:120}
        
        return {0:1.7 , 1:1.58, 2:1.53, 3: 1.48 }

    elif campaign_name == "tokiiosmodd" and event_name == "user_subscription_validated":  
        if channel in  ["mobpine", "77ads", "appamplify"]:
            from datetime import datetime
            today = datetime.now().weekday()
            if today in [2, 4, 6]:
                return {0:240} 
        
        return {0:23, 1: 12, 2:10.5, 3:9.5}

    
    elif campaign_name == "techcombankiosmodd" and event_name == "OnO_account_Success":
        if offer_id.isdecimal():
            return {0:5}
        
        return {0:19, 1: 11, 2:9, 3: 7.1}

    elif campaign_name == "b86betmodd" and event_name == "first_dep":

        return {0:30, 1: 18.5, 2:15}

    elif campaign_name == "tangledropemodd" and event_name == "af_purchase_199":
        return  {0: 31, 1: 19}

    elif campaign_name == "tangledropeiosmodd" and event_name == "af_purchase_199":
        return  {0: 31, 1: 19}
        
    
    campaign_stats = get_stats(campaign_name)

    if campaign_stats:
        event_data = campaign_stats.get(event_name)

        if all(isinstance(v, (int, float)) for v in event_data.values()):
            return event_data

        keys_to_try = [
            f"{channel}::{network}::{offer_id}",
            f"{channel}::{network}::*",
            f"{channel}::*::{offer_id}",
            f"*::{network}::{offer_id}",
            f"{channel}::*::*",
            f"*::*::{offer_id}",
            f"*::{network}::*",
            "*::*::*"
        ]

        for key in keys_to_try:

            if key in event_data:
                return event_data[key]

    else:
        print ("*"*50)
        print (campaign_name, event_name)
        print ("*"*50)
    
class checkEligibility(APIView):
    def get(self, request):
        campaign_name = request.GET.get('campaign_name')
        event_name = request.GET.get("event_name")
        offer_serial = request.GET.get("offer_serial")
        event_day = request.GET.get("event_day")
        revenue = request.GET.get("revenue", 0)
        track_only = request.GET.get("track_only", False)
        required_timezone = request.GET.get("required_timezone")
        Pay_out = request.GET.get("Pay_out",0.0)    

        if not all([campaign_name, event_name, offer_serial, event_day]):
            return Response({"status": 400,"message": "Missing required parameters","data": {}})

        try:
            event_day = int(event_day)
        except ValueError:
            return Response({"status": 400,"message": "Invalid event_day. It must be an integer.","data": {}})
        
        if not campaign_name in ["bigloanmodd"] and event_day>7:
            return Response({"status": 400, "message": "Max day allowed is 7", "data": {}})

        try:
            install_details = InstallData.objects.get(serial=offer_serial)
        except InstallData.DoesNotExist:
            return Response({"status": 404,"message": "Install record not found for given serial","data": {}})

        channel = install_details.channel
        network = install_details.network
        offer_id = install_details.offer_id
        install_count = install_details.installs
        offer_serial = install_details.serial

        if install_details.campaign_name != campaign_name:
            return Response({"status": 400, "message": "Camapaign Name and offer serial mismatched", "data": {}})

        
        day_wise_stats = camp_wise_stats(campaign_name, event_name, channel, network, offer_id,Pay_out, event_day)

        if not day_wise_stats:
            return Response({"status": 400, "message": "Requirements not found", "data": {}})

        status = 500
        
        stat_days = list(day_wise_stats.keys())
        min_day = min(stat_days)
        # max_day = max(day_wise_stats.keys())

        if event_day < min_day:
            return Response({"status": 500, "message": "Min day should be "+ str(min_day), "data": {}})
        
        target_day =  max((d for d in stat_days if d <= event_day), default=min_day)
        required_installs = day_wise_stats[target_day]

        required_events = events_per_day_stats(campaign_name, event_name, channel, network, offer_id)        

        is_eligible = False

        if install_count > required_installs:
            event_details = EventInfo.objects.filter(offer_serial=offer_serial, event_name=event_name, event_day__lte=event_day).values("event_count")

            total_event_count = sum((event['event_count'] for event in event_details))
           
            required_event_count = int(round(install_count / required_installs))
            is_eligible = total_event_count < required_event_count

            if required_events:
                today = datetime.now().strftime('%Y-%m-%d')
                completed_event_count = EventInfo.objects.filter(offer_serial=offer_serial, event_name=event_name + "_done", created_at__gte=str(today)).values("event_count")
                completed_event_count = sum((event['event_count'] for event in completed_event_count))

                if completed_event_count >= required_events:
                    is_eligible = False

            if campaign_name == "underarmourauto":

                today = datetime.now().strftime('%Y-%m-%d')

                revenue_details = EventInfo.objects.filter(event_name=event_name, created_at__gte=str(today)).values("revenue")
                total_revenue = sum((event['revenue'] for event in revenue_details))    

                if total_revenue + int(revenue) >= 36300:
                    is_eligible = False 
            
            if is_eligible and not track_only:
                event_details, created = EventInfo.objects.get_or_create(campaign_name=campaign_name,offer_serial=install_details,event_name=event_name,event_day=event_day,defaults={"event_count": 1, "revenue": revenue})

                if not created:
                    event_details.event_count += 1
                    event_details.revenue += float(revenue)
                    event_details.save()
                    
            status = 200
        
        return Response({"status": status, "message": "Success", "data": {"is_allowed": is_eligible}})

class EventCount(APIView):
    def get(self, request):
        campaign_name = request.GET.get('campaign_name')
        event_name = request.GET.get("event_name")
        offer_serial = request.GET.get("offer_serial")
        event_day = request.GET.get("event_day")
        revenue = request.GET.get("revenue", 0)
        track_only = request.GET.get("track_only", False)
        required_timezone = request.GET.get("required_timezone")

        if not all([campaign_name, event_name, offer_serial, event_day]):
            return Response({"status": 400,"message": "Missing required parameters","data": {}})

        try:
            event_day = int(event_day)
        except ValueError:
            return Response({"status": 400,"message": "Invalid event_day. It must be an integer.","data": {}})

        if event_day > 7:
            return Response({"status": 400, "message": "Max day allowed is 7", "data": {}})

        # if required_timezone:
        #     try:
        #         install_details = InstallDataTZ.objects.get(serial=offer_serial)
        #     except InstallDataTZ.DoesNotExist:
        #         return Response({"status": 404,"message": "Install record not found for given serial","data": {}})
        # else:
        try:
            install_details = InstallData.objects.get(serial=offer_serial)
        except InstallData.DoesNotExist:
            return Response({"status": 404,"message": "Install record not found for given serial","data": {}})

        channel = install_details.channel
        network = install_details.network
        offer_id = install_details.offer_id
        install_count = install_details.installs
        offer_serial = install_details.serial

        if install_details.campaign_name != campaign_name:
            return Response({"status": 400, "message": "Camapaign Name and offer serial mismatched", "data": {}})

        
        day_wise_stats = camp_wise_stats(campaign_name, event_name, channel, network, offer_id, event_day)

        if not day_wise_stats:
            return Response({"status": 400, "message": "Requirements not found", "data": {}})

        status = 500
        
        stat_days = list(day_wise_stats.keys())
        min_day = min(stat_days)
        # max_day = max(day_wise_stats.keys())

        if event_day < min_day:
            return Response({"status": 500, "message": "Min day should be "+ str(min_day), "data": {}})
        
        target_day =  max((d for d in stat_days if d <= event_day), default=min_day)
        required_installs = day_wise_stats[target_day]

        required_events = events_per_day_stats(campaign_name, event_name, channel, network, offer_id)

        is_eligible = False

        if install_count > required_installs:
            # event_details = EventInfo.objects.filter(offer_serial=offer_serial, event_name=event_name, event_day__lte=event_day).values("event_count")
            # total_event_count = sum((event['event_count'] for event in event_details))
            # required_event_count = int(round(install_count / required_installs))
            # is_eligible = total_event_count < required_event_count

            if required_events:
                today = datetime.now().strftime('%Y-%m-%d')
                # if required_timezone:
                #     completed_event_count = EventInfoTZ.objects.filter(offer_serial=offer_serial, event_name=event_name + "_done", created_at__gte=str(today)).values("event_count")
                # else:
                completed_event_count = EventInfo.objects.filter(offer_serial=offer_serial, event_name=event_name + "_done", created_at__gte=str(today)).values("event_count")
                completed_event_count = sum((event['event_count'] for event in completed_event_count))
                if (completed_event_count/install_count)*100 <= required_events:
                    is_eligible = True            
                    
            status = 200
        
        return Response({"status": status, "message": "Success", "data": {"is_allowed": is_eligible}})

class camps_running_status(APIView):
    def get(self, request):        

        today = timezone.now().date()
        start_date = today - timedelta(days=6)

        # Helper for nested default dicts
        def nested_dict():
            return defaultdict(nested_dict)

        result = {"data": {"offer_info": nested_dict()}}

        # Get InstallData
        installs = InstallData.objects.filter(
            created_at__range=(start_date, today)
        ).values("campaign_name", "network", "offer_id", "created_at", "installs")

        for row in installs:
            offer_key = f"{row['campaign_name']}::{row['network']}::{row['offer_id']}"
            date_key = row["created_at"].isoformat()
            result["data"]["offer_info"][offer_key][date_key]["install_count"] += row["installs"]

        # Get EventInfo
        events = EventInfo.objects.filter(
            created_at__range=(start_date, today)
        ).values("campaign_name", "network", "offer_id", "created_at", "event_name", "event_day", "event_count")

        for event in events:
            offer_key = f"{event['campaign_name']}::{event['network']}::{event['offer_id']}"
            date_key = event["created_at"].isoformat()
            event_name = event["event_name"]
            event_day = str(event["event_day"])

            result["data"]["offer_info"][offer_key][date_key]["event_info"][event_name][event_day] += event["event_count"]

        # Convert defaultdicts to dict
        def to_dict(obj):
            if isinstance(obj, defaultdict):
                return {k: to_dict(v) for k, v in obj.items()}
            return obj

        return to_dict(result)


class Compare_event_stats(APIView):
    def get(self, request):
        campaign_name = request.GET.get('campaign_name')
        event_name = request.GET.get("event_name")
        event_name_2 = request.GET.get("event_name_2")        
        event_day = request.GET.get("event_day")

        created_at = datetime.now().strftime('%Y-%m-%d')

        output_data = {}

        events = EventInfo.objects.filter(campaign_name=campaign_name,created_at=created_at, event_day=event_day).values("event_name", "event_count", "offer_serial")

        for rows in events:
            offer_serial = rows.get("offer_serial")
            if offer_serial not in output_data:
                output_data[offer_serial] = {}

            if rows.get("event_name") not in output_data.get(offer_serial):
                output_data[offer_serial][rows.get("event_name")] = rows.get("event_count")

        updated_entries = {}
        for key, value in output_data.items():
            event_count = value.get(event_name, 0)
            done_event_count = value.get(event_name_2, 0)

            if event_count - done_event_count > 1:
                updated_entries[key] = value
                events = EventInfo.objects.filter(event_name=event_name,offer_serial = key, event_day=event_day).get()
                events.event_count = value.get(event_name_2, 0) + 1
                events.save()





        #         install_data = InstallData.objects.filter(campaign_name=campaign_name, created_at=date, channel=channel, network=network, offer_id=offer_id)

        # if not install_data:
        #     install_details = InstallData(campaign_name=campaign_name, channel=channel, network=network, offer_id=offer_id, currency=currency, installs=1)
        # else:
        #     install_details = install_data.get()
        #     install_details.installs += 1
        # install_details.save()
                





        # for row in installs:
        #     camp_name = row["campaign_name"]
        #     if camp_name not in output_data:
        #         output_data[camp_name] = {}
        #     offer_key = f"{row['channel']}::{row['network']}::{row['offer_id']}"
        #     date_key = row["created_at"].isoformat()

        #     if offer_key not in output_data[camp_name]:
        #         output_data[camp_name][offer_key] = {}

        #     if date_key not in output_data[camp_name][offer_key]:
        #         output_data[camp_name][offer_key][date_key] = {}

        #     events = EventInfo.objects.filter(offer_serial_id=row["serial"], **ev_filter_dict).values("event_name", "event_day", "event_count", "revenue", "created_at")
        #     event_data = {}
        #     if events:
        #         for event in events:
        #             event_name = event["event_name"]
        #             event_day = str(event["event_day"])

        #             if event_name not in event_data:
        #                 event_data[event_name] = {}

        #             event_data[event_name][event_day]= event["event_count"]

        #     output_data[camp_name][offer_key][date_key] = {"installs" : row["installs"], "events": event_data}

        return Response({"status": 200, "message": "Success", "data": updated_entries})


API_KEY = "2a8fad1896a9d051d5ed1763"  # Replace with your actual API key

class CurrencyConvertAPIView(APIView):
    def post(self, request):

        url = "https://v6.exchangerate-api.com/v6/2a8fad1896a9d051d5ed1763/latest/USD"
        response = requests.get(url)

        if response.status_code != 200:
            return Response({"error": "Failed to fetch exchange rate"}, status=500)

        data = response.json()

        record = ExchangeRate.objects.create(
            from_currency="USD",
            to_currency="INR",
            amount=1,
            raw_response=data
        )

        return Response({
            "message": "Exchange rate saved successfully",
            "id": record.id
        }, status=201)

    def get(self, request):
        records = ExchangeRate.objects.all().order_by("-timestamp")
        result = []
        for r in records:
            result.append({
                "id": r.id,
                "from_currency": r.from_currency,
                "to_currency": r.to_currency,
                "amount": r.amount,
                "timestamp": r.timestamp,
                "raw_response": r.raw_response
            })
        return Response(result, status=200)

class db_health(APIView):
    def get(self, request):
        try:
            connections['default'].ensure_connection()
            return Response({"status": "ok", "db": "connected"})
        except Exception as e:
            _msg = f"""
            🚨 *DB HEALTH CHECK FAILED*

            • Service   : Django API
            • Check     : Database Connection
            • Status    : ❌ DOWN
            • Time      : {timezone.now().strftime('%Y-%m-%d %H:%M:%S %Z')}
            • Endpoint  : /health/db/
            • Error     : {str(e)}

            ⚠️ Immediate action recommended.
            """
            send_to_server_health_report(_msg)

            return Response({"status": "error", "db": "down"}, status=500)

class InstallDataHealth(APIView):
    def get(self, request):
        try:
            last_2_hours = timezone.now() - timedelta(hours=2)

            exists = InstallData.objects.filter(
                created_at__gte=last_2_hours
            ).exists()

            if exists:
                return Response({
                    "status": "ok",
                    "message": "Entries found in last 2 hours"
                }, status=200)

            return Response({
                "status": "warning",
                "message": "No entries found in last 2 hours"
            }, status=200)

        except Exception as e:

            return Response({
                "status": "error",
                "message": "Check failed"
            }, status=500)

class ServerHealth(APIView):
    def get(self, request):
        return Response({
            'resp': 'OK'
        })
        
def send_to_server_health_report(_msg):

    webhook_url = "https://chat.googleapis.com/v1/spaces/AAQAaJoIej8/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=glHq92wJLF4Yq2QB_AdpoGSfTXRiEU6No5OPOmGTrk4"

    payload = {
        "text": _msg
    }

    try:
        resp = requests.post(
            webhook_url,
            json=payload,
            timeout=10
        )

        resp.raise_for_status()

    except Exception as e:
        print("❌ Google Chat webhook failed:", str(e))


class Running_camps_stats(APIView):
    def get(self, request):
        campaign_name = request.GET.get('campaign_name')
        event_name = request.GET.get("event_name")
        from_date = request.GET.get("from_date")
        to_date = request.GET.get("to_date")
        channel = request.GET.get("channel")
        network = request.GET.get("network")
        offer_id = request.GET.get("offer_id")

        if not from_date:
            today = timezone.now().date()
            from_date = today - timedelta(days=6)
        
        if not to_date:
            to_date = timezone.now().date()

        output_data = {}

        filter_dict = {}
        if channel:
            filter_dict["channel"] = channel
        if network:
            filter_dict["network"] = network
        if offer_id:
            filter_dict["offer_id"] = offer_id
        if campaign_name:
            filter_dict["campaign_name"] = campaign_name

        ev_filter_dict = {}
        if event_name:
            ev_filter_dict["event_name"] = event_name

        installs = InstallData.objects.filter(created_at__range=(from_date, to_date), **filter_dict).values("campaign_name", "channel", "network", "offer_id", "created_at", "installs", "serial")


        for row in installs:
            camp_name = row["campaign_name"]
            if camp_name not in output_data:
                output_data[camp_name] = {}
            offer_key = f"{row['channel']}::{row['network']}::{row['offer_id']}"
            date_key = row["created_at"].isoformat()

            if offer_key not in output_data[camp_name]:
                output_data[camp_name][offer_key] = {}

            if date_key not in output_data[camp_name][offer_key]:
                output_data[camp_name][offer_key][date_key] = {}

            events = EventInfo.objects.filter(offer_serial_id=row["serial"], **ev_filter_dict).values("event_name", "event_day", "event_count", "revenue", "created_at")
            event_data = {}
            if events:
                for event in events:
                    event_name = event["event_name"]
                    event_day = str(event["event_day"])

                    if event_name not in event_data:
                        event_data[event_name] = {}

                    event_data[event_name][event_day]= event["event_count"]

            output_data[camp_name][offer_key][date_key] = {"installs" : row["installs"], "events": event_data}

        return Response({"status": 200, "message": "Success", "data": output_data})
    

    # def post(self, request):
    #     EventInfo.objects.filter()


class DB_event_randomness(APIView):
    def get(self, request):

        campaign_name = request.GET.get('campaign_name')
        channel = request.GET.get("channel")
        network = request.GET.get("network")
        offer_id = request.GET.get("offer_id")


        campaign_stats = get_stats(campaign_name)
        if not campaign_stats:
            return Response({})
        
        result = {}

        for event_name, event_data in campaign_stats.items():

            if all(isinstance(v, (int, float)) for v in event_data.values()):
                result[event_name] = event_data
                continue

            keys_to_try = [
                f"{channel}::{network}::{offer_id}",
                f"{channel}::{network}::*",
                f"{channel}::*::{offer_id}",
                f"*::{network}::{offer_id}",
                f"{channel}::*::*",
                f"*::*::{offer_id}",
                f"*::{network}::*",
                "*::*::*"
            ]

            for key in keys_to_try:
                if key in event_data:
                    result[event_name] = event_data[key]
                    break
            else:
                result[event_name] = list(event_data.values())[0]

        return Response(result)



