import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from web_bases.base_page import WebPage

class InMonthcar(WebPage):
    def __init__(self,driver):
        self.driver = driver


    button_first = (By.XPATH, '//span[contains(text(),"导入")]')

    input_xlsx = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/div/div[1]/input')


    def in_month_car(self,txt):
        self.click_loctor(self.button_first)
        self.input_loctor(self.input_xlsx,txt=txt)
        self.wait(10)
        self.exce_png('D:\\POM\\picture\\月租车导入.png')
        allure.attach.file(r'D:\\POM\\picture\\月租车导入.png',attachment_type=allure.attachment_type.PNG)