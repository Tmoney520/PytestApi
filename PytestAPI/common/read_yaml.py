# -*- coding: utf-8 -*- 
"""          
# @Time : 2023/2/23 8:45
# @Author :TGW
"""
import yaml


def read_yaml(file):
    with open(file,encoding='utf-8') as f:
        data = yaml.load(f,yaml.FullLoader)
    return data
