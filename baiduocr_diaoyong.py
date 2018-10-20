import base64
from urllib.parse import urlencode

import certifi
import urllib3

access_token= '24.b370b77d44c6757b8d3388d60170dfc7.2592000.1541983838.282335-14408430'
# http=urllib3.PoolManager()
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where()
)
url='https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token='+ access_token
f = open('code.jpg','rb')
#参数image：图像base64编码
img = base64.b64encode(f.read())
params={'image':img}
#对base64数据进行urlencode处理
params=urlencode(params)
request=http.request('POST',
                      url,
                      body=params,
                      headers={'Content-Type':'application/x-www-form-urlencoded'})
#对返回的byte字节进行处理。Python3输出位串，而不是可读的字符串，需要进行转换
result = str(request.data,'utf-8')
print(result)