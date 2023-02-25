# -*- coding: utf-8 -*- 
"""          
# @Time : 2023/2/23 10:39
#  :TGW
"""
import allure
import pytest

from VAR.URL import search_api, order_api
from common.send_request import HttpClient


class Test_Api:
    HttpClient = HttpClient()
    price = None
    @allure.story('订单模块')
    @allure.title('搜索商品接口')
    def test_search(self,test_login):
        token = test_login
        data = {"token":token,"goods":"苹果手机"}
        url = search_api
        res = Test_Api.HttpClient(method='post',url=url,data=data)
        Test_Api.price = res.json()['price']
        print(res.json())
        with allure.step('断言响应码'):
            assert '200' == res.json()['status']
        with allure.step('断言信息'):
            assert 'success' == res.json()['msg']

    @allure.story('订单模块')
    @allure.title('下单接口')
    def test_order(self):
        data = {"price": Test_Api.price}
        url = order_api
        res = Test_Api.HttpClient(method='post',url=url,data=data)
        print(res.json())
        with allure.step('断言响应码'):
            assert '200' == res.json()['status']
        with allure.step('断言结果'):
            assert '下单成功' in res.json()['msg']

