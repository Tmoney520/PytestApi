# -*- coding: utf-8 -*- 
"""          
# @Time : 2023/2/23 8:06
# @Author :TGW
"""


import requests
class HttpClient:
    # 只要用post,get请求方式 就创建会话
    def __init__(self):
        self.session=requests.session()

    # 发送请求  请求方式，接口地址 ，接口数据(data)，接口参数类型(param_type)，头部信息,其他的信息
    # 判断 你要发送的是请求方式 如果get post
    # post请求参数类型 json data
    def send_request(self,method,url,data=None,param_type='json',**kwargs):
        if method=='get':
            response=self.session.request(method=method,url=url,params=data,**kwargs)
        elif method=='post':
            if param_type=='json':
                response=self.session.request(method=method,url=url,json=data,**kwargs)
            else:
                response=self.session.request(method=method,url=url,data=data,**kwargs)
        elif method=='delete':
            if param_type=='json':
                response=self.session.request(method=method,url=url,json=data,**kwargs)
            else:
                response=self.session.request(method=method,url=url,data=data,**kwargs)
        elif method=='put':
            if param_type=='json':
                response=self.session.request(method=method,url=url,json=data,**kwargs)
            else:
                response=self.session.request(method=method,url=url,data=data,**kwargs)
        else:
            raise ValueError
        return response

    # 实例化类 HttpClient().send_request()
    # a=HttpClient()
    def __call__(self,method,url,data=None,param_type='json',**kwargs):
        return self.send_request(method,url,data,param_type,**kwargs)

    def close_session(self):
        self.session.close()