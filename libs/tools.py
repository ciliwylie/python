import requests
import unittest
class RequestHttp(object):
    host = 'http://localhost'

    def requestData(self,method,url,body,*args,**kwargs):
        req_url = '{}{}'.format(self.host, url)
        if method=='post':
            result=requests.request(method=method,url=req_url,data=body, *args, **kwargs)
        elif method=='get':
            result = requests.request(method=method, url=req_url, params=body, *args, **kwargs)
        return result

class verifyClass(unittest.TestCase):
    #校验状态码
    def verifyStatus_code(self,result,v_code):
        self.assertEqual(result.status_code,v_code)
    #校验某个json字段
    def verifyKey(self,result,key,value):
        #将json字段转为字典放在result中
        result=result.json()
        #寻找字典中key的值，未找到则返回None
        v=result.get(key,None)
        self.assertEqual(v,value)
    #校验html某个字段
    def verifyhtml(self,result,key):
        result=result.text
        self.assertEqual(result,key)





