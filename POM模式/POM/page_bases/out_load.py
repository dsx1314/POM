import allure
from selenium.webdriver.common.by import By
from common_object.selenium_text import page_contains
from web_bases.base_page import WebPage
from time import sleep


class Out_load(WebPage):
    def __init__(self,driver):
        self.driver = driver

    car_chechang = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div[2]/div[1]/div/form/div[1]/div/section/div/div/div/div/input')

    car_choose = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[2]')

    car_guanli = (By.XPATH, '//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[2]/div')

    car_  = (By.XPATH, '//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[2]/ul/li[5]')

    button = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[2]/button[1]')

    input_car = (By.XPATH, '/html/body/div[3]/div[2]/div/section/main/div/div/div/form/div[1]/div/div/input')

    click_one_out = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[2]/div/div/div/input')

    click_two_out = (By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[2]')

    click_three_out = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[4]/div/div/div[1]/input')

    click_frou_out = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li')

    click_five_out = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[5]/div/div/div[1]/input')

    click_six_out = (By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul/li')

    click_seven_out = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[6]/div/div/div[1]/input')

    click_eight_out = (By.XPATH, '/html/body/div[6]/div[1]/div[1]/ul/li')

    click_nine_out = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[7]/div/label/span[1]/span')

    click_all_out = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[8]/div/button')

    click_check = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div[2]/div[1]/div/form/div[3]/div/button[1]')

    delete_chedao = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr[1]/td[12]/div/button[2]')

    delete_two = (By.XPATH, '/html/body/div[2]/div/div[3]/button[2]')

    def out_load(self,out_name):
        # self.click_loctor(self.car_guanli)
        self.click_loctor(self.car_)
        # self.click_loctor(self.car_chechang)
        # self.click_loctor(self.car_choose)
        # self.click_loctor(self.click_all_out)
        sleep(1)
        self.click_loctor(self.button)
        self.input_loctor(self.input_car,txt=out_name)
        self.click_loctor(self.click_one_out)
        self.click_loctor(self.click_two_out)
        self.click_loctor(self.click_three_out)
        self.click_loctor(self.click_frou_out)
        self.click_loctor(self.click_five_out)
        self.click_loctor(self.click_six_out)
        self.click_loctor(self.click_seven_out)
        self.click_loctor(self.click_eight_out)
        self.click_loctor(self.click_nine_out)
        self.click_loctor(self.click_all_out)
        self.click_loctor(self.click_check)
        self.wait(1)
        self.driver.get_screenshot_as_file('D:\\POM\\picture\\车道自动化测试-出口.png')
        allure.attach.file(r'D:\\POM\\picture\\车道自动化测试-出口.png', attachment_type=allure.attachment_type.PNG)
        self.wait(1)
        # 删除车道
        # self.click_loctor(self.delete_chedao)
        # self.click_loctor(self.delete_two)
        # self.waiting(1)
        # self.driver.get_screenshot_as_file('D:\\POM\\picture\\车道自动化测试-删除出口车道.png')
        # allure.attach.file(r'D:\\POM\\picture\\车道自动化测试-删除出口车道.png',attachment_type=allure.attachment_type.PNG)
        #
        # assert page_contains(self.driver,'删除成功'),'删除失败'
        # # self.waiting(2)
        # # self.quit()
