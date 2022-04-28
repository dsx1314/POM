import allure
from selenium import webdriver
# from common_object.driver_page import BaseTestCase
from common_object.clear import del_file
from common_object.name_all import get_name
from common_object.random_demo import rand_str
from common_object.read_excel import read_xlsx
from common_object.修改excel import remove
from common_object.读取txt import read_txt
from common_object.车牌号码02 import get_number
from page_bases.login_object import LoginPage
from page_bases.out_load_two import Out_load_two
from page_bases.导入车辆 import InMonthcar
from page_bases.月租车 import MonthCar
from web_bases.base_page import WebPage
import pytest
from page_bases.in_load import CarPage
from page_bases.out_load import Out_load
from page_bases.stop_list import StopList
from time import sleep
from common_object.selenium_text import page_contains
from page_bases.岗亭 import GangTing
from page_bases.区域 import Quyu
from page_bases.设备 import Shebei
from common_object.车牌号码 import get_car_number


# @allure.story('停车列表')
class TestLogin:
    car_list ,ids_value= read_xlsx('D:\\POM\\data\\车场列表用例.xlsx', 'CarList')

    # @allure.story('车道管理')
    # @allure.title('车道管理用例')
    def setup_class(self):
        get_number()
        sleep(2)
        read_txt()
        sleep(2)
        remove()
        get_name()
        get_car_number()
        del_file(r'D:\POM\picture')
        self.driver = webdriver.Chrome()
        login_page = LoginPage(self.driver)
        login_page.login(username='63010623',password='13202029682')

    def teardown_class(self):
        sleep(3)
        self.driver.quit()

    @allure.story('停车列表')
    @allure.title('停车列表用例')
    @allure.testcase('http://www.baidu.com',name='百度')
    @pytest.mark.parametrize(argnames='carlist',argvalues=car_list,ids=ids_value)
    def test_a_01(self,carlist):
        stop_list = StopList(self.driver)
        stop_list.car_list_all(name=carlist)
        sleep(3)

    @allure.story('车场岗亭')
    @allure.title('新增岗亭')
    def test_a_02(self):
        gangting_ = GangTing(self.driver)
        gangting_.gangting(txt01='自动化测试—岗亭'+rand_str(),txt02='自动化测试岗亭备注')
        assert page_contains(self.driver,'自动化测试—岗亭'), '新增岗亭失败'
        sleep(3)

    @allure.story('车场区域')
    @allure.title('大车场区域')
    def test_b(self):
        quyu_xinzeng = Quyu(self.driver)
        quyu_xinzeng.quyu_(txt01='自动化测试区域'+rand_str(),txt02='1000',txt03='1000',txt04='100',txt05='100',txt06='900',txt07='900')
        assert page_contains(self.driver,'自动化测试区域'), '新增区域失败'
        sleep(3)



    @allure.story('车场设备')
    @allure.title('M款设备')
    def test_c(self):
        new_shebei = Shebei(self.driver)
        new_shebei.sehbei_m(txt01='自动化'+rand_str(),txt02=rand_str(),txt03='192.168.35.1')
        assert page_contains(self.driver,'操作成功'),'操作失败'
        sleep(3)






    # 车道自动化测试
    @allure.story('车道新增')
    @allure.title('车道新增测试用例')
    def test_d(self):
        out_load_page = Out_load(self.driver)
        out_load_page.out_load(out_name='自动化出口-1'+rand_str())
        sleep(3)


    # 月租车新增自动化测试
    @allure.story('月租车')
    @allure.title('月租车新增测试用例')
    def test_e(self):
        month_ = MonthCar(self.driver)
        month_.new_monthcar(txt01=get_name(),txt02=get_car_number(),txt03='100',txt04='1',txt05='1')
        sleep(3)


    # 月租车导入
    @allure.story('月租车导入')
    @allure.title('月租车导入用例')
    def test_f(self):
        daoru = InMonthcar(self.driver)
        daoru.in_month_car(txt='D:\\POM\\data\\车辆导入模板 (6).xls')
        sleep(3)


















    #失败用例
    # def test_dar(self):
    #     out_two = Out_load_two(self.driver)
    #     out_two.out_load_02(out_name_two='自动化出口-2')
    #     assert page_contains(self.driver,'请选择相机设备'), '已选择相机'


    # def test_object_02(self):
    #     self.driver = webdriver.Chrome()
    #     login_page = LoginPage(self.driver)
    #     login_page.login(username='',password='13202029682')
    #
    # def test_object_03(self):
    #     self.driver = webdriver.Chrome()
    #     login_page = LoginPage(self.driver)
    #     login_page.login(username='63010623',password='')


