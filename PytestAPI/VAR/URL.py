# -*- coding: utf-8 -*- 
"""          
# @Time   : 2023/2/23 11:10
# @Author :TGW
"""

from VAR.IP import sit_IP

#手动改环境
ipNumber = sit_IP

#登录接口地址
login_api=ipNumber + '/login'

#搜索商品地址
search_api=ipNumber + '/search'

#下单接口地址
order_api=ipNumber + '/order'