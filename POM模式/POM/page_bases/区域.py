import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from web_bases.base_page import WebPage


class Quyu(WebPage):
    def __init__(self,driver):
        self.driver = driver

    # 大车场
    quyu = (By.XPATH, '//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[2]/ul/li[3]')

    xinzengquyu = (By.XPATH ,'//*[@id="my-master-app"]/div/section/section/main/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[2]/button[1]')

    input_name = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[1]/div/div/input')

    click_one = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[2]/div/div/div/input')

    click_two = (By.XPATH ,'/html/body/div[3]/div[1]/div[1]/ul/li[1]')

    click_three_input = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[3]/div/div/input')

    click_four_input = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[4]/div/div/input')

    click_five_input = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[5]/div/div/input')

    click_six_input = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[6]/div/div/input')

    click_seven_input = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[7]/div/div/input')

    click_eight_input = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[8]/div/div/input')

    all_button = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[9]/div/button')

    def quyu_(self,txt01,txt02,txt03,txt04,txt05,txt06,txt07):
        self.click_loctor(self.quyu)
        sleep(3)
        self.click_loctor(self.xinzengquyu)
        self.input_loctor(self.input_name,txt=txt01)
        self.click_loctor(self.click_one)
        self.click_loctor(self.click_two)
        self.input_loctor(self.click_three_input, txt=txt02)
        self.input_loctor(self.click_four_input, txt=txt03)
        self.input_loctor(self.click_five_input, txt=txt04)
        self.input_loctor(self.click_six_input, txt=txt05)
        self.input_loctor(self.click_seven_input, txt=txt06)
        self.input_loctor(self.click_eight_input, txt=txt07)
        self.click_loctor(self.all_button)
        sleep(1)
        self.exce_png('D:\\POM\\picture\\自动化测试区域.png')
        allure.attach.file(r'D:\\POM\\picture\\自动化测试区域.png',attachment_type=allure.attachment_type.PNG)