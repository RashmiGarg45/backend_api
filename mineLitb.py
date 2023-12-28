import requests
import json,random,datetime,time
import os,time

import boto3
import time
from decimal import Decimal
import os
import json,random
import base64
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr


dynamodb = boto3.resource("dynamodb",aws_access_key_id='AKIA4W2ZSO7TZXX7XRD6',aws_secret_access_key='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',region_name='us-east-1')
table = dynamodb.Table('lightintheboxmodd')

def getorderid(id_,status):
	url = 'https://gw.lightinthebox.com/newv/en/user/ajax_customer_service?order_id={}&order_status={}'.format(id_,status)
	cookie_list = [
    			"ci-session=meb93brtse1ahsb4aah9k3bf7o",
				"first_visit=1703669895",
				"sid=254C6BBC-28DD-DC21-D893-3AF5BC81DB09",
				"vela_w=658BF0875347E",
				"vela_w_c=36",
				"vela_m=658BF08753495",
				"vela_m_c=36",
				"local=en%7CIN%7CINR",
				"__cust=AAAAAGWL8IdXN8oSB2wnAg==",
				"SRV=A_202312151000",
				"ci-vtimes=a%3A2%3A%7Bs%3A5%3A%22count%22%3Bi%3A2%3Bs%3A4%3A%22time%22%3Bi%3A1703755038%3B%7D",
				"ci-ppv=a%3A2%3A%7Bs%3A5%3A%22count%22%3Bi%3A0%3Bs%3A4%3A%22time%22%3Bi%3A1703755038%3B%7D",
				"vela_s=658D3D1E07DDF",
				"vela_s_c=10",
				"vela_v=658D3D1E08A1E",
				"vela_v_c=10",
				"vela_device=desktop",
				"vela_is_first_visit=1",
				"vtime=1%2C1703755058",
				"feature=V1219567_A",
				"PIM-SESSION-ID=scH3zYuKTGjRlAfH",
				"AKA-WWW-LITB-ORIGIN=US",
				"_gcl_au=1.1.468496671.1703755061",
				"_gid=GA1.2.1295947995.1703755062",
				"akacd_PIM-prd_ah_rollout=3881207860~rv=11~id=1b098608569beb139eb53f32487e66d3",
				"_pin_unauth=dWlkPVltSTBaR1EyWVRrdFkyWmlOaTAwWldaaUxUaGlPVFF0TVdWak56RXdOMll3TVRJeg",
				"__rub_uid=uid-38dc4ddb9.2609faea0.26889360b",
				"_mk_sync=1703765873882",
				"lls=4",
				"customer_first_name=",
				"customer_id=FOEVSMUpNN0FGOExWNEpJM0ZXN1JPOUtaZ",
				"customer_email=FZERZZU5HZVlHcFVLZVJMc01aaFBOQFVSYVhFcEhGcE9Pc1hBdU9TY1NTY1FYZUpMc01Xc09Sb1NVcllSLk1UY1BMb0tEbVNXY",
				"sessionKey=db2da503e5f70a3979fb10e6290c1462",
				"ppv=0%2C1703755079",
				"__rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22db2da503e5f70a3979fb10e6290c1462%22%7D",
				"_uetsid=f5214310a56111ee918bff0e4c29b06c",
				"_uetvid=7bc79090860911ee986b8fd01941c6e5",
				"_ga=GA1.1.1522027886.1703755062",
				"uid=mk57ba84fb-bfc8-486c-80fb-08694b40d4e1",
				"_ga_H41KJ9GF94=GS1.1.1703755061.1.1.1703755082.0.0.0",
			]
	cookie_string = ";".join(cookie_list)
	headers = {
				"cache-control": "max-age=0",
				"sec-ch-ua": '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
				"sec-ch-ua-mobile": "?0",
				"sec-ch-ua-platform": '"macOS"',
				"upgrade-insecure-requests": "1",
				"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
				"sec-fetch-site": "none",
				"sec-fetch-mode": "navigate",
				"sec-fetch-user": "?1",
				"sec-fetch-dest": "document",
				"accept-encoding": "gzip, deflate, br",
				"accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
				"Cookie":cookie_string
				
    }
	resp = requests.get(url=url,headers=headers)
	print(resp.json())
	return resp

orderid = 76320064
while True:
	orderid+=1
	for status in [23]:
		try:
			if getorderid(orderid,status).json().get('success'):
				dict_={
					'orderid':str(orderid),
					'date_added':str(datetime.datetime.now().date()),
					'order_status':status,
					'used':False
				}
				print(dict_)
				table.put_item(Item=dict_)
				print('Item : {} inserted'.format(orderid))
		except:
			pass
		    