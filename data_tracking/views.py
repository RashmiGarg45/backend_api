import json
import array
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
from hashlib import pbkdf2_hmac
from django.http import HttpResponse
from rest_framework.decorators import api_view

# def pad(s):
#     bs = AES.block_size
#     s = str(s)
#     print ((bs - len(s) % bs) * chr(bs - len(s) % bs))
#     return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)

@api_view(['POST', 'GET'])
def tracking(request, package_name, path):
    import base64
    if request.body:
        d = request.body

        key = "R2PcxTzKKaWVyMakREG6X9".encode("utf-8")
        key = pbkdf2_hmac(hash_name='sha1', password=bytes(key), salt=bytearray([0] * 8), iterations=10000, dklen=16)
        cipher = AES.new(key, AES.MODE_CBC, iv=d[-24:-8])
        data = pad(d, 16)
        new_data = cipher.decrypt(data)#.replace('\n', '')

        print (new_data)

    return HttpResponse(json.dumps({"package_name": package_name, "path": path}))
