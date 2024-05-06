from django.http import HttpResponse
import subprocess
import json
from subprocess import STDOUT, PIPE
import sqlite3
import random
import execjs
import datetime
import time
import mysql.connector as mysql
from rest_framework.decorators import api_view

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
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="123admin!", database="techteam")
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
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="123admin!", database="techteam")
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
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="123admin!", database="techteam")
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
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="123admin!", database="techteam")
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
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="123admin!", database="techteam")
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
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="123admin!", database="techteam")
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
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="123admin!", database="techteam")
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
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="123admin!", database="techteam")
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
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="123admin!", database="techteam")
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
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="123admin!", database="techteam")
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
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="123admin!", database="techteam")
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
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="123admin!", database="techteam")
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
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="123admin!", database="techteam")
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
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="123admin!", database="techteam")
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
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="123admin!", database="techteam")
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
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="123admin!", database="techteam")
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
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="123admin!", database="techteam")
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
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="123admin!", database="techteam")
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
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="123admin!", database="techteam")
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
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="123admin!", database="techteam")
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
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="123admin!", database="techteam")
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
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="123admin!", database="techteam")
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
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="123admin!", database="techteam")
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
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="123admin!", database="techteam")
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
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="123admin!", database="techteam")
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
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="123admin!", database="techteam")
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
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="123admin!", database="techteam")
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
    conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="123admin!", database="techteam")
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
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="123admin!", database="techteam")
        cursor = conn.cursor()  

        # current_date = datetime.datetime.fromtimestamp(time.time()).strftime("%d.%m.%Y")
        
        cursor.execute('''SELECT * FROM stylishop_orderId WHERE NOT isUsed=1 ORDER BY order_id ASC''')#AND order_date LIKE "{}" ORDER BY order_id ASC'''.format(current_date))
        data = cursor.fetchall()
        order_id = data[0][1]
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
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="123admin!", database="techteam")
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
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="123admin!", database="techteam")
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
        conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="123admin!", database="techteam")
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
