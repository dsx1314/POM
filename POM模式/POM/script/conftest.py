# from selenium import webdriver
# import pytest
# from page_bases.login_object import LoginPage
# from web_bases.base_page import WebPage
# from time import sleep
#
#
#
# # class First:
# @pytest.fixture(scope='function',autouse=True)
# def first_login(self=None):
#     driver = webdriver.Chrome()
#     login_page = LoginPage(driver)
#     login_page.login(username='63010623', password='13202029682')
#     yield driver
#     sleep(3)
#     self.driver.quit()
from typing import List
import pytest
import sys
sys.dont_write_bytecode = True
from common_object.clear import del_file






# 设置控制避免乱码
def pytest_collection_modifyitems(session: "Session", config: "Config", items: List["Item"]) -> None:
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")
