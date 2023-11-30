from django.http import HttpResponse
import subprocess
import json
from subprocess import STDOUT, PIPE
import sqlite3

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
    
    data = cursor.execute('''SELECT * FROM TATAPALETTE WHERE NOT OrderId_Status=1 ORDER BY ShipmentUploadTime DESC, OrderId ASC''')
    order_id = "-1"
    for row in data:
        order_id = row[2]
        if request_type != "test":
            cursor.execute('UPDATE TATAPALETTE SET OrderId_Status=1 WHERE serial={}'.format(row[0]))  
            conn.commit()
        break
    return HttpResponse(order_id)

def get_available_orders_count(request):
    conn = sqlite3.connect(r".\db.sqlite3")
    cursor = conn.cursor()    
    
    data = cursor.execute('''SELECT COUNT(*) FROM TATAPALETTE WHERE NOT OrderId_Status=1''')
    count = "-1"
    for row in data:
        count = row[0]
        break
    return HttpResponse(count)