from scrapy import signals
# from urllib import request
import random
from job1 import settings
import base64

# class AuthRandomProxy(object):
#     def process_request(self,request,spider):
#         proxy = random.choice(settings.AUTH_PRXIES)
#         auth = base64.b64encode(bytes(proxy['auth'],'utf-8'))
#         request.headers['Proxy-Authorization'] = b'Basic ' + auth
#         # request.headers['proxies-Auththorization'] = b'Basic'+ base64.b64encode(bytes(proxy['auth'],'utf-8'))
#         request.meta['proxy'] = 'http://'+proxy['host']
# from utils import get_proxy

from job1.utils import get_proxy

class RandomProxy(object):
    def process_request(self,request,spider):
        m = get_proxy.getproxy()
        host = str(m[0]) + ":" + str(m[1])
        print(m)
        # proxy = random.choice(settings.PROXIES)
        # print(proxy)
        # request.meta['proxy'] = 'http://'+proxy['host']
        request.meta['proxy'] = 'http://'+host

