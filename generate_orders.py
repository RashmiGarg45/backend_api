import datetime
import json
import random
import sqlite3
import requests
from sqlite3 import Error
from bs4 import BeautifulSoup

def get_tracking_data(order_id):
	url = "https://ecomexpress.in/tracking/?awb_field="+ order_id
	resp = requests.get(url)
	html = resp.text
	soup = BeautifulSoup(html, "html.parser")
	output = soup.find_all("script")#, id_="__NUXT_DATA__")
	count = 0
	for s in output:
		count +=1 
		if count ==2:
			javascript_data = str(s)

	start_index = javascript_data.find('[')
	end_index = javascript_data.rfind(']')
	json_data = javascript_data[start_index:end_index + 1]
	parsed_data = json.loads(json_data)
	resp = {"orderid": "", "actual_weight":"", "origin": "", "Upload_Time": "", "status_remark": ""}
	for s in parsed_data:
		for key in resp:
			try:
				if key in s:
					val_index = s.get(key)
					resp[key] = parsed_data[val_index]
			except:
				pass

	resp["AWB"] = order_id
	return resp

def convert(date_time):
    format = '%d-%b-%Y %H:%M'
    datetime_str = datetime.datetime.strptime(date_time, format)
 
    return datetime_str

if __name__ == "__main__":

    conn = sqlite3.connect(".\db.sqlite3")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS TATAPALETTE")
    table = """ CREATE TABLE TATAPALETTE (
            serial INTEGER PRIMARY KEY AUTOINCREMENT,
            AWB VARCHAR(255) NOT NULL,
            OrderId VARCHAR(255) NOT NULL,
            ShipmentUploadTime DATETIME,
            ShipmentOrigin VARCHAR(255),
            ShipmentStatus VARCHAR(255),
            ShipmentWeight VARCHAR(255),
            OrderId_Status INTEGER DEFAULT 0
        ); """
    
    cursor.execute(table)

    exit()
    already_present_awbs = []
    current_awbs = []
    successful_awbs = []

    data=cursor.execute('''SELECT * FROM TATAPALETTE''') 
    for row in data: 
        already_present_awbs.append(str(row[0]))

    for j in range(1000):
        awb = "2073" + str(random.randint(100000, 999999))
        if awb not in already_present_awbs and awb not in current_awbs:
            resp = get_tracking_data(awb)
            if "bhiwandi" in resp.get("origin").lower() and len(resp.get("orderid"))==9 and resp.get("orderid").startswith("129"):
                successful_awbs.append(resp)				
            current_awbs.append(awb)

    for j in range(1000):
        awb = "7046" + str(random.randint(100000, 999999))
        if awb not in already_present_awbs and awb not in current_awbs:
            resp = get_tracking_data(awb)
            if "bhiwandi" in resp.get("origin").lower() and len(resp.get("orderid"))==9 and resp.get("orderid").startswith("129"):
                successful_awbs.append(resp)				
            current_awbs.append(awb)

    for resp in successful_awbs:
        print ("found")
        cursor.execute('''INSERT INTO TATAPALETTE (AWB, OrderId, ShipmentUploadTime, ShipmentOrigin, ShipmentStatus, ShipmentWeight, OrderId_Status)
                  VALUES ('{}', '{}', '{}', '{}', '{}', '{}', {})'''.format(
                      resp.get("AWB"),
                      resp.get("orderid"),
                      convert(resp.get("Upload_Time")),
                      resp.get("origin"),
                      resp.get("status_remark"),
                      resp.get("actual_weight"),
                      0 
                  ))
        conn.commit()

    output = []
    data=cursor.execute('''SELECT * FROM TATAPALETTE''') 
    for row in data: 
        print (list(row))
