# -*- coding: utf-8 -*- 
"""          
# @Time : 2023/2/23 9:59
#  :TGW
"""
import allure
import pytest
import requests
from VAR.URL import login_api
from VAR.account import account_A


@pytest.fixture
def test_login():
    data = account_A
    url = login_api
    res = requests.post(url=url,json=data)
    token = res.json()['token']
    with allure.step('断言响应码'):
        assert '200' == res.json()['status']
    with allure.step('msg信息'):
        assert 'success' == res.json()['msg']
    return token
