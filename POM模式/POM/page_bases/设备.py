import allure
from selenium.webdriver.common.by import By

from web_bases.base_page import WebPage
from time import sleep

class Shebei(WebPage):
    def __init__(self,driver):
        self.driver = driver


    shebei = (By.XPATH, '//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[2]/ul/li[4]')

    xinzeng_shebei = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[2]/button[1]')

    input_name_one = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[1]/div/div/input')

    click_one = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[2]/div/div/div/input')

    click_two = (By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[1]')

    click_three_input = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[3]/div/div/input')

    click_four = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[4]/div/div/div/input')

    click_five = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[1]')

    click_six = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[5]/div/div/div/input')

    click_seven = (By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul/li[1]')

    input_name_two = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[6]/div/div/input')

    all_button = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[7]/div/button')

    def sehbei_m(self,txt01,txt02,txt03):
        self.click_loctor(self.shebei)
        sleep(1)
        self.click_loctor(self.xinzeng_shebei)
        self.input_loctor(self.input_name_one,txt=txt01)
        self.click_loctor(self.click_one)
        self.click_loctor(self.click_two)
        self.input_loctor(self.click_three_input,txt=txt02)
        self.click_loctor(self.click_four)
        self.click_loctor(self.click_five)
        self.click_loctor(self.click_six)
        self.click_loctor(self.click_seven)
        self.input_loctor(self.input_name_two,txt=txt03)
        self.click_loctor(self.all_button)
        sleep(1)
        self.exce_png('D:\\POM\\picture\\自动化测试设备.png')
        allure.attach.file(r'D:\\POM\\picture\\自动化测试设备.png',attachment_type=allure.attachment_type.PNG)