from django.http import HttpResponse
import subprocess
import json
from subprocess import STDOUT, PIPE
import sqlite3
import random
import execjs
import datetime
import time
import requests
import mysql.connector as mysql
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from collections import defaultdict
from datetime import timedelta
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


def get_tatapalette_orders(request):
    request_data = json.loads(request.body)
    request_type = request_data.get("request_type")
    valid_status = request_data.get("valid_status", False)

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()  

        current_date = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y")
        cursor.execute('''SELECT COUNT(DISTINCT OrderId) FROM tatapalette_orderIds WHERE UsedAt LIKE "{}%" AND ShipmentStatus = "Shipment Delivered"'''.format(current_date))
        data = cursor.fetchall()
        ids_used = data[0][0]

        if valid_status:
            if ids_used<=50:
                cursor.execute('''SELECT * FROM tatapalette_orderIds WHERE NOT OrderId_Status=1 AND  ShipmentStatus = "Shipment Delivered" AND validStatus=1 ORDER BY OrderId ASC''') #ShipmentUploadTime ASC
                data = cursor.fetchall()
                order_id = data[0][2]

                if request_type != "test":
                    used_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
                    cursor.execute("UPDATE tatapalette_orderIds SET OrderId_Status=1, UsedAt='{}' WHERE OrderId='{}'".format(used_at, order_id))
                    conn.commit()
            else:
                order_id = "-1"
        else:
            cursor.execute('''SELECT * FROM tatapalette_orderIds WHERE NOT OrderId_Status=1 AND  ShipmentStatus = "Shipment Delivered" AND validStatus=0 ORDER BY OrderId ASC''') #ShipmentUploadTime ASC
            data = cursor.fetchall()
            order_id = data[0][1]

            if request_type != "test":
                used_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
                cursor.execute("UPDATE tatapalette_orderIds SET OrderId_Status=1, UsedAt='{}' WHERE OrderId='{}'".format(used_at, order_id))
                conn.commit()

        response_code = 200
        message = "success"
    except Exception as e:
        response_code = 500
        message = str(e)
        order_id = "-1"
        ids_used = -1

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "order_id": order_id, "ids_used":ids_used}))

def get_available_orders_count(request):
    try:
        request_data = json.loads(request.body)
        valid_status = request_data.get("valid_status", False)
    except:
        valid_status = False
    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()    

        if valid_status:        
            cursor.execute('''SELECT COUNT(DISTINCT OrderId) FROM tatapalette_orderIds WHERE NOT OrderId_Status=1 AND validStatus=1 AND ShipmentStatus = "Shipment Delivered"''')
            data = cursor.fetchall()
            count = data[0]  
        else:
            cursor.execute('''SELECT COUNT(DISTINCT OrderId) FROM tatapalette_orderIds WHERE NOT OrderId_Status=1 AND validStatus=0 AND ShipmentStatus = "Shipment Delivered"''')
            data = cursor.fetchall()
            count = data[0]  
        response_code = 200
        message = "success"

    except Exception as e:
        response_code = 500
        message = str(e)
        count = None

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "total_orders": count}))


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

        created_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
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

def get_univest_orders(request):
    request_data = json.loads(request.body)
    request_type = request_data.get("request_type")

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()  
        
        cursor.execute('''SELECT * FROM univest_orderIds WHERE NOT status=1 ORDER BY order_id ASC''')
        data = cursor.fetchall()
        order_id = data[0][2]

        if request_type != "test":
            used_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
            cursor.execute("UPDATE univest_orderIds SET status=1, used_at='{}' WHERE order_id='{}'".format(used_at, order_id))
            conn.commit()

        response_code = 200
        message = "success"
    except Exception as e:
        response_code = 500
        message = str(e)
        order_id = -1

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "order_id": order_id}))

def get_univest_orders_count(request):
    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()    
        
        cursor.execute('''SELECT COUNT(DISTINCT order_id) FROM univest_orderIds WHERE NOT status=1''')
        data = cursor.fetchall()
        count = data[0]   
        response_code = 200
        message = "success"

    except Exception as e:
        response_code = 500
        message = str(e)
        count = None

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "total_orders": count}))

def get_zalora_orders_count(request):
    request_data = json.loads(request.body)
    country = request_data.get("country")

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()    
        
        cursor.execute('''SELECT COUNT(DISTINCT order_id) FROM zalora_orderIds WHERE NOT isUsed=1 AND country ="{}"'''.format(country))
        data = cursor.fetchall()
        count = data[0]   
        response_code = 200
        message = "success"

    except Exception as e:
        response_code = 500
        message = str(e)
        count = None

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "total_orders": count}))

def get_zalora_orders(request):
    request_data = json.loads(request.body)
    country = request_data.get("country")
    user_type = request_data.get("user_type")

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()  
        
        cursor.execute('''SELECT * FROM zalora_orderIds WHERE NOT isUsed=1 AND country ="{}" ORDER BY order_id DESC'''.format(country))
        data = cursor.fetchall()
        order_id = data[0][4]

        cursor.execute('''SELECT * FROM zalora_orderIds WHERE order_id = "{}"'''.format(order_id))
        data = cursor.fetchall()

        if user_type == "server":
            used_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
            cursor.execute("UPDATE zalora_orderIds SET isUsed=1, used_at='{}' WHERE order_id='{}'".format(used_at, order_id))
            conn.commit()

        response_code = 200
        message = "success"
    except Exception as e:
        response_code = 500
        message = str(e)
        data = {}

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "data": data}))

@api_view(['POST'])
def update_zalora_orderid_status(request):
    request_data = json.loads(request.body)
    order_id = request_data.get("order_id")
    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor() 

        used_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
        cursor.execute("UPDATE zalora_orderIds SET isUsed=0, used_at='{}' WHERE order_id='{}'".format(used_at, order_id))
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

def get_samco_user_data(request):
    request_data = json.loads(request.body)
    user_type = request_data.get("user_type")

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()  
        
        cursor.execute('''SELECT * FROM samco_userIds WHERE NOT isUsed=1 ORDER BY user_id ASC''')
        data = cursor.fetchall()
        user_id = data[0][3]
        data = {"user_id": user_id, "user_details": data[0][4]}
        

        # cursor.execute('''SELECT * FROM samco_userIds WHERE order_id = "{}"'''.format(order_id))
        # data = cursor.fetchall()

        if user_type == "server":
            used_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
            cursor.execute("UPDATE samco_userIds SET isUsed=1, used_at='{}' WHERE user_id='{}'".format(used_at, user_id))
            conn.commit()

        response_code = 200
        message = "success"
    except Exception as e:
        response_code = 500
        message = str(e)
        data = {}

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "data": data}))

def get_samco_users_count(request):

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()    
        
        cursor.execute('''SELECT COUNT(DISTINCT user_id) FROM samco_userIds WHERE NOT isUsed=1''')
        data = cursor.fetchall()
        count = data[0]   
        response_code = 200
        message = "success"

    except Exception as e:
        response_code = 500
        message = str(e)
        count = None

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "total_orders": count}))

def get_flappdeals_orderId(request):
    request_data = json.loads(request.body)
    user_type = request_data.get("user_type")

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()  
        
        cursor.execute('''SELECT * FROM flappdeals_orderIds WHERE NOT isUsed=1 ORDER BY order_id ASC''')
        data = cursor.fetchall()
        order_id = data[0][4]
        data = {"order_id": order_id}

        if user_type == "server":
            used_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
            cursor.execute("UPDATE flappdeals_orderIds SET isUsed=1, used_at='{}' WHERE order_id='{}'".format(used_at, order_id))
            conn.commit()

        response_code = 200
        message = "success"
    except Exception as e:
        response_code = 500
        message = str(e)
        data = {}

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "data": data}))

def get_flappdeals_orders_count(request):

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()    
        
        cursor.execute('''SELECT COUNT(DISTINCT order_id) FROM flappdeals_orderIds WHERE NOT isUsed=1''')
        data = cursor.fetchall()
        count = data[0]   
        response_code = 200
        message = "success"

    except Exception as e:
        response_code = 500
        message = str(e)
        count = None

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "total_orders": count}))

def get_practo_orderId(request):
    request_data = json.loads(request.body)
    user_type = request_data.get("user_type")

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()  

        current_date = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y")
        cursor.execute('''SELECT COUNT(DISTINCT order_id) FROM practo_orderIds WHERE used_at LIKE "{}%"'''.format(current_date))
        data = cursor.fetchall()
        ids_used = data[0][0]

        if ids_used <40:        
            cursor.execute('''SELECT * FROM practo_orderIds WHERE NOT isUsed=1 ORDER BY order_id ASC''')
            data = cursor.fetchall()
            order_id = data[0][4]
            data = {"order_id": order_id}

            if user_type == "server":
                used_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
                cursor.execute("UPDATE practo_orderIds SET isUsed=1, used_at='{}' WHERE order_id='{}'".format(used_at, order_id))
                conn.commit()
        else:
            data = {"order_id": None}

        response_code = 200
        message = "success"
    except Exception as e:
        response_code = 500
        message = str(e)
        data = {}

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "data": data}))

def get_practo_orders_count(request):

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()    
        
        cursor.execute('''SELECT COUNT(DISTINCT order_id) FROM practo_orderIds WHERE NOT isUsed=1''')
        data = cursor.fetchall()
        count = data[0]   
        response_code = 200
        message = "success"

    except Exception as e:
        response_code = 500
        message = str(e)
        count = None

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "total_orders": count}))

def get_tamasha_userId(request):
    request_data = json.loads(request.body)
    user_type = request_data.get("user_type")

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()  

        # current_date = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y")
        cursor.execute('''SELECT COUNT(DISTINCT user_id) FROM tamasha_userIds''')
        data = cursor.fetchall()
        ids_used = data[0][0]

        # if ids_used <50:        
        cursor.execute('''SELECT * FROM tamasha_userIds WHERE NOT isUsed=1 ORDER BY user_id ASC''')
        data = cursor.fetchall()
        user_id = data[0][1]
        username = data[0][2]
        data = {"user_id": user_id, "username": username}

        if user_type == "server":
            used_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
            cursor.execute("UPDATE tamasha_userIds SET isUsed=1, used_at='{}' WHERE user_id='{}'".format(used_at, user_id))
            conn.commit()
        # else:
        #     data = {"user_id": None, "username":None}

        response_code = 200
        message = "success"
    except Exception as e:
        response_code = 500
        message = str(e)
        data = {}

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "data": data}))

def get_tamasha_users_count(request):

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()    
        
        cursor.execute('''SELECT COUNT(DISTINCT user_id) FROM tamasha_userIds WHERE NOT isUsed=1''')
        data = cursor.fetchall()
        count = data[0]   
        response_code = 200
        message = "success"

    except Exception as e:
        response_code = 500
        message = str(e)
        count = None

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "total_orders": count}))

def get_cleartrip_id(request):
    request_data = json.loads(request.body)
    user_type = request_data.get("user_type")

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()  
     
        cursor.execute('''SELECT * FROM cleartrip_Ids WHERE NOT isUsed=1 ORDER BY trip_id ASC''')
        data = cursor.fetchall()
        trip_id = data[0][1]
        data = {"trip_id": trip_id}

        if user_type == "server":
            used_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
            cursor.execute("UPDATE cleartrip_Ids SET isUsed=1, used_at='{}' WHERE trip_id='{}'".format(used_at, trip_id))
            conn.commit()

        response_code = 200
        message = "success"
    except Exception as e:
        response_code = 500
        message = str(e)
        data = {}

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "data": data}))

def get_cleartrip_ids_count(request):

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()    
        
        cursor.execute('''SELECT COUNT(DISTINCT trip_id) FROM cleartrip_Ids WHERE NOT isUsed=1''')
        data = cursor.fetchall()
        count = data[0]   
        response_code = 200
        message = "success"

    except Exception as e:
        response_code = 500
        message = str(e)
        count = None

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "total_orders": count}))

def get_sololearn_userId(request):
    request_data = json.loads(request.body)
    user_type = request_data.get("user_type")
    subscription_type = request_data.get("subscription_type")

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()  
     
        cursor.execute('''SELECT * FROM sololearn_userIds WHERE NOT isUsed=1 AND subscription_type = '{}' ORDER BY user_id ASC'''.format(subscription_type))
        data = cursor.fetchall()
        user_id = data[0][1]
        data = {"user_id": user_id, "subscription_type":subscription_type}

        if user_type == "server":
            used_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
            cursor.execute("UPDATE sololearn_userIds SET isUsed=1, used_at='{}' WHERE user_id='{}'".format(used_at, user_id))
            conn.commit()

        response_code = 200
        message = "success"
    except Exception as e:
        response_code = 500
        message = str(e)
        data = {}

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "data": data}))

def get_sololearn_users_count(request):

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()    
        
        cursor.execute('''SELECT COUNT(DISTINCT user_id) FROM sololearn_userIds WHERE NOT isUsed=1''')
        data = cursor.fetchall()
        count = data[0]   
        response_code = 200
        message = "success"

    except Exception as e:
        response_code = 500
        message = str(e)
        count = None

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "total_orders": count}))

def get_petbook_orderId(request):
    request_data = json.loads(request.body)
    user_type = request_data.get("user_type")

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()  
        
        cursor.execute('''SELECT * FROM petbook_Ids WHERE NOT isUsed=1 ORDER BY order_id ASC''')
        data = cursor.fetchall()
        order_id = data[0][1]
        data = {"order_id": order_id}

        if user_type == "server":
            used_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
            cursor.execute("UPDATE petbook_Ids SET isUsed=1, used_at='{}' WHERE order_id='{}'".format(used_at, order_id))
            conn.commit()

        response_code = 200
        message = "success"
    except Exception as e:
        response_code = 500
        message = str(e)
        data = {}

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "data": data}))

def get_petbook_orders_count(request):

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()    
        
        cursor.execute('''SELECT COUNT(DISTINCT order_id) FROM petbook_Ids WHERE NOT isUsed=1''')
        data = cursor.fetchall()
        count = data[0]   
        response_code = 200
        message = "success"

    except Exception as e:
        response_code = 500
        message = str(e)
        count = None

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "total_orders": count}))

def get_elelive_userId(request):
    request_data = json.loads(request.body)
    user_type = request_data.get("user_type")

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()  
        
        cursor.execute('''SELECT * FROM elelive_userIds WHERE NOT isUsed=1 ORDER BY user_id ASC''')
        data = cursor.fetchall()
        user_id = data[0][1]
        data = {"user_id": user_id}

        if user_type == "server":
            used_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
            cursor.execute("UPDATE elelive_userIds SET isUsed=1, used_at='{}' WHERE user_id='{}'".format(used_at, user_id))
            conn.commit()

        response_code = 200
        message = "success"
    except Exception as e:
        response_code = 500
        message = str(e)
        data = {}

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "data": data}))

def get_elelive_users_count(request):

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()    
        
        cursor.execute('''SELECT COUNT(DISTINCT user_id) FROM elelive_userIds WHERE NOT isUsed=1''')
        data = cursor.fetchall()
        count = data[0]   
        response_code = 200
        message = "success"

    except Exception as e:
        response_code = 500
        message = str(e)
        count = None

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "total_users": count}))

def get_ladygentleman_order(request):
    request_data = json.loads(request.body)
    user_type = request_data.get("user_type")

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()  

        # current_date = datetime.datetime.fromtimestamp(time.time()).strftime("%d.%m.%Y")
        
        cursor.execute('''SELECT * FROM ladygentleman_orderData WHERE NOT isUsed=1 ORDER BY order_id ASC''')#AND order_date LIKE "{}" ORDER BY order_id ASC'''.format(current_date))
        data = cursor.fetchall()
        order_id = data[0][1]
        data = {"order_id": order_id}

        if user_type == "server":
            used_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
            cursor.execute("UPDATE ladygentleman_orderData SET isUsed=1, used_at='{}' WHERE order_id='{}'".format(used_at, order_id))
            conn.commit()

        response_code = 200
        message = "success"
    except Exception as e:
        response_code = 500
        message = str(e)
        data = {}

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "data": data}))

def get_ladygentleman_order_count(request):

    # try:
    conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
    cursor = conn.cursor()    
    
    # current_date = datetime.datetime.fromtimestamp(time.time()).strftime("%d.%m.%Y")
    cursor.execute('''SELECT COUNT(DISTINCT order_id) FROM ladygentleman_orderData WHERE NOT isUsed=1''')#AND order_date LIKE "{}"'''.format(current_date))
    data = cursor.fetchall()
    count = data[0]   
    response_code = 200
    message = "success"

    # except Exception as e:
        # response_code = 500
        # message = str(e)
        # count = None

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "total_users": count}))

def get_styli_order(request):
    request_data = json.loads(request.body)
    user_type = request_data.get("user_type")

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()  

        # current_date = datetime.datetime.fromtimestamp(time.time()).strftime("%d.%m.%Y")
        
        cursor.execute('''SELECT * FROM stylishop_orderId WHERE NOT isUsed=1 ORDER BY order_id ASC''')#AND order_date LIKE "{}" ORDER BY order_id ASC'''.format(current_date))
        data = cursor.fetchall()
        order_id = data[0][2]
        data = {"order_id": order_id}

        if user_type == "server":
            used_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
            cursor.execute("UPDATE stylishop_orderId SET isUsed=1, used_at='{}' WHERE order_id='{}'".format(used_at, order_id))
            conn.commit()

        response_code = 200
        message = "success"
    except Exception as e:
        response_code = 500
        message = str(e)
        data = {}

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "data": data}))

def get_styli_order_count(request):

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()    
        
        # current_date = datetime.datetime.fromtimestamp(time.time()).strftime("%d.%m.%Y")
        cursor.execute('''SELECT COUNT(DISTINCT order_id) FROM stylishop_orderId WHERE NOT isUsed=1''')#AND order_date LIKE "{}"'''.format(current_date))
        data = cursor.fetchall()
        count = data[0]   
        response_code = 200
        message = "success"

    except Exception as e:
        response_code = 500
        message = str(e)
        count = None

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "total_users": count}))

def get_pocket52_userId(request):
    request_data = json.loads(request.body)
    user_type = request_data.get("user_type")

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()  
        
        cursor.execute('''SELECT * FROM pocket52_userId WHERE NOT isUsed=1 ORDER BY user_id ASC''')
        data = cursor.fetchall()
        user_id = data[0][1]
        data = {"user_id": user_id}

        if user_type == "server":
            used_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
            cursor.execute("UPDATE pocket52_userId SET isUsed=1, used_at='{}' WHERE user_id='{}'".format(used_at, user_id))
            conn.commit()

        response_code = 200
        message = "success"
    except Exception as e:
        response_code = 500
        message = str(e)
        data = {}

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "data": data}))

def get_pocket52_users_count(request):

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()    
        
        cursor.execute('''SELECT COUNT(DISTINCT user_id) FROM pocket52_userId WHERE NOT isUsed=1''')
        data = cursor.fetchall()
        count = data[0]   
        response_code = 200
        message = "success"

    except Exception as e:
        response_code = 500
        message = str(e)
        count = None

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "total_users": count}))

def get_smytten_orderId(request):
    request_data = json.loads(request.body)
    user_type = request_data.get("user_type")

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()  
        
        cursor.execute('''SELECT * FROM smytten_orderId WHERE NOT isUsed=1 AND order_status LIKE "{}%" ORDER BY order_id ASC'''.format("DELIVERED"))

        data = cursor.fetchall()
        order_id = data[0][1]
        data = {"order_id": order_id}

        if user_type == "server":
            used_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
            cursor.execute("UPDATE smytten_orderId SET isUsed=1, used_at='{}' WHERE order_id='{}'".format(used_at, order_id))
            conn.commit()

        response_code = 200
        message = "success"
    except Exception as e:
        response_code = 500
        message = str(e)
        data = {}

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "data": data}))

def get_smytten_orders_count(request):

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()    
        
        cursor.execute('''SELECT COUNT(DISTINCT order_id) FROM smytten_orderId WHERE NOT isUsed=1 AND order_status LIKE "DELIVERED%" ''')
        data = cursor.fetchall()
        count = data[0]   
        response_code = 200
        message = "success"

    except Exception as e:
        response_code = 500
        message = str(e)
        count = None

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "total_users": count}))

def get_lenskart_orderId(request):
    request_data = json.loads(request.body)
    user_type = request_data.get("user_type")

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()  
        
        cursor.execute('''SELECT * FROM lenskart_orderId WHERE NOT isUsed=1 ORDER BY order_id ASC''')

        data = cursor.fetchall()
        order_id = data[0][1]
        data = {"order_id": order_id}

        if user_type == "server":
            used_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
            cursor.execute("UPDATE lenskart_orderId SET isUsed=1, used_at='{}' WHERE order_id='{}'".format(used_at, order_id))
            conn.commit()

        response_code = 200
        message = "success"
    except Exception as e:
        response_code = 500
        message = str(e)
        data = {}

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "data": data}))

def get_lenskart_orders_count(request):

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()    
        
        cursor.execute('''SELECT COUNT(DISTINCT order_id) FROM lenskart_orderId WHERE NOT isUsed=1''')
        data = cursor.fetchall()
        count = data[0]   
        response_code = 200
        message = "success"

    except Exception as e:
        response_code = 500
        message = str(e)
        count = None

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "total_users": count}))

def get_myteam11_userId(request):
    request_data = json.loads(request.body)
    user_type = request_data.get("user_type")

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()  
        
        cursor.execute('''SELECT * FROM myteam11_userId WHERE NOT isUsed=1 ORDER BY user_id ASC''')
        data = cursor.fetchall()
        user_id = data[0][1]
        data = {"user_id": user_id}

        if user_type == "server":
            used_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
            cursor.execute("UPDATE myteam11_userId SET isUsed=1, used_at='{}' WHERE user_id='{}'".format(used_at, user_id))
            conn.commit()

        response_code = 200
        message = "success"
    except Exception as e:
        response_code = 500
        message = str(e)
        data = {}

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "data": data}))

def get_myteam11_userId_count(request):

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()    
        
        cursor.execute('''SELECT COUNT(DISTINCT user_id) FROM myteam11_userId WHERE NOT isUsed=1''')
        data = cursor.fetchall()
        count = data[0]   
        response_code = 200
        message = "success"

    except Exception as e:
        response_code = 500
        message = str(e)
        count = None

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "total_users": count}))

def get_gamezy_userId(request):
    request_data = json.loads(request.body)
    user_type = request_data.get("user_type")

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()  
        
        cursor.execute('''SELECT * FROM gamezypoker_userId WHERE NOT isUsed=1 ORDER BY user_id ASC''')
        data = cursor.fetchall()
        user_id = data[0][1]
        data = {"user_id": user_id}

        if user_type == "server":
            used_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
            cursor.execute("UPDATE gamezypoker_userId SET isUsed=1, used_at='{}' WHERE user_id='{}'".format(used_at, user_id))
            conn.commit()

        response_code = 200
        message = "success"
    except Exception as e:
        response_code = 500
        message = str(e)
        data = {}

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "data": data}))

def get_gamezy_users_count(request):

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()    
        
        cursor.execute('''SELECT COUNT(DISTINCT user_id) FROM gamezypoker_userId WHERE NOT isUsed=1''')
        data = cursor.fetchall()
        count = data[0]   
        response_code = 200
        message = "success"

    except Exception as e:
        response_code = 500
        message = str(e)
        count = None

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "total_users": count}))

def get_galaxychat_userData(request):
    request_data = json.loads(request.body)
    user_type = request_data.get("user_type")

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()  
        
        cursor.execute('''SELECT * FROM galaxy_user_data WHERE NOT isUsed=1 ORDER BY user_id ASC''')
        data = cursor.fetchall()
        user_id = data[0][1]
        user_name = data[0][2]
        data = {"user_id": user_id, "username": user_name}

        if user_type == "server":
            used_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
            cursor.execute("UPDATE galaxy_user_data SET isUsed=1, used_at='{}' WHERE user_id='{}'".format(used_at, user_id))
            conn.commit()

        conn.close()

        response_code = 200
        message = "success"
    except Exception as e:
        response_code = 500
        message = str(e)
        data = {}

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "data": data}))

def get_galaxychat_users_count(request):

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()    
        
        cursor.execute('''SELECT COUNT(DISTINCT user_id) FROM galaxy_user_data WHERE NOT isUsed=1''')
        data = cursor.fetchall()
        count = data[0]   
        response_code = 200
        message = "success"

        conn.close()

    except Exception as e:
        response_code = 500
        message = str(e)
        count = None

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "total_users": count}))

def get_derma_orderData(request):
    request_data = json.loads(request.body)
    user_type = request_data.get("user_type")

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()  
        
        cursor.execute('''SELECT * FROM derma_user_data WHERE NOT isUsed=1 ORDER BY order_id ASC''')
        data = cursor.fetchall()
        order_id = data[0][1]
        order_total = data[0][2]
        order_date = data[0][3]
        system_order_id = data[0][4]
        data = {"order_id": order_id, "order_total": order_total, "order_date": order_date, "system_order_id": system_order_id}

        if user_type == "server":
            used_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
            cursor.execute("UPDATE derma_user_data SET isUsed=1, used_at='{}' WHERE order_id='{}'".format(used_at, order_id))
            conn.commit()

        response_code = 200
        message = "success"
    except Exception as e:
        response_code = 500
        message = str(e)
        data = {}

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "data": data}))

def get_derma_orders_count(request):

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()    
        
        cursor.execute('''SELECT COUNT(DISTINCT order_id) FROM derma_user_data WHERE NOT isUsed=1''')
        data = cursor.fetchall()
        count = data[0]   
        response_code = 200
        message = "success"

    except Exception as e:
        response_code = 500
        message = str(e)
        count = None

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "total_users": count}))

def get_toonsutra_user_data(request):
    request_data = json.loads(request.body)
    user_type = request_data.get("user_type")

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()  
        
        cursor.execute('''SELECT * FROM toonsutra_user_data WHERE NOT isUsed=1 ORDER BY user_id ASC''')
        data = cursor.fetchall()
        user_id = data[0][1]
        extra_details = data[0][2]
        data = {"user_id": user_id, "extra_details": extra_details}

        if user_type == "server":
            used_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
            cursor.execute("UPDATE toonsutra_user_data SET isUsed=1, used_at='{}' WHERE user_id='{}'".format(used_at, user_id))
            conn.commit()

        response_code = 200
        message = "success"
    except Exception as e:
        response_code = 500
        message = str(e)
        data = {}

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "data": data}))

def get_toonsutra_users_count(request):

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()    
        
        cursor.execute('''SELECT COUNT(DISTINCT user_id) FROM toonsutra_user_data WHERE NOT isUsed=1''')
        data = cursor.fetchall()
        count = data[0]   
        response_code = 200
        message = "success"

    except Exception as e:
        response_code = 500
        message = str(e)
        count = None

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "total_users": count}))

def get_sportbaazi_userId(request):
    request_data = json.loads(request.body)
    user_type = request_data.get("user_type")

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()  
        
        cursor.execute('''SELECT * FROM sportbaazi_userId WHERE NOT isUsed=1 ORDER BY user_id DESC''')
        data = cursor.fetchall()
        user_id = data[0][1]
        data = {"user_id": user_id}

        if user_type == "server":
            used_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
            cursor.execute("UPDATE sportbaazi_userId SET isUsed=1, used_at='{}' WHERE user_id='{}'".format(used_at, user_id))
            conn.commit()

        response_code = 200
        message = "success"
    except Exception as e:
        response_code = 500
        message = str(e)
        data = {}

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "data": data}))

def get_sportbaazi_users_count(request):

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()    
        
        cursor.execute('''SELECT COUNT(DISTINCT user_id) FROM sportbaazi_userId WHERE NOT isUsed=1''')
        data = cursor.fetchall()
        count = data[0]   
        response_code = 200
        message = "success"

    except Exception as e:
        response_code = 500
        message = str(e)
        count = None

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "total_users": count}))

def get_privalia_userId(request):
    request_data = json.loads(request.body)
    user_type = request_data.get("user_type")

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()  
        
        cursor.execute('''SELECT * FROM privalia_userId WHERE NOT isUsed=1 ORDER BY user_id DESC''')
        data = cursor.fetchall()
        user_id = data[0][1]
        data = {"user_id": user_id}

        if user_type == "server":
            used_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
            cursor.execute("UPDATE privalia_userId SET isUsed=1, used_at='{}' WHERE user_id='{}'".format(used_at, user_id))
            conn.commit()

        response_code = 200
        message = "success"
    except Exception as e:
        response_code = 500
        message = str(e)
        data = {}

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "data": data}))

def get_privalia_users_count(request):

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()    
        
        cursor.execute('''SELECT COUNT(DISTINCT user_id) FROM privalia_userId WHERE NOT isUsed=1''')
        data = cursor.fetchall()
        count = data[0]   
        response_code = 200
        message = "success"

    except Exception as e:
        response_code = 500
        message = str(e)
        count = None

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "total_users": count}))

def get_rentomojo_userId(request):
    request_data = json.loads(request.body)
    user_type = request_data.get("user_type")

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()  
        
        cursor.execute('''SELECT * FROM rentmojo_userId WHERE NOT isUsed=1 ORDER BY user_id DESC''')
        data = cursor.fetchall()
        user_id = data[0][1]
        data = {"user_id": user_id}

        if user_type == "server":
            used_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
            cursor.execute("UPDATE rentmojo_userId SET isUsed=1, used_at='{}' WHERE user_id='{}'".format(used_at, user_id))
            conn.commit()

        response_code = 200
        message = "success"
    except Exception as e:
        response_code = 500
        message = str(e)
        data = {}

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "data": data}))

def get_rentomojo_users_count(request):

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()    
        
        cursor.execute('''SELECT COUNT(DISTINCT user_id) FROM rentmojo_userId WHERE NOT isUsed=1''')
        data = cursor.fetchall()
        count = data[0]   
        response_code = 200
        message = "success"

    except Exception as e:
        response_code = 500
        message = str(e)
        count = None

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "total_users": count}))

def get_muthoot_userId(request):
    request_data = json.loads(request.body)
    user_type = request_data.get("user_type")

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()  
        
        cursor.execute('''SELECT * FROM muthootfino_userId WHERE NOT isUsed=1 ORDER BY user_id DESC''')
        data = cursor.fetchall()
        user_id = data[0][1]
        data = {"user_id": user_id}

        if user_type == "server":
            used_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
            cursor.execute("UPDATE muthootfino_userId SET isUsed=1, used_at='{}' WHERE user_id='{}'".format(used_at, user_id))
            conn.commit()

        conn.close()

        response_code = 200
        message = "success"
    except Exception as e:
        response_code = 500
        message = str(e)
        data = {}

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "data": data}))

def get_muthoot_users_count(request):

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()    
        
        cursor.execute('''SELECT COUNT(DISTINCT user_id) FROM muthootfino_userId WHERE NOT isUsed=1''')
        data = cursor.fetchall()
        count = data[0]   
        response_code = 200
        message = "success"

        conn.close()

    except Exception as e:
        response_code = 500
        message = str(e)
        count = None

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "total_users": count}))

def get_bottles_orderId(request):
    request_data = json.loads(request.body)
    user_type = request_data.get("user_type")

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()  
        
        cursor.execute('''SELECT * FROM bottles_order_data WHERE NOT isUsed=1 ORDER BY order_id ASC''')
        data = cursor.fetchall()
        order_id = data[0][1]
        order_total = data[0][2]
        order_date = data[0][3]
        data = {"order_id": order_id, "order_total": order_total, "order_date": order_date}
        

        # cursor.execute('''SELECT * FROM samco_userIds WHERE order_id = "{}"'''.format(order_id))
        # data = cursor.fetchall()

        if user_type == "server":
            used_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
            cursor.execute("UPDATE bottles_order_data SET isUsed=1, used_at='{}' WHERE order_id='{}'".format(used_at, order_id))
            conn.commit()

        response_code = 200
        message = "success"
    except Exception as e:
        response_code = 500
        message = str(e)
        data = {}

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "data": data}))

def get_bottles_orders_count(request):

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()    
        
        cursor.execute('''SELECT COUNT(DISTINCT order_id) FROM bottles_order_data WHERE NOT isUsed=1''')
        data = cursor.fetchall()
        count = data[0]   
        response_code = 200
        message = "success"

    except Exception as e:
        response_code = 500
        message = str(e)
        count = None

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "total_orders": count}))


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
                    created_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
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
                    created_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
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
                    created_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
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
                    created_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
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
                    created_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
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
                    created_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
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
                    created_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
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
                    created_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
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
                    created_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
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
                    created_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
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
    date_ = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d")
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

def get_finimize_userData(request):
    request_data = json.loads(request.body)
    user_type = request_data.get("user_type")
    os_type = request_data.get("os_type")

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()  
        
        cursor.execute('''SELECT * FROM finimizeios_user_data WHERE os_type ="{}" AND NOT isUsed=1 ORDER BY user_id DESC'''.format(os_type))
        data = cursor.fetchall()
        user_id = data[0][1]
        extra_details = data[0][2]
        subs_type = data[0][5]
        data = {"user_id": user_id, "extra_details": extra_details, "subs_type": subs_type}

        if user_type == "server":
            used_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
            cursor.execute("UPDATE finimizeios_user_data SET isUsed=1, used_at='{}' WHERE user_id='{}'".format(used_at, user_id))
            conn.commit()

        response_code = 200
        message = "success"
    except Exception as e:
        response_code = 500
        message = str(e)
        data = {}

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "data": data}))

def get_finimize_users_count(request):

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()    
        
        cursor.execute('''SELECT COUNT(DISTINCT user_id) FROM finimizeios_user_data WHERE NOT isUsed=1''')
        data = cursor.fetchall()
        count = data[0]   
        response_code = 200
        message = "success"

    except Exception as e:
        response_code = 500
        message = str(e)
        count = None

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "total_users": count}))

def get_tajrummy_userId(request):
    request_data = json.loads(request.body)
    user_type = request_data.get("user_type")

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()  
        
        cursor.execute('''SELECT * FROM tajrummey_userId WHERE NOT isUsed=1 ORDER BY user_id DESC''')
        data = cursor.fetchall()
        user_id = data[0][1]
        data = {"user_id": user_id}

        if user_type == "server":
            used_at = datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3]
            cursor.execute("UPDATE tajrummey_userId SET isUsed=1, used_at='{}' WHERE user_id='{}'".format(used_at, user_id))
            conn.commit()

        response_code = 200
        message = "success"
    except Exception as e:
        response_code = 500
        message = str(e)
        data = {}

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "data": data}))

def get_tajrummy_users_count(request):

    try:
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="team2@backend", database="techteam")
        cursor = conn.cursor()    
        
        cursor.execute('''SELECT COUNT(DISTINCT user_id) FROM tajrummey_userId WHERE NOT isUsed=1''')
        data = cursor.fetchall()
        count = data[0]   
        response_code = 200
        message = "success"

    except Exception as e:
        response_code = 500
        message = str(e)
        count = None

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "total_users": count}))

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
        

        if required_timezone:
            try:
                import pytz
                print (required_timezone)
                tz = pytz.timezone(required_timezone)
                date = datetime.datetime.now(tz).date()
                print ("kfc", date)
            except Exception as e:
                print (e)
                date = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d")
        else:
            date = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d")       


        if not all([campaign_name, channel, network, offer_id]):
            return Response({"status": 400,"message": "Missing required parameters","data": {}})
        
        if required_timezone:
            install_data = InstallData.objects.filter(campaign_name=campaign_name, created_at__gte=str(date), channel=channel, network=network, offer_id=offer_id)
        else:
            install_data = InstallData.objects.filter(campaign_name=campaign_name, created_at=date, channel=channel, network=network, offer_id=offer_id)            

        if not install_data:
            install_details = InstallData(created_at=date, campaign_name=campaign_name, channel=channel, network=network, offer_id=offer_id, currency=currency, installs=1)
        else:
            install_details = install_data.get()
            install_details.installs += 1
        install_details.save()

        return Response({"status": 200, "message": "Install Tracked", "status": 200, "data": {"count": install_details.installs, "serial": install_details.serial}})

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
                date = datetime.datetime.now(tz).date()
                print ("kfc", date)
            except Exception as e:
                print (e)
                date = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d")
        else:
            date = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d")
        
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
    
    elif campaign_name == "williamhillsportiosmodd" and offer_id in ["apps-whsports.ios", "test"]:
        return 1
    
    elif campaign_name == "lottermxiosmodd"  and channel in ["mobpine", "77ads", "appamplify"]:
        return 3


def camp_wise_stats(campaign_name, event_name, channel, network, offer_id,Pay_out=0.0):
    if campaign_name == "quickcashonlinemodd" and event_name == "approvals_cnt_server":
        return {0: 41, 1:24, 2:19, 3:16.6}

    elif campaign_name == "moomootrademodd" and event_name == "af_ss_event_202":
        return {1: 41, 2:33, 3:23, 4:19}
    
    elif campaign_name == "bd678auto" and event_name == "8jcdcl":
        return {0:14.28, 1:11.11, 2:9.09, 3: 8.33}
    
    elif campaign_name == "fb77auto" and event_name == "f80wwq":
        return {0:14.28, 1:12.5, 2:11.11, 3:10}

    elif campaign_name == "ragnarokmodd" and event_name == "revenue_490":
        return {0: 40, 2:30}

    elif campaign_name == "ragnarokmodd" and event_name == "revenue_1500":
        return {0: 15}

    elif campaign_name == "ragnarokmodd" and event_name == "revenue_1000":
        return {1: 40, 4:30}

    elif campaign_name == "ragnarokmodd" and event_name == "revenue_100":
        return {3: 40, 5:30}

    elif campaign_name == "moovauto" and channel == "vestaapps" and network == "vkmdigital" and offer_id == "movkmvammpdup" and event_name == "xgivki":
        return {0: 4, 1:4}
    
    elif campaign_name == "moovauto" and channel == "vestaapps" and network == "vkmdigital" and offer_id == "movkmvammpdup" and event_name == "ld4kw6":
        return {0: 19, 1:19}

    elif campaign_name == "moovauto" and channel == "test" and network == "test" and offer_id == "test" and event_name == "xgivki":
        return {0: 4, 1:4}
    
    elif campaign_name == "moovauto" and channel == "test" and network == "test" and offer_id == "test" and event_name == "ld4kw6":
        return {0: 19, 1:19}

    elif campaign_name == "boylesportstmodd" and event_name == "n_ftd" and channel:
        # if channel in ["mobpine", "77ads", "appamplify"]:
        #     return {0: 80, 1:30, 2:23}
        # else:
        # if offer_id in ["boyadexaosmmp", "byax1aosafvammp"]:
        #     return {0:80, 1:25, 2:16.6, 3:14.2}

        # if offer_id in ['boymobvammp', 'byaxaosafvammp','boyadexiosmmp','boyhilimmp','boymovmmp']:
        #     return {0:70, 1:35, 2:23}
        
        # return {0: 16, 1:8, 2:6.5}

        return {0:43, 1:25, 2:20}

    elif campaign_name == "boylesportstmodd" and event_name == "n_reg_confirm":
        # if offer_id in ["boyadexaosmmp", "byax1aosafvammp"]:
        #     return {0:12.5, 1:7.14, 2:12.5, 3:5}
        
        # return {0: 6.6, 1:4.5, 2: 3.7, 3:3.3}

        return {0: 25, 1:16.6, 2: 10}

    elif campaign_name == "singamodd" and event_name=="risk-control":
        return {0: 43, 1:27}
    
    elif campaign_name == "singamodd" and event_name=="loanapplied":
        return {0: 43, 1: 43}

    elif campaign_name == "leonrutmodd" and event_name=="af_first_deposit":
        return {0: 27, 1: 22, 2: 18}
    
    elif campaign_name == "ikukuruuiosauto" and event_name == "mcaw45":
        return {0:6, 1:6}
    
    elif campaign_name == "ikukuruuiosauto" and event_name == "wvzrbc":
        return {0:12, 1:12}
    
    elif campaign_name == "juanhandmodd" and event_name == "af_fst_insbrw_suss" and channel in ["mobpine", "77ads", "appamplify"]:
        return {0:33, 1: 20, 2: 14.28, 3: 12.5}

    elif campaign_name == "juanhandmodd" and event_name == "af_fst_insbrw_suss":
        return {0:45, 1: 35, 2: 25, 3: 20, 4: 16}

    elif campaign_name == "juanhandmodd" and event_name == "af_tzmx_10":
        return {0:47, 1: 33, 2: 24, 3: 20, 4: 15}

    # elif campaign_name == "myacuvuemodd" and event_name == "Registration_Success":
    #     return {0:2.3, 1: 2}

    elif campaign_name == "jazzcashmodd" and event_name == "L1_registration_successful":

        if channel in ["77ads", "appamplify"] and network =='doromobile':
            return {0:2.11, 1:2, 2:1.72, 3:1.58 }

        elif channel in ["mobpine", "77ads", "appamplify"] and 0.05<=float(Pay_out)<=0.10 :
            return {0:2.22, 1:2, 2: 1.81, 3: 1.72, 4: 1.66}
        else:
            return {0:2.5, 1:1.7, 2: 1.6, 3: 1.4, 4: 1.2}

    elif campaign_name == "moovauto" and event_name == "ld4kw6":
        return {0:11, 1:8.3 , 2: 6.6, 3: 6.6}

    elif campaign_name == "moovauto" and event_name == "ggjyhe":
        return {0:20, 1:14.28, 2:11.11, 3: 9}

    elif campaign_name == "ucuzabiletauto" and event_name == "vnc85a":
        return {0:20, 1:12.5, 2:10, 3: 8.7}
    
    elif campaign_name == "profit2modd" and event_name == "ActionNewOrder":
        return {0:10, 1:8.3, 2: 7.14, 3: 6.6}

    elif campaign_name == "dupoiniosauto" and event_name == "7py4mn":
        return {0:23, 1:16.6, 2: 12.5, 3: 10}
    
    elif campaign_name == "loveparadaiseauto" and event_name == "revenue_199":
        return {0:25, 1: 20, 2:16.6, 3:14.2, 4:12.5, 5:11.11}
    
    elif campaign_name == "loveparadaiseauto" and event_name == "revenue_499":  
        return {0:68, 1: 45, 2:30 }

    elif campaign_name == "cashroyaleauto" and event_name == "revenue_599":
        return {0:20, 1: 16.66, 3:14.28}
    
    elif campaign_name == "cashroyaleauto" and event_name == "revenue_999":
        return {1:80, 2:41, 4:30}
    
    elif campaign_name == "moneycolorauto" and event_name == "revenue_199":
        return {0:10, 1: 6.6, 2:5.5, 3:4.76, 4:4.16, 5:3.84, 6:3.44, 7:3.22}
    
    elif campaign_name == "moneycolorauto" and event_name == "revenue_499":
        return {0:16.6, 1: 11.11, 2:8.33, 3:7.14, 4:6.25, 5:5.5, 6:5, 7:4.54 }

    # elif campaign_name == "dailysolitaremodd" and event_name == "revenue_099":
    #     return {0:16.6, 1: 11.11, 2:8.33, 3:7.14, 4:6.25, 5:5.88, 6:5.5, 7:5.26 }
    
    # elif campaign_name == "dailysolitaremodd" and event_name == "revenue_599":
    #     return {0:25, 1:14.2, 2:12.5, 3:11.1, 4:10, 5:9, 6:8.3, 7:8.3}
    
    elif campaign_name == "dailysolitaremodd" and event_name == "revenue_099":
        return {0:13, 1: 10, 3:7.5, 4:6, 6:4, 7:3.5}
    
    elif campaign_name == "dailysolitaremodd" and event_name == "revenue_599":
        return {0:7.5, 1:7.5, 2:7, 3:6, 4:5, 5:4.28}

    elif campaign_name == "tikettmodd" and event_name == "af_purchase":
        return {0:50, 1:50, 2:33.3}
    
    elif campaign_name == "tikettmodd" and event_name == "af_purchase_toDO" and channel == "77ads" and network == "dopemobi" and offer_id == "9dope-todo":
        return {0:20, 1:12.5, 2:10, 3:8}

    elif campaign_name == "tikettmodd" and event_name == "af_purchase_toDO":
        return {0:14, 1:11, 2:10, 3:8}

    elif campaign_name == "tikettmodd" and event_name == "af_purchase_hotel" and channel == "77ads" and network == "dopemobi" and offer_id == "9dope-hotel":
        return {0:20, 1:12.5, 2:10, 3:8}
    
    elif campaign_name == "tikettmodd" and event_name == "af_purchase_hotel":
        return {0:14, 1:12, 2:9, 3:8}

    elif campaign_name == "tikettmodd" and event_name == "af_purchase_flight" and channel == "77ads" and network == "dopemobi" and offer_id == "9dope-flight":
        return {0:20, 1:12.5, 2:10, 3:8}
    
    elif campaign_name == "tikettmodd" and event_name == "af_purchase_flight":
        return {0:16.6, 1:12.5, 2:11, 3:8}

    elif campaign_name == "axisinvestmodd" and event_name == "TXN Successful":
        return {0:29, 1:26, 2:20, 3:16.6, 4:14.28, 5:12.5, 6:12.5}

    elif campaign_name == "moneymetmodd" and event_name == "LoanApplicationV2.ApplicationSent.View":
        return {0:70, 1:50, 2:33, 3:33}
    
    elif campaign_name == "moneycatmxmodd" and event_name == "NEW_LOAN":
        return {0:150, 1:150}
    
    elif campaign_name == "signnowmodd" and event_name == "af_start_trial":
        return {0:20, 1:14.2, 2:11.11, 3:10}
    
    elif campaign_name == "signnowmodd" and event_name == "af_purchase":
        return {2:100, 3:100}
    
    elif campaign_name == "signnowmodd" and event_name == "af_subscribe":
        return {8:50, 9:50}

    elif campaign_name == "opaymodd" and channel == "77ads" and network == "dopemobi" and offer_id in ["7dope-opayy", "7dope-opayy2", "7dope-opayy3", "7dope-opayy4", "7dope-opayy5", "7dope-opayy6", "7dope-opayy7"] and event_name == "signup_success":
        return {0:3.7, 1:3.3, 2:3, 3:2.85}
    
    elif campaign_name == "opaymodd" and event_name == "signup_success":
        return {0:3.7, 1:3.44, 2:3.3}
    
    elif campaign_name == "opaymodd" and channel == "adshustle" and network == "leanmobi" and offer_id in ["noplenmmp"] and event_name == "first_transaction":
        return {0:7.14, 1:6.25, 2:5.67, 3:5}
    
    elif campaign_name == "opaymodd" and event_name == "first_transaction":
        return {0:16.6, 1:11, 2:7.14}
    
    elif campaign_name == "opaymodd" and event_name == "total_transaction":
        return {0:15, 1:10, 2:6}
    
    elif campaign_name == "hoteltonightautoios" and channel == "adshustle" and network == "advivifymedia" and offer_id in ["21653946", "21676889"] and event_name == "pey3pd":
        return {0: 12.5, 1:9, 2:7.14, 3:6.25}
    
    elif campaign_name == "hoteltonightautoios" and channel == "adshustle" and network == "attrimob" and offer_id == "817dup" and event_name == "pey3pd":
        return {0: 6.6, 1:5, 2:4, 3:3.33}
    
    elif campaign_name == "hoteltonightautoios" and event_name == "pey3pd":
        return {0:16.6, 1:11.11, 2:8.33, 3:7.14, 4:6.6}

    elif campaign_name == "hoteltonightauto" and event_name == "jviyct":
        return {0:16.6, 1:11.11, 2:8.33, 3:7.14, 4:6.6}

    elif campaign_name == "onmobileauto" and event_name == "jr95xb":
        # return {0:1.81, 1:1.56, 2:1.42, 3:1.33}
        return {0:1.33, 1:1.17, 2:1.11}

    elif campaign_name == "onmobilautoios" and event_name == "jr95xb":
        # return {0:1.81, 1:1.56, 2:1.42, 3:1.33}
        return {0:1.33, 1:1.07, 2:1.02}
    
    elif campaign_name == "magztermodd" and event_name == "mg_1month_freetrial":
        return {0:20, 1:14.2, 2:11.11, 3:10}
    
    elif campaign_name == "magztermodd" and event_name == "mg_1year_freetrial":
        return {0:20, 1: 14.2 , 2: 11.11 , 3: 10 }
    
    elif campaign_name == "paysettmodd" and event_name == "registration_success":
        return {0:2, 1:1.81, 2:1.6}
    
    elif campaign_name == "paysettmodd" and event_name == "send_success":
        return {0:10, 1:7.14, 2:6.25, 3:5.5}
    
    elif campaign_name == "puntitmodd" and event_name == "FTD":
        return {0:40, 1:25}

    elif campaign_name == "friendipayomauto" and event_name == "lql86o":
        return {0:10, 1:8, 2:6.5}
    
    elif campaign_name == "novawateriosmodd" and event_name == "af_purchase":
        return {0:16, 1:12.5, 2:10}

    elif campaign_name == "dimemodd" and event_name == "onboardSuccess":
        return {0:10, 1:7, 2:5, 3:4.34, 4:3.8}

    elif campaign_name == "dailynumbermatchauto" and event_name == "pdeipy":
        return {0:30, 1:30, 2:25, 3:25, 4: 20, 5:20}

    elif campaign_name == "cubiosmodd" and event_name == "esign_View_ActivateCL":
        return {0:85, 1:80, 2:60, 3:45, 4: 33}

    elif campaign_name == "bingofrenzytmodd" and event_name == "1_99":
        return {0:7, 1:7}

    elif campaign_name == "imagineartautoios" and event_name == "h5ihok":
        return {0:80, 1:33.33}

    elif campaign_name == "imagineartautoios" and event_name == "pdc6m9":
        return {0:80,1:50}

    elif campaign_name == "betrmodd" and event_name == "af_purchase":
        return {0:80,1:50,2:33.33}

    elif campaign_name == "uiuxmobileauto" and event_name == "rmlund":
        return {0:45, 1:33.33, 2:25, 3:20}
    
    elif campaign_name == "uiuxmobileauto" and event_name == "jjww2u":
        return {0:80}
    
    elif campaign_name == "garantiauto" and event_name == "otpgdr":
        return {0:30, 1:16.66, 2:12.5}
    
    elif campaign_name == "garantiauto" and event_name == "gr546v":
        return {0:30, 1:16.66, 2:12.5}

    elif campaign_name == "garantiauto" and event_name == "pfj58r":
        return {0:14, 1:9}
    
    elif campaign_name == "bybittmodd" and event_name == "eftd":
        return {0:90, 1:45}

    elif campaign_name == "bybittmodd" and event_name == "ftd":
        return {0:80, 1:16.67}
    
    # elif campaign_name == "bingofrenzytmodd" and event_name == "19_99":
    #     return {1:68, 2:68, 3:41, 4:41}
    
    elif campaign_name == "bingofrenzytmodd" and event_name == "4_99":
        return {4:7, 5:7}
    
    elif campaign_name == "bingofrenzytmodd" and event_name == "9_99":
        return {2:7, 3:7}

    elif campaign_name == "caesarsmodd" and event_name == "mb_deposit.first_time_deposit":
        return {0:15, 1:15}
    
    elif campaign_name == "newdouluomodd" and event_name == "0_99":
        return {0:23, 2:20, 4:16.67, 5:14.28, 6:12.5, 7:14.28}
    
    elif campaign_name == "newdouluomodd" and event_name == "4_99":
        return {0:29, 1:25, 3:20, 5:16.6, 6:14.28, 7:12.5}
    
    elif campaign_name == "newdouluomodd" and event_name == "9_99":
        return {1:41, 3:33, 5:25, 7:20}

    elif campaign_name == "newdouluomodd" and event_name == "14_99":
        return {2:41, 4:33, 6:25}
    
    elif campaign_name == "caesarscasinoiosmodd" and event_name == "mb_deposit.first_time_deposit":
        return {0:55, 1: 50}
    
    elif campaign_name == "mullerauto" and event_name == "x2mrfw":
        return {0:1.5, 1: 1.2}

    elif campaign_name == "mullerauto" and event_name == "fihqvn":
        return {0:1.8, 1: 1.6}
    
    elif campaign_name == "13cabstauto" and event_name == "swtdbc":
        return {0:1.5, 1: 1.5}

    elif campaign_name == "khiladiaddamodd" and event_name == "af_complete_registration":
        # return {0:1.8, 1: 1.6, 2:1.53, 3:1.42}
        return {0:1.8, 1: 1.53, 2:1.42, 3:1.33}
    
    elif campaign_name == "boylesportsiostmodd" and event_name == "n_ftd":
        # if channel in ["mobpine", "77ads", "appamplify"]:
        #     return {0: 80, 1:30, 2:23}
        # else:

        # if offer_id in ["boyadexiosmmp"]:
        #     return {0:80, 1:25, 2:16.6, 3:14.2}

        # if offer_id in ['byaxiosafvammp', 'byax1iosafvammp','boyadexiosmmp','boyhilimmp','boymovmmp']:
        #     return {0:70, 1:35, 2:23}

        # return {0: 16, 1:8, 2:6.5}

        return {0:43, 1:25, 2:20}

    elif campaign_name == "boylesportsiostmodd" and event_name == "n_reg_confirm":
        # if offer_id in ["byax1iosafvammp", "boyadexiosmmp"]:
        #     return {0:12.5, 1:7.14, 2:12.5, 3:5}
        # return {0: 6.6, 1:4.5, 2: 3.7, 3:3.3}
        return {0: 25, 1:16.6, 2: 10}
    
    elif campaign_name == "bcsinvestmenttmodd" and event_name == "93441_Onboard_OpenAcc_SignDocsSmsTap":
        return {0: 6.2, 1:5, 2: 4.34, 3:4, 4:3.84}

    elif campaign_name == "bcsinvestmenttmodd" and event_name == "28500_Instr_Bid_Success":

        if channel=="adshustle" and offer_id in ["bcsmnditvammp", "bcsmicovammp"]:
            return {0:9}

        return {0: 45, 1:23}

    elif campaign_name == "bcsinvestiosmodd" and event_name == "93441_Onboard_OpenAcc_SignDocsSmsTap":
        return {0: 6.2, 1:5, 2: 4.34, 3:4, 4:3.84}

    elif campaign_name == "bcsinvestiosmodd" and event_name == "28500_Instr_Bid_Success":

        return {0: 19, 1:12, 2:9.6, 3:8}

    elif campaign_name == "indigomoddteam2modd" and event_name == "af_purchase" and channel in ["mobpine", "77ads", "appamplify"]:
        return {0:12, 1:10, 2:9}
    
    elif campaign_name == "indigomoddteam2modd" and event_name == "af_purchase":
        return {0: 8, 1:7.33, 2: 6.14}
    
    elif campaign_name == "cloneindigomoddteam2modd" and event_name == "af_purchase":
        return {0: 9, 1:8.33, 2: 7.14}
    
    elif campaign_name == "clone2indigomoddteam2modd" and event_name == "af_purchase":
        return {0: 9, 1:8.33, 2: 7.14}
    
    elif campaign_name == "breakthroughkingdommodd" and event_name == "1_09":
        return {0:10, 1:20, 4:16.67, 5:14.28, 6:12.5, 7:14.28}
    
    elif campaign_name == "breakthroughkingdommodd" and event_name == "2_19":
        return {0:10, 1:25, 3:20, 5:16.6, 6:14.28, 7:12.5}
    
    elif campaign_name == "breakthroughkingdommodd" and event_name == "5_47":
        return {0:10, 1:8.3, 2:7.14, 3:6.25, 4:5.88, 5:5.5, 6:5, 7:4.54}
    
    elif campaign_name == "breakthroughkingdommodd" and event_name == "21_89":
        return {1:33, 2:25, 3:16.67, 4:12.5, 5:10, 6:9, 7:7.69}
    
    elif campaign_name == "kriptoauto" and event_name == "lpfhv5":
        return {0:9, 3:5}
    
    elif campaign_name == "homiedevmodd" and event_name == "af_subscribe":
        return {0:10, 1:5, 2:4}

    elif campaign_name == "homieiosmodd" and event_name == "af_subscribe":
        return {0:10, 1:7.5, 2:5}
    
    elif campaign_name == "dimeiosmodd" and event_name == "onboardSuccess":
        return {0:10, 1:7, 2:5, 3:4.34, 4:3.8}
    
    elif campaign_name == "kfcmexicotmodd" and event_name == "first_purchase":
        return {0:5, 3:5}
    
    elif campaign_name == "tejimaandiauto" and event_name == "csqfum":
        return {0:20, 1:16.6, 2: 14.28, 3:12.5}

    elif campaign_name == "teenpatiauto" and event_name == "0_36":
        return {0:20}
    
    elif campaign_name == "teenpatiauto" and event_name == "1_08":
        return {0:38, }
    
    elif campaign_name == "teenpatiauto" and event_name == "3_6":
        return {0:41, 1: 29}
    
    elif campaign_name == "teenpatiauto" and event_name == "10_79":
        return {1:41, 3:41}

    elif campaign_name == "alphabetoftastemodd" and event_name == "purchase_start":
        return {0:50, 1:33, 3:25, 4:20}

    elif campaign_name == "kafimodd" and event_name == "stock_order_matching":
        return {0:41, 1:33, 2:25, 3:20}
    
    elif campaign_name == "kafitradeiosmodd" and event_name == "stock_order_matching":
        return {0:41, 1:33, 2:25, 3:20}

    elif campaign_name == "mcdeliverymodd" and event_name == "af_purchase_delivery":

        if offer_id in ["mobs-mcd"]:
            return {0:5, 1:4, 2:3.3}
        
        return {0:6.6, 1:5.5, 2:5}
    
    elif campaign_name == "clonemcdeliverymodd" and event_name == "af_purchase_to_be_delivered":
        return {0:6.6, 1:5.5, 2:5}
    
    elif campaign_name == "raisinggoblinmodd" and event_name == "First_Purchase":
        return {0:6.67, 1:20}

    elif campaign_name == "rummytimemodd" and event_name == "user_first_add_cash":
        return {0:25, 1:16.67, 2:12.5 }

    elif campaign_name == "toponemarketauto" and event_name == "6uwnyv":
        return {0:65, 1:40}
    
    elif campaign_name == "toponemarketiosauto" and event_name == "f3a4ks":
        return {0:65, 1:40}

    elif campaign_name == "vpnpantheriosmodd" and event_name == "trial converted":
        return {3:33, 4:20, 5:14.28, 6:12.5, 7:11.1}

    elif campaign_name == "vpnpantheriosmodd" and event_name == "af_trial_started":
        return {0:14, 1:10, 2:7.5, 3:6.5}
        
    elif campaign_name == "zeptodeliverymodd" and event_name == "first_order_delivered":
        return {0:12, 1:9, 2:7.69, 3:6.6}

    elif campaign_name == "dupointmodd" and event_name == "yh7wzr" and channel=="adshustle" and network=="refrevenue" and offer_id=="duphurmmp":
        return {0:55}
    
    elif campaign_name == "dupointmodd" and event_name == "yh7wzr":
        return {0:33, 1:22, 2:18, 3:16}
    
    elif campaign_name == "youset2modd" and event_name == "generate_proposal_auto":
        return {0:33, 1:22, 2:18}
    
    elif campaign_name == "youset2modd" and event_name == "generate_proposal_home":
        return {0:41, 1:33}
    
    elif campaign_name == "yesmadammodd" and event_name == "af_complete_registration":
        return {0:2, 1:1.78, 2:1.66}
    
    elif campaign_name == "yesmadammodd" and event_name == "af_purchase":
        return {0:12.5, 1:10, 2:7.14}
        
    elif campaign_name == "bigloanmodd" and event_name == "issueNewCPA":
        return {1:90, 2:30, 3:20, 4:16, 5:14}
    
    elif campaign_name == "bigloanmodd" and event_name == "minconditionsapprove":
        if offer_id in ["bigldopvammp"]:
            return {0:12.5, 1:7.14, 2:6.6, 3:5}
        
        return {0:12.5, 1:8.3, 2:7.14, 3:6.6}

    elif campaign_name == "otpbankappmetrica" and event_name == "screen__dc_success_courier":
        return {1:70, 2:23, 3:14, 4:11, 5:10}

    elif campaign_name == "byutmodd" and event_name == "purchase_iJoin":
        return {0:20, 1:14.28, 2:12.5, 3:11.11, 4:10}

    elif campaign_name == "comparemodd" and event_name == "mfoDealConfirmed":
        return {0:33.33, 1:20, 2:16.66, 3:14.28, 4:12.25}
    
    elif campaign_name == "melivemodd" and event_name == "af_revenue":
        return {0:26, 1:20, 2:16}

    elif campaign_name == "metlivemodd" and event_name == "af_revenue":
        return {0:26, 1:20, 2:16}
    
    elif campaign_name == "globusappmetrica" and event_name == "purchaseEvent":
        return {0:45, 1:30}

    elif campaign_name == "parimatchthmodd" and event_name == "Deposit Successful First":
        return {0:25, 1:20, 2:16}

    elif campaign_name == "myntmodd" and event_name == "af_deposit":
        return {0:23, 1:20, 2:16.6, 3:14.28}

    elif campaign_name == "spinnytauto" and event_name == "cqjxvf":
        return {0:45, 1:30, 2:25}

    elif campaign_name == "shienindiamodd" and event_name == "af_purchase":
        return {0:30, 1:20, 2:14.28, 3:12.5}

    elif campaign_name == "digitalbankmodd" and event_name == "upgrade2SA":
        return {0:45, 1:16.6, 2:11.1}

    elif campaign_name == "woolsocksmodd" and event_name == "3ts38m":
        return {0:15, 1:11, 2:10, 3:9}

    elif campaign_name == "cimbthaimodd" and event_name == "NTB_Deposit_Open_Speed-d-plus_Success_Viewed":
        return {0:45, 1:30, 2:25}
    
    elif campaign_name == "cimbthaimodd" and event_name == "NTB_Deposit_Open_Chill-d_Success_Viewed":
        return {0:47, 1:32, 2:26}

    elif campaign_name == "cimbthaimodd" and event_name == "NTB_Mutual_Fund_Open_Deposit_And_MF_Success":
        return {0:70, 1:50, 2:33}

    elif campaign_name == "robotzaimerrmodd" and event_name == "signContractFirst":
        return {0:45, 1:30, 2:25}

    elif campaign_name == "stockitymodd" and event_name == "payment.deposit_first_new":
        return {0:45, 1:25, 2:20}
                
    elif campaign_name == "heliummobilemodd" and event_name == "app_purchase_free" and offer_id:
        if offer_id.isdecimal():
            return {0:5, 1:3} # {0:5, 1:4.5}
        else:
            return {0:30, 1:20, 2:16}

    elif campaign_name == "heliummobilemodd" and event_name == "purchase":
        return {0:45, 1:30, 2:25}

    elif campaign_name == "abhibusauto" and event_name == "cukuuk" and offer_id:
        if offer_id.isdecimal():
            return {0:5, 1:3}
        else:
            return {0:14, 1:8.33}
        

    elif campaign_name == "garantiauto" and event_name == "rmq154" and offer_id:
        if offer_id.isdecimal():
            return {0:2.5, 1:2.5}
        else:
            return  {0:12.5} 

    elif campaign_name == "duittmodd" and event_name == "Successful_loan":
        return {0:90, 1:30, 2:20, 3:16}
    
    elif campaign_name == "r888casinomodd" and event_name == "MB_First_Deposit":
        return {0:70, 1:50}
    
    elif campaign_name == "istanbulairportauto" and event_name == "duf9j9":
        return {0:4.4, 1:3.8, 2:3.5}
    
    elif campaign_name == "istanbulairportauto" and event_name == "pykeub":
        return {0:2.2, 1:2, 2:1.8}
    
    elif campaign_name == "sliceauto" and event_name == "ksdh0l":
        return {0:80, 1:33, 2:25}
    
    elif campaign_name == "sliceauto" and event_name == "ghmq8p":
        return {0:80, 1:25, 2:20, 3:16.6}
        
    elif campaign_name == "instamoneyquickmodd" and event_name == "AF_RF_Paid":
        return {0:45, 1:20, 2:14, 3:11, 4:10}
    
    elif campaign_name == "instamoneyquickmodd" and event_name == "AF_RF_LOAN_DISBURSED":
        return {1:45, 2:30, 3:24}

    elif campaign_name == "coinmenaauto" and event_name == "aj5y08":
        return {0:41, 1:19, 2:14, 3:11, 4:9}

    elif campaign_name == "smilesauto" and event_name == "a6ou21":
        return {0:45, 1:20, 2:14, 3:11}

    elif campaign_name == "netshoesmodd" and event_name == "af_purchase":

        if offer_id == 'dope-netshoes-251030' and channel == 'appamplify' and network =='dopemobi':
            return{0:100}

        # if offer_id in ["nesmetmmp"]:
        #     return {0:25, 1:17, 2:14}
        
        return {0:25, 1:17, 2:14}

    elif campaign_name == "bingoplustmodd" and event_name == "BINGOPLUS_EVENT_REGIST":
        return {0:3, 1:2.36, 2:2.09, 3:1.91}

    elif campaign_name == "bingoplustmodd" and event_name == "bingoplus_first_deposit":
        return {0:90, 1:45, 2:30}

    elif campaign_name == "myshiftappmetricat" and event_name == "ShiftCatalogShiftDetails_shift_booked":
        return {0:45, 1:25, 2:20}

    elif campaign_name == "shorttvtmodd" and event_name == "revenue_3499":
        return {0:45}
    
    elif campaign_name == "shorttvtmodd" and event_name == "revenue_4999":
        return {0:30}

    elif campaign_name == "shorttvtmodd" and event_name == "revenue_9999":
        return {0:16}

    elif campaign_name == "shorttvtmodd" and event_name == "revenue_349":
        return {1:90}
    
    elif campaign_name == "shorttvtmodd" and event_name == "revenue_499":
        return {2:90}
    
    elif campaign_name == "shorttvtmodd" and event_name == "revenue_999":
        return {3:90}
    
    elif campaign_name == "etomomodd" and event_name == "loan_requested":
        if offer_id.isdecimal():
            return {0:7}
        
        return {0:25, 1: 14.28, 2:11}
    
    elif campaign_name == "cryptocomtmodd" and event_name == "mktg:kyc_approved_push_sent":
        return {0:4, 1:3}
    
    elif campaign_name == "megogot2modd" and event_name == "af_purchase":
        return {0:6.66, 1:5.26, 2:4.76, 3:4.54}

    elif campaign_name == "wiomodd" and event_name == "view_screen_onboarding_app_submitted":
        return {0:80}

    elif campaign_name == "paisayaarauto" and event_name == "jbjcze":
        return {1:30, 2:20, 3: 16}

    elif campaign_name == "gsmtmodd" and event_name == "sign_up":
        return {0:3.33, 1:2.85, 2:2.63, 3:2.5}

    elif campaign_name == "gsmtmodd" and event_name == "order_completed_1st_time":
        return {0:10, 1:8,2:7, 3: 6}

    elif campaign_name == "bollingerauto" and event_name == "purchase":
        return {0:18, 1:9}

    # elif campaign_name == "bollingerauto" and event_name == "l1swxm":
    #     return {0:90, 1:50}

    # elif campaign_name == "bollingerauto" and event_name == "jzo4sk":
    #     return {0:48, 1:30}

    elif campaign_name == "joybuymodd" and event_name == "PURCHASE":
        return {0:25, 1:20, 2:16.6}
        
    elif campaign_name == "soulchilltmodd" and event_name == "revenue_049":
        return {1:35, 3:25, 5:15}

    elif campaign_name == "soulchilltmodd" and event_name == "revenue_099":
        return {2:40, 5:25, 6:17, 7:9}

    elif campaign_name == "soulchilltmodd" and event_name == "revenue_499":
        return {0:40, 3:25, 4:16}
    
    elif campaign_name == "soulchilltmodd" and event_name == "revenue_999":
        return {1:40}

    elif campaign_name == "kotak811mbtmodd" and event_name == "AccountOTP_OTP_Acq":
        return {0:30}
    
    elif campaign_name == "mylingueautoios" and event_name == "y3ahlf":

        if offer_id.isdecimal():
            return {0:2, 1:1.81, 2:1.63, 3:1.49}
        
        return {0:3.33, 1:2.77, 2:2.43, 3:2.22}

    elif campaign_name == "omniheroesmodd" and event_name == "revenue_099":
        return {4:49}

    elif campaign_name == "omniheroesmodd" and event_name == "revenue_499":
        return {0:25, 4:16}

    elif campaign_name == "omniheroesmodd" and event_name == "revenue_1499":
        return {0:24, 1:16, 2:12, 3:8, 5:7, 6:6.25}

    elif campaign_name == "nomadesimauto" and event_name == "5f3kzv":
        return {0:16, 1:11.11, 2:9.09, 3:8.33}

    elif campaign_name == "nouslibauto" and event_name == "chju3f":
        return {0:2, 1:1.78, 2:1.6}

    elif campaign_name == "nouslibauto" and event_name == "purchase":
        return {0:21, 1:16}

    elif campaign_name == "nouslibt2autoios" and event_name == "chju3f":
        return {0:2, 1:1.78, 2:1.6}

    elif campaign_name == "nouslibt2autoios" and event_name == "purchase":
        return {0:21, 1:16}

    elif campaign_name == "carjammodd" and event_name == "revenue199":
        return {1:15, 3:9,4:6.6}
    
    elif campaign_name == "carjammodd" and event_name == "revenue799":
        return {0:9, 2:6.6}
    
    elif campaign_name == "fabmobilemodd" and event_name == "ntb_casa_account_created":
        return {1:45, 2:30, 3: 23}

    elif campaign_name == "fabmobilemodd" and event_name == "ntb_cc_card_created":
        return {0:45, 1:30, 2:23, 3:19}

    elif campaign_name == "bbvamodd" and event_name == "portabilidad_nomina-app_approved":
        if channel=="adshustle" and network=="myfunadstrack" and offer_id=="bbvamyfmmp":
            return {1:80}
        return {0:40, 1:26, 2:20, 3:18}
    
    elif campaign_name == "babytrackermodd" and event_name == "af_start_trial":
        return {0:30, 1:18, 2:16}

    elif campaign_name == "babytrackermodd" and event_name == "af_subscribe":
        return {0:90, 1:45}
    
    elif campaign_name == "babytrackermodd" and event_name == "af_purchase":
        return {0:31, 1:19, 2:15, 3:12}

        
    elif campaign_name == "glowbabytrackeriosmodd" and event_name == "af_start_trial":
        return {0:30, 1:18, 2:16}

    elif campaign_name == "glowbabytrackeriosmodd" and event_name == "af_subscribe":
        return {0:90, 1:45}
    
    elif campaign_name == "glowbabytrackeriosmodd" and event_name == "af_purchase":
        return {0:31, 1:19, 2:15, 3:12}

    elif campaign_name == "onepuchmanmodd" and event_name == "revenue1516":
        return {0:17}
    
    elif campaign_name == "onepuchmanmodd" and event_name == "revenue488":
        return {0:9,1:6.6}

    elif campaign_name == "onepuchmanmodd" and event_name == "revenue103":
        return {0:19, 1:8}

    elif campaign_name == "vogaclosetiosauto" and event_name == "yewk8s":
        return {0:15, 1:9, 2:7}

    elif campaign_name == "mibptmodd" and event_name == 'FB_Mobile_complete registration':
        return {0:1.85, 1:1.6}
    
    elif campaign_name == "filteraiiosauto" and event_name == 'mjq7jz':
        return {0:30, 1:19, 2:16}
        
    elif campaign_name == "utimamarketsmodd" and event_name == 'P_FTD':
        return {1:30, 2:19, 3:16}
            
    elif campaign_name == "osagomodd" and event_name == 's2s-cpa-conversion':
        return {1:24, 2:14, 3:11, 4:9}
                
    elif campaign_name == "neobetiosmodd" and event_name == 'af_first_purchase':
        return {0:90, 1:45}

    elif campaign_name == "qustodioparentalauto" and event_name == '85anak':
        return {0:22.5, 1:15, 2:12.85}

    elif campaign_name == "qustodioparentalauto" and event_name == 'g2gfaz':
        return {0:90, 1:45, 2:30}
        
    elif campaign_name == "mexdinmodd" and event_name == 'first_loan_success':
        return {0:90, 1:30, 2:18, 3:15}

    elif campaign_name == "underarmourauto" and event_name == '5uo13w':

        if offer_id in ["undapcmmp", "test"]:
            return {0:15}
        
        return {0:15, 1:9, 2:6.42, 3:5.62}

    elif campaign_name == "nuiauto" and event_name == '1rck55':
        return {0:6, 1:4.5, 2:3.6, 3:3.21}
    
    elif campaign_name == "nuiauto" and event_name == 'vcoavi':
        return {0:45, 1:22.5, 2:18, 3:15}
    
    elif campaign_name == "credmaxmodd" and event_name == 'approvals_server':
        return {0:45, 1:30, 2:22.5, 3:18}

    elif campaign_name == "credmaxmodd" and event_name == 'tutorial_complete_server':
        return {0:90, 1:45, 2:30, 3:22.5}

    elif campaign_name == "cryptocomtmodd" and event_name == 'mktg:buy_crypto':
        return {0:25, 1:14, 2:11, 3:10}
    
    elif campaign_name == "bancaauto" and event_name == 'xnfrxy':
        return {0:30, 1:20, 2:14}

    elif campaign_name == "fiverrt2modd" and event_name == 'FTB_BUCKET':
        return {0:30, 1:18, 2:15}
    
    elif campaign_name == "fiverriosmodd" and event_name == 'FTB':
        return {0:30, 1:18, 2:15}
    
    elif campaign_name == "williamhillsportiosmodd" and event_name == 'FTD':
        if offer_id in ["apps-whsports.ios", "whuk2adgmmp"]:
            return {0:45}

        elif offer_id in ["willadghubmmp"]:
            return {0:50}
        
        elif offer_id in ["whsptadgmmp"]:
            return {0:60}

        return {0:30, 1:22.5, 2:18}

    # elif campaign_name == "vegasiosmodd" and event_name == 'FTD':
    #     return {0:45, 1:30, 2:22.5, 3:18}

    elif campaign_name == "vegasiosmodd" and event_name == 'registration':

        if offer_id in ['williamhill-mpjads-jan','mpj-wcios','adhub-whcasinoiios-26a017260']:
            return {0:6}
        # if channel in ['mobpine', '77ads', 'appamplify']:
        return {0:24, 1:12, 2:10}

        # return {0:6, 1:5, 2:3.91}
        # return {0:13, 1:8, 2:6}
    
    elif campaign_name == "vegasiosmodd" and event_name == 'FTD':
        
        if offer_id in ['williamhill-mpjads-jan','mpj-wcios','adhub-whcasinoiios-26a017260']:
            return {0:13}

        elif offer_id in ["wh2casdgmmp"]:
            return {0:67}
        # if channel in ['mobpine', '77ads', 'appamplify']:
        return {0:30, 1:20, 2:16}
        # return {0:24, 1:13, 2:10, 3:9}

    elif campaign_name == "cleanervpniosmodd" and event_name == 'apphud_trial_started':
        return {0:22.5, 1:15, 2:12.85, 3:11.25}

    elif campaign_name == "adblockeriosmodd" and event_name == 'apphud_trial_started':
        return {0:22.5, 1:15, 2:12.85, 3:11.25}

    elif campaign_name == "jyotiaiiosmodd" and event_name == 'apphud_trial_started':
        return {0:22.5, 1:15, 2:12.85, 3:11.25}

    elif campaign_name == "moneygrammiosmodd" and event_name == 'first_transaction':
        return {0:22.5, 1:15, 2:12.85, 3:11.25}

    elif campaign_name == "mixvpniosmodd" and event_name == 'apphud_trial_started':
        return {0:22.5, 1:15, 2:12.85, 3:11.25}

    elif campaign_name == "plantexpertaiiosmodd" and event_name == 'apphud_trial_started':
        return {0:22.5, 1:15, 2:12.85, 3:11.25}

    elif campaign_name == "888pokeriosmodd" and event_name == "MB_First_Deposit":
        return {0:90, 1:45, 2:30}

    elif campaign_name == "tataneuauto" and event_name == "CC_CARD_SELECTION":
        return {0:6, 1:5, 2:4.5}

    elif campaign_name == "tataneuauto" and event_name == "plm_disbursement":
        return {0:30, 1:18, 2:15, 3:12.85}

    elif campaign_name == "betfredsportsiosmodd" and event_name == "deposit":
        return {0:90, 1:30, 2:22.5, 3:18}

    elif campaign_name == "ajioiosmodd" and event_name == "first_purchase":
        return {0:45, 1:30, 2:22.5, 3:18}

    elif campaign_name == "cashmaxmodd" and event_name == "Successful_loan":
        return {0:90, 1:22.5, 2:15, 3:12.85}

    elif campaign_name == "idntimesmodd" and event_name == "Subscribe_success":
        return {0:45, 1:18, 2:12.85, 3:11.25}

    elif campaign_name == "teldaauto" and event_name == "ntd8cj":
        return {0:11.25, 1:7.5, 2:6, 3:5.29}

    elif campaign_name == "tenthousandmodd" and event_name == "revenue_099":
        return {0:90, 1:45, 3:30, 4:22.5, 5:18, 6:15, 7:12.85}
    
    elif campaign_name == "tenthousandmodd" and event_name == "revenue_499":
        return {0:48, 2:32}

    elif campaign_name == "vtb24tappmetrica" and event_name == "screenTap_notClient_liteData_litePasscode":
        return {0:2.5, 1:2}

    elif campaign_name == "mbbankmodd" and event_name == "AF_OB_SUCCESS":
        if offer_id in ["mbb2iwammp"]:
            return {0:30, 1:20, 2:16.6, 3:14.28}
        return {0:12.85, 1:9, 2:7.5}

    elif campaign_name == "mbbankautoios" and event_name == "AF_OB_SUCCESS":
        if offer_id in ["mbbiwammp"]:
            return {0:30, 1:20, 2:16.6, 3:14.28}
        
        return {0:12.85, 1:9, 2:7.5}

    elif campaign_name == "tawkeeltmodd" and event_name == "payment_completed":
        return {0:30, 1:18, 2:12.85, 3:11.25}

    elif campaign_name == "webullmodd" and event_name == "first_deposit_success_F":
        return {1:23, 2:13.5, 3:11.87}
    
    elif campaign_name == "lottermxiosmodd" and event_name == "FTD":

        if channel in ["mobpine", "77ads", "appamplify"]:
            return {0:12}

        if offer_id in ["17425"]:
            return {0:13}
        
        return {0:80, 1:33}
    
    elif campaign_name == "thelotterusiosmodd" and event_name == "FTD":
        return {0:80, 1:33}

    elif campaign_name == "blibliiosmodd" and event_name == "new_customer_purchase":
        return {0:24, 1:13.71, 2:10.66, 3:9.6}

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

    elif campaign_name == "mtcmusiciosmodd" and event_name == "af_subscribe":
        return {0:45, 1:24, 2:19}

    elif campaign_name == "mtcmusicmodd" and event_name == "af_subscribe":
        return {0:45, 1:24, 2:19}

    elif campaign_name == "bitoasistauto" and event_name == "deposit":
        return {0:45, 1:24, 2:19}

    elif campaign_name == "myacuvuemodd" and event_name == "Registration_Success":
        # return {0:3.3, 1:2.6, 2:2.06}
        return {0:2.22, 1:2.08, 2:1.92}

    elif campaign_name == "myacuvuemodd" and event_name == "fitting_events":

        return {0:5.8, 1:5.26, 2:4.76}

    elif campaign_name == "myfoodappmetrica" and event_name == "2990_rev":
        return {0:30, 1:19, 2:16}

    elif campaign_name == "myfoodappmetrica" and event_name == "2590_rev":
        return {0:31, 1:18, 2:15}

    elif campaign_name == "myacuvueiosmodd" and event_name == "Registration_Success":

        if offer_id in ["myiosappmmp"]:
            return {0:3.3, 1:2.77, 2:2.38}
        
        # return {0:2.6, 1:2.06, 2:2.4}
        return {0:2.22, 1:2.08, 2:1.92}

    elif campaign_name == "myacuvueiosmodd" and event_name == "fitting_events":

        if offer_id in ["myiosappmmp"]:
            return {0:12.5, 1:10, 2:7.14}
        
        # return {0:13, 1:9, 2:7}
        return {0:5.8, 1:5.26, 2:4.76}

    elif campaign_name == "bbvamodd" and event_name == "afiliacion_basica-app_online_purchases":

        if channel=="adshustle" and network=="myfunadstrack" and offer_id=="bbvamyfmmp":
            return {0:95, 1:48}
        return {0:48, 1:19, 2:14}

    elif campaign_name == "makebykbankiosmodd" and event_name == "ON2kSucceed":
        return {0:24, 1:11, 2:8, 3:7}

    elif campaign_name == "velvetvpniosmodd" and event_name == 'apphud_trial_started':
        return {0:22.5, 1:15, 2:12.85, 3:11.25}

    elif campaign_name == "bluerewardsmodd" and event_name == 'sign_up':
        return {0:8, 1:6, 2:5, 3:4.75, 4:4.31}
    
    elif campaign_name == "bluerewardsmodd" and event_name == 'sign_up':
        return {0:8, 1:6, 2:5, 3:4.75, 4:4.31}
    
    elif campaign_name == "paymeiosauto" and event_name == "zgxxz1":
        return {0:18, 1:11.25, 2:8}
    
    elif campaign_name == "paymeauto" and event_name == "zgxxz1":
        return {0:18, 1:11.25, 2:8}

    elif campaign_name == "seevpniosmodd" and event_name == 'apphud_trial_started':
        return {0:22.5, 1:15, 2:12.85, 3:11.25}
    
    elif campaign_name == "ajiomodd" and event_name == "luxe_purchase":
        return {0:19, 1: 11, 2:9}
    
    elif campaign_name == "ajiomodd" and event_name == "ajio_purchase":
        return {0:80, 1: 40}

    elif campaign_name == "octatrademodd" and event_name == "af_realtime_activation":
        return {0:90, 1: 45}
    
    elif campaign_name == "action247iosmodd" and event_name == "af_FTD":
        return {0:20}

    elif campaign_name == "sensorvpniosmodd" and event_name == 'apphud_trial_started':
        return {0:22.5, 1:15, 2:12.85, 3:11.25}

    elif campaign_name == "albertbudgetauto" and event_name == 'finished_signup_flow_and_bank':
        if offer_id.isdecimal():
            return {0:14, 1:12, 2:9}

        return {0:30, 1:24, 2:19}

    elif campaign_name == "weltradeauto" and event_name == "kbwb07":
        return {0:45, 1: 18}

    elif campaign_name == "weltradeauto" and event_name == "evpfo1":
        return {1:89}

    elif campaign_name == "vanaauto" and event_name == "15serm":
        return {0:89, 1: 30, 2: 18, 3:15}

    elif campaign_name == "sahimodd" and event_name == "5fno_completed":
        return {0:89, 1:22.5, 2:18.5}

    elif campaign_name == "moneymaniosmodd" and event_name == "NEW_CREDIT_ACTIVE_DB":
        return {0:89, 1: 30, 2: 18, 3:15}

    elif campaign_name == "moneyviewmodd" and event_name == "submit_success":
        return {0:30, 1: 19, 2: 16, 3:14}

    elif campaign_name == "viuhkmodd" and event_name == "subscription_payment_success":
        return {0:30, 1:24 , 2: 19}

    elif campaign_name == "tinkofft2modd" and event_name == "credit_approve_offline":
        return {0:45, 1:30, 2: 22.5, 3: 18}

    elif campaign_name == "tinkofft2modd" and event_name == "debit_utilization_offline":
        return {0:45, 1:22.5, 2: 18, 3: 15, 4: 12.85}

    elif campaign_name == "healthifymetmodd" and event_name == "sp_plan_purchase":
        return {0:31.66, 1:19, 2: 15.8, 3: 13.57}

    elif campaign_name == "mistplayearnmoneymodd" and event_name == "iap_spend_all_v2":
        return {0:90, 1:45}

    elif campaign_name == "yandexrealestateiosmodd" and event_name == "first_call_posle-paid_s2s":
        return {0:80, 1:30}

    elif campaign_name == "popaimodd" and event_name == "onPurchasesUpdated":
        return {0:90, 1:45, 2:30}

    elif campaign_name == "dominosturkeyauto" and event_name == "yfub50":

        # if offer_id in ["domdoummp", "dom2doummp"]:
        #     return {0:4, 1:2.85, 2:2.6}
        
        return {0:5, 1:2.85, 2:2.6} # need to update

    elif campaign_name == "wetterandroidauto" and event_name == "u6z21k" and offer_id:
        if offer_id.isdecimal():
            return {0:6, 1:4.2, 2:3}

        return {0:14, 1:9.5, 2:8}
    
    elif campaign_name == "btcturktauto" and event_name == "496w0o":
        if offer_id.isdecimal():
            return {0:2.5}
        
        return {1:14, 2:10}

    elif campaign_name == "rootcarinsurancemodd" and event_name == "Profile":
        return {0: 9, 1:7, 2: 6}

    elif campaign_name == "mcluckcasinoiosmodd" and event_name == 'first_purchase':
        return {0:75, 1:45}

    elif campaign_name == "eternzmodd" and event_name == 'First Purchase':
        return {0:14, 1:10, 2:8, 3:6}

    elif campaign_name == "dominoesgoldiosmodd" and event_name == "firstCashNPU":
        return {0:45, 1:23, 2: 18}
    
    elif campaign_name == "unodigitalbankiosmodd" and event_name == "loan_disbursed":
        return {0:90, 1:30, 2: 23}

    elif campaign_name == "loansonlinemodd" and event_name == "newloancount":
        return {0:90, 1:45, 2:30}

    elif campaign_name == "webzaimiosmodd" and event_name == "newloancount":
        return {0:90, 1:45, 2:30}

    elif campaign_name == "litresiosmodd" and event_name == 'af_purchase_success_ppd':
        return {0:22.5, 1:18, 2:15.5, 3:12.85}

    elif campaign_name == "shahidmodd" and event_name == "evergent_server_subscription_success":
        return {0:24, 1:16, 2:14, 3: 12}

    elif campaign_name == "shionauto" and event_name == "10000_revenue":
        from datetime import datetime
        today = datetime.now().weekday()
        if today in [0,4]:
            return {0:37}

    elif campaign_name == "bajajfinauto" and event_name == "Lead_PROL_DR":
        return {0:49, 1:24, 2:19}
    
    elif campaign_name == "bajajfinauto" and event_name == "Lead_PROL_CA":
        return {0:48, 1:23, 2:18}

    elif campaign_name == "maxfashionindiaauto" and event_name == "PURCHASE":
        return {0:24, 1:8.3, 2:7.5}

    elif campaign_name == "afriexaiosauto" and event_name == 'opawt9':
        return {0:45, 1:22, 2:15, 3:12}
    
    elif campaign_name == "pointsbetsportsbookmodd" and event_name == "Deposit Placed First Time":
        return {0:45, 1:22.5, 2:18}

    elif campaign_name == "burgerkingbrasilt2modd" and event_name == "af_purchase":
        return {0:9, 1:7.14}

    elif campaign_name == "sugarworldiosmodd" and event_name == "sale":
        return {0:25, 1:16.6}

    elif campaign_name == "neoniosmodd" and event_name == 'crd_pre_approved_stts':
        return {1:29, 2:18, 3:15, 4:14.3}

    elif campaign_name == "starzplayiosmodd" and event_name == "af_subscribe":
        return {0:45, 1:32}

    elif campaign_name == "ballmodd" and event_name == "ChallengeCompleted_1":
        return {0:18, 1:11.25, 2:9}
    
    elif campaign_name == "defactotauto" and event_name == "icmk9u":
        return {0:24, 1:14, 2: 12}
    
    elif campaign_name == "defactoiosauto" and event_name == "icmk9u":
        return {0:24, 1:14, 2: 12}
    
    elif campaign_name == "pulszcasinomodd" and event_name == "af_purchase_total_10_00":
        return {0:95, 1:48}
    
    elif campaign_name == "darknessmodd" and event_name == "revenue_1":
        return {0 : 47, 1: 30}

    elif campaign_name == "darknessmodd" and event_name == "revenue_5":
        return {0: 47, 1: 30 ,2:23}

    elif campaign_name == "darknessmodd" and event_name == "revenue_10":
        return {0: 87, 1:47}

    elif campaign_name == "darknessmodd" and event_name == "revenue_20":
        return {2:95}

        
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

        
        day_wise_stats = camp_wise_stats(campaign_name, event_name, channel, network, offer_id,Pay_out)

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
            # if required_timezone:
            #     event_details = EventInfoTZ.objects.filter(offer_serial=offer_serial, event_name=event_name, event_day__lte=event_day).values("event_count")
            # else:

            event_details = EventInfo.objects.filter(offer_serial=offer_serial, event_name=event_name, event_day__lte=event_day).values("event_count")

            total_event_count = sum((event['event_count'] for event in event_details))
           
            required_event_count = int(round(install_count / required_installs))
            is_eligible = total_event_count < required_event_count

            if required_events:
                from datetime import datetime
                today = datetime.now().strftime('%Y-%m-%d')
                # if required_timezone:
                #     completed_event_count = EventInfoTZ.objects.filter(offer_serial=offer_serial, event_name=event_name + "_done", created_at__gte=str(today)).values("event_count")
                # else:
                completed_event_count = EventInfo.objects.filter(offer_serial=offer_serial, event_name=event_name + "_done", created_at__gte=str(today)).values("event_count")
                completed_event_count = sum((event['event_count'] for event in completed_event_count))

                if completed_event_count >= required_events:
                    is_eligible = False

            if campaign_name == "underarmourauto":

                from datetime import datetime
                today = datetime.now().strftime('%Y-%m-%d')

                revenue_details = EventInfo.objects.filter(event_name=event_name, created_at__gte=str(today)).values("revenue")
                total_revenue = sum((event['revenue'] for event in revenue_details)) 

                print (total_revenue)     
                print (int(revenue))        

                if total_revenue + int(revenue) >= 27000:
                    is_eligible = False 
            
            if is_eligible and not track_only:
                # if required_timezone:
                #     event_details, created = EventInfoTZ.objects.get_or_create(campaign_name=campaign_name,offer_serial=install_details,event_name=event_name,event_day=event_day,defaults={"event_count": 1, "revenue": revenue})

                # else:
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

        
        day_wise_stats = camp_wise_stats(campaign_name, event_name, channel, network, offer_id)

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
                from datetime import datetime
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


class Compare_event_stats(APIView):
    def get(self, request):
        campaign_name = request.GET.get('campaign_name')
        event_name = request.GET.get("event_name")
        event_name_2 = request.GET.get("event_name_2")        
        event_day = request.GET.get("event_day")

        from datetime import datetime
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
