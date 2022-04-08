import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.common_findelemen import Driver
from base.baseTestCase import BaseTestCase
from page_object.login_object import LoginPage
from  page_object.Search_object import SearchObject

class TestLogin(BaseTestCase):

    def test_login(self):
        po_login = LoginPage(self.driver)
        po_login.open()
        po_login.input_name('63010623')
        po_login.input_pwd('13202029682')
        po_login.click_button()
        # 断言
        txt = po_login.get_text()
        print(txt)
        self.assertEqual("车场管理",po_login.get_text())
        sleep(2)

        # 订单管理——临停订单
        po_search = SearchObject(self.driver)
        po_search.dingdan_click()
        po_search.linting_click()
        sleep(2)
        po_search.chechang_click()
        # sleep(2)
        po_search.choose_chang()
        # po_search.carnumber_input('贵VGCWXU')
        # sleep(1)
        po_search.date_input()
        po_search.date_txt_demo()
        po_search.date_txt_input('2022-01-01')
        po_search.date_click()
        sleep(1)
        po_search.carnumber_input('贵VGCWXU')
        po_search.zhankai()
        po_search.quyu_click()
        sleep(1)
        po_search.quyu_button()
        po_search.zhifuchangjing()
        sleep(1)
        po_search.chose_chajing()
        sleep(1)
        po_search.zhifushi_button()
        sleep(1)
        po_search.chose_zhifushi()
        po_search.zhaungtai_button()
        sleep(1)
        po_search.chose_zhuang()
        po_search.dingdanzhaungtai()
        po_search.chose_kaipiao_demo()
        po_search.qudao_click()
        po_search.qudaochoose()
        po_search.pay_fenlei()
        po_search.pay_click()
        po_search.chaxun_click()

        sleep(2)
        txt_dingdan = po_search.get_text_linting()
        print(txt_dingdan)
        self.assertEqual("10.00",po_search.get_text_linting())
#           切换窗口
    def test_login_02(self):
        po_login = LoginPage(self.driver)
        po_login.open()
        po_login.input_name('63010623')
        po_login.input_pwd('13202029682')
        po_login.click_button()
        # 断言
        txt = po_login.get_text()
        print(txt)
        self.assertEqual("车场管理",po_login.get_text())
        sleep(2)

        # 订单管理——临停订单
        po_search = SearchObject(self.driver)
        po_search.dingdan_click()
        po_search.linting_click()
        sleep(2)
        po_search.chechang_click()
        # sleep(2)
        po_search.choose_chang()
        # po_search.carnumber_input('贵VGCWXU')
        # sleep(1)
        po_search.date_input()
        po_search.date_txt_demo()
        po_search.date_txt_input('2022-01-01')
        po_search.date_click()
        sleep(1)
        # po_search.carnumber_input('贵VGCWXU')
        po_search.zhankai()
        po_search.quyu_click()
        sleep(1)
        po_search.quyu_button()
        po_search.zhifuchangjing()
        sleep(1)
        po_search.chose_chajing()
        sleep(1)
        po_search.zhifushi_button()
        sleep(1)
        po_search.chose_zhifushi()
        po_search.zhaungtai_button()
        sleep(1)
        po_search.chose_zhuang()
        po_search.dingdanzhaungtai()
        po_search.chose_kaipiao_demo()
        po_search.qudao_click()
        po_search.qudaochoose()
        po_search.pay_fenlei()
        po_search.pay_click()
        po_search.chaxun_click()

        sleep(2)

if __name__ == '__main__':
    unittest.main()