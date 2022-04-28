import allure
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

from web_bases.base_page import WebPage

class GangTing(WebPage):
    def __init__(self,driver):
        self.driver = driver

    # 车场管理元素
    car_guanli = (By.XPATH, '//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[2]/div')

    car_gangting  = (By.XPATH, '//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[2]/ul/li[2]')

    xinzeng_gangting = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[2]/button[1]')

    input_gangting = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[1]/div/div/input')

    input_beizhu = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[2]/div/div/textarea')

    button_all = (By.XPATH ,'/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[3]/div/button')

    def gangting(self,txt01,txt02):
        self.click_loctor(self.car_guanli)
        self.click_loctor(self.car_gangting)
        self.click_loctor(self.xinzeng_gangting)
        self.input_loctor(self.input_gangting,txt=txt01)
        self.input_loctor(self.input_beizhu,txt=txt02)
        self.click_loctor(self.button_all)
        sleep(1)
        self.exce_png('D:\\POM\\picture\\自动化测试岗亭.png')
        allure.attach.file(r'D:\\POM\\picture\\自动化测试岗亭.png',attachment_type=allure.attachment_type.PNG)