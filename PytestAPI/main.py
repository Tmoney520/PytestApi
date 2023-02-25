# -*- coding: utf-8 -*- 
"""          
# @Time : 2023/2/23 8:51
#  :TGW
"""
import os
import pytest

def run():
    pytest.main(['-v','--alluredir','./report/result','--clean-alluredir'])
    os.system('allure generate ./report/result/ -o ./report/report_api/ --clean')

if __name__ == '__main__':
    run()
    print(__file__)


