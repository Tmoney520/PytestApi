# -*- coding: utf-8 -*- 
"""          
# @Time   : 2023/2/25 19:16
# @Author :TGW
"""

from hashlib import md5

#MD5加密
def make_md5(arg, encoding='utf-8'):
    return md5(arg.encode(encoding)).hexdigest()
