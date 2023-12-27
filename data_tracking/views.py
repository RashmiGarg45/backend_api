import json
import array
from Crypto.Cipher import AES
from django.http import HttpResponse
from rest_framework.decorators import api_view

def pad(s):
	bs = AES.block_size
	return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)

@api_view(['POST', 'GET'])
def tracking(request, package_name, path):
    if request.body:
        d = json.loads(request.body)
        data = []
        for i in bytearray(d):

            if i > 127:
                data.append(-256+i)
            else:
                data.append(i)	

        key = [100, 45, -19, -50, 81, 127, -26, -20, -98, -35, -61, -99, -10, 78, 70, -83]
        val = data[-24::]
        iv = val[:16]
        key_new = array.array('b', key).tostring()
        iv_new = array.array('b', iv).tostring()
        cipher = AES.new(key_new, AES.MODE_CBC, iv_new )
        data = array.array('b', data).tostring()
        data = pad(data)	
        decrypted_text = cipher.decrypt( data )
        print (decrypted_text)

    return HttpResponse(json.dumps({"package_name": package_name, "path": path}))
