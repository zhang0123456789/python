#encoding=utf-8
__author__ = 'Administrator'
'''
@Time:2018-12-2 16:37
'''
import requests

class HttpRequests:
    def httprequests(self,http_url,param,http_method,cookie=None):
        # session_id=requests.session()
        if http_method=="get":
            # res=session_id.get(http_url,params=param,cookies=cookie)
            res=requests.get(http_url,param,cookies=cookie)
        else:
            # res=session_id.get(http_url,params=param,cookies=cookie)
            res=requests.post(http_url,param,cookies=cookie)
        return res
