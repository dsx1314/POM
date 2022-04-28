import allure
from selenium.webdriver.common.by import By

from web_bases.base_page import WebPage
from time import sleep

class MonthCar(WebPage):
    def __init__(self,driver):
        self.driver = driver


    car_guanli = (By.XPATH, '//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[7]/div')

    month_car = (By.XPATH, '//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[7]/ul/li[2]')

    button = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div[2]/div[2]/div/form/div/div/button[1]')

    input_name = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div[2]/form/div[1]/div[2]/div/div[1]/div/div/input')

    input_carnumber = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div[2]/form/div[1]/div[2]/div/div[2]/div/div/input')

    chose_car_click = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div[2]/form/div[1]/div[2]/div/div[3]/div/div/div/input')

    chose_car_agin_click = (By.XPATH, '//span[contains(text(),"月租车A")]')

    chedao_click = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div[2]/form/div[2]/div[2]/div/div[1]/div/div/span/span/div/div/div[2]/input')

    chedao_click_two = (By.XPATH, '//*[@role="tooltip"]/div[1]/div[2]/div[1]/div/label/span/span')

    month_click = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div[2]/form/div[2]/div[2]/div/div[2]/div/div/div/input')

    month_click_two = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[1]')

    money_input = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div[2]/form/div[2]/div[2]/div/div[3]/div/div[1]/input')

    cheweishu_input = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div[2]/form/div[2]/div[2]/div/div[5]/div/div/input')

    cheweishu_two_input = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div[2]/form/div[2]/div[2]/div/div[6]/div/div/input')

    all_button = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div[2]/form/div[2]/div[2]/div/div[7]/div/button[1]')

    def new_monthcar(self,txt01,txt02,txt03,txt04,txt05):
        self.click_loctor(self.car_guanli)
        self.click_loctor(self.month_car)
        sleep(5)
        self.click_loctor(self.button)
        self.input_loctor(self.input_name,txt=txt01)
        self.input_loctor(self.input_carnumber,txt=txt02)
        self.click_loctor(self.chose_car_click)
        sleep(3)
        self.click_loctor(self.chose_car_agin_click)
        self.click_loctor(self.chedao_click)
        self.click_loctor(self.chedao_click_two)
        sleep(1)
        self.click_loctor(self.chedao_click)
        self.click_loctor(self.month_click)
        self.click_loctor(self.month_click_two)
        self.input_loctor(self.money_input, txt=txt03)
        self.input_loctor(self.cheweishu_input, txt=txt04)
        self.input_loctor(self.cheweishu_two_input, txt=txt05)
        self.click_loctor(self.all_button)
        sleep(3)
        self.exce_png('D:\\POM\\picture\\自动化测试新增月租车.png')
        allure.attach.file(r'D:\\POM\\picture\\自动化测试新增月租车.png',attachment_type=allure.attachment_type.PNG)