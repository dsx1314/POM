import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

from web_bases.base_page import WebPage


class StopList(WebPage):
    def __init__(self,driver):
        self.driver = driver

    car_guanli = (By.XPATH, '//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[2]/div')

    car_list = (By.XPATH, '//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[2]/ul/li[1]')

    car_list_input = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[1]/div/div/input')

    chose = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[2]/div/div/div[1]/input')

    chose_two = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[1]')

    check = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[3]/div/button[1]')

    def car_list_all(self,name):
        self.click_loctor(self.car_guanli)
        self.click_loctor(self.car_list)
        self.clear_input(self.car_list_input)
        self.input_loctor(self.car_list_input,name)
        self.click_loctor(self.chose)
        self.click_loctor(self.chose_two)
        self.click_loctor(self.check)
        self.wait(1)
        self.driver.get_screenshot_as_file('D:\\POM\\picture\\查询车场列表.png')
        allure.attach.file(r'D:\\POM\\picture\\查询车场列表.png', attachment_type=allure.attachment_type.PNG)
