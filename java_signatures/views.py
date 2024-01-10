from django.http import HttpResponse
import subprocess
import json
from subprocess import STDOUT, PIPE
import sqlite3
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
    conn = sqlite3.connect(r".\db.sqlite3")
    cursor = conn.cursor()    
    request_data = json.loads(request.body)
    request_type = request_data.get("request_type")
    
    data = cursor.execute('''SELECT * FROM tatapalette_orderIds WHERE NOT OrderId_Status=1 ORDER BY ShipmentUploadTime DESC, OrderId ASC''')
    order_id = "-1"
    for row in data:
        order_id = row[2]
        if request_type != "test":
            cursor.execute('UPDATE tatapalette_orderIds SET OrderId_Status=1 WHERE OrderId={}'.format(order_id))  
            conn.commit()
        break
    return HttpResponse(order_id)

def get_available_orders_count(request):
    conn = sqlite3.connect(r".\db.sqlite3")
    cursor = conn.cursor()    
    
    data = cursor.execute('''SELECT COUNT(DISTINCT OrderId) FROM tatapalette_orderIds WHERE NOT OrderId_Status=1''')
    count = "-1"
    for row in data:
        count = row[0]
        break
    return HttpResponse(count)

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
        
        cursor.execute('''SELECT * FROM zalora_orderIds WHERE NOT isUsed=1 AND country ="{}" ORDER BY order_id ASC'''.format(country))
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

def cipher(decrypted_text=None,encrypted_text=None):
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
    
    key = "iGvRAL5CpW4cp#LCDF2T"
    
    if encrypted_text:
        # encrypted_text = "U2FsdGVkX18XhGeLwLLRzruAHaVzBtzCwKhCaONA6H4+LRIW8qbr1f2UkGQaFhbFTZWyp5RX8M4t5rsEpbMKBQ9lMHy+z88oXYePL2KeaUaSF2zcHK9lRWgMEoebcRg4vme5/aE98V3N9P1Gys00VYKl01jYxd7cYLn3mdz4iEy9LiobAMpXAQHBvpmmdPqfsKEnbpPD09QJrBKLwUZVhSDiUFjoV4lhD/6uH9uAwwQaX9ubzsC4yoet9A/nKSUIsm/mWpPj/uV06sAolSPFkjmOYKxJgB6U2aCaE4aXL8zcSkfCVjaTNvRs8KJ01uA36RY0VCu7EXaNutaehVt5NldqiZDCviI2X2Ggovn74/qfTQ0APiIJgli095UDd6AhS8N010F4dWxTOZuufBeXn1niAhHALTmtpcrsEMqT0yM1Vs+lzyvEoti7bB5YxPF+b7kAQgL64I6hEtHiAuBSIw=="
        decrypted_text = ctx.call('module.exports.decrypt', encrypted_text, key)
        print(decrypted_text)

    if decrypted_text:
        # decrypted_text='{"carrinho_id":"96173802","forma_pagamento":"offline","deviceData":null,"dinheiro":0,"forma_pagamento_offline":"5","observacoes":"","latitude":null,"longitude":null,"dispositivo":{"dispositivo":"03c7d8269e2a41f8","plataforma":"Android","modelo":"Redmi K20 Pro","versao_app":"3.1.4","versao":"10"},"pagamento_via_pix":false}'
        encrypted_text=decrypted_text = ctx.call('module.exports.encrypt', decrypted_text, key)
        # print(encrypted_text)
        
def ragazzo_signature(request):
    data = json.loads(request.body)
    encrypted_string = data.get("encrypted_string")
    decrypted_string = data.get("decrypted_string")

    # try:       
    if encrypted_string:
        output = cipher(encrypted_text=encrypted_string)
    if decrypted_string:
        output = json.dumps(cipher(decrypted_text=decrypted_string))

    response_code = 200
    message = "success"

    # except Exception as e:
    #     response_code = 500
    #     message = str(e)
    #     output = ""

    return HttpResponse(json.dumps({"response_code": response_code, "message": message, "data": output}))
