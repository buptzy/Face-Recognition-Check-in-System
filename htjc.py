# encoding:utf-8
import urllib
import urllib,sys
from urllib.request import urlopen, Request
from urllib.parse import urlencode
import ssl
import base64
import  json

def pic_base64(image):
    with open(image, 'rb') as f:
        base64_data = base64.b64encode(f.read())
    return base64_data
def htjc():
    image_name = 'image/0.jpg'
    image_base64 = pic_base64(image_name)
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceverify"

    params_d = dict()
    params_d['image'] = str(image_base64, encoding='utf-8')
    params_d['image_type'] = 'BASE64'
    params_d['face_field'] = 'landmark'

    params = json.dumps([params_d]).encode('utf-8')
    access_token = '24.da4c56e6666de58f0efa972bab19ca21.2592000.1561884770.282335-15898427'#参考百度ai文档
    request_url = request_url + "?access_token=" + access_token
    request = Request(url=request_url, data=params)
    request.add_header('Content-Type', 'application/json')
    response = urlopen(request)
    content = response.read()
    if content:
         data = json.loads(content)
    return  data['result']['face_liveness']
