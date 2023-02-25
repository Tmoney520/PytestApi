# -*- coding: utf-8 -*- 
"""          
# @Time   : 2023/2/21 22:10
# @Author :TGW
"""

import random
from flask import Flask, request, jsonify

str = ""
for i in range(18):
    ch = chr(random.randrange(ord('0'), ord('9') + 1))
    str += ch
token = str

#实例化flask
app = Flask(__name__)

#创建路由
@app.route('/login',methods=['get','post'])
def login_api():
    """
    登录接口
    :return:
    """
    data = request.get_json()
    if data['username'] == 'tgw' and data['password']=='666':
        return jsonify({"msg":"success","status":"200","token":token})
    else:
        return jsonify({"msg":"用户名或密码错误","code":"001"})


@app.route('/search',methods=['get','post'])
def search_api():
    """
    搜索商品接口
    :return:
    """
    data = request.get_json()
    if data['token'] == token:
        if data['goods'] == '苹果手机':
            return jsonify({"msg":"success","status":"200","price": "5999"})
        elif data['goods'] == '华为手机':
            return jsonify({"msg":"success","status":"200","price": "4999"})
        else:
            return jsonify({"msg": "无此商品", "code": "001"})
    else:
        return jsonify({"msg":"请登录，否则无法购买商品","code":"001"})

@app.route('/order',methods=['get','post'])
def order_api():
    """
    下单接口
    :return:
    """
    data = request.get_json()
    if data['price'] == '5999':
        return jsonify({"msg":"苹果手机下单成功","status":"200"})
    elif data['price'] == '4999':
        return jsonify({"msg":"华为手机下单成功","status":"200"})
    else:
        return jsonify({"msg":"只有苹果和华为卖，请重新搜索商品","code":"001"})

if __name__ == '__main__':
    app.run('127.6.6.6',debug=True)