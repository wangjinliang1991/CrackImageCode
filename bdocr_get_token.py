import urllib3,base64,certifi
from urllib.parse import urlencode

# 获取access_token,证书认证
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where()
)
# http=urllib3.PoolManager()
request=http.request('POST',
                        'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=FrkXesqdodXNpmFxgltdp7Ch&client_secret=ul4iU4pZW19a4WTnFf8Lq7TBOXpI975X'
                    )
print(request.data)

