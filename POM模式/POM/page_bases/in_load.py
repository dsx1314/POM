import allure
from selenium.webdriver.common.by import By

from web_bases.base_page import WebPage

class CarPage(WebPage):
    def __init__(self,driver):
        self.driver = driver

    car_guanli = (By.XPATH, '//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[2]/div')

    car_  = (By.XPATH, '//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[2]/ul/li[5]')

    button = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/button[1]')

    input_car = (By.XPATH, '/html/body/div[3]/div[2]/div/section/main/div/div/div/form/div[1]/div/div/input')

    # 入口车道

    click_one = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[2]/div/div/div/input')

    click_two = (By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[1]')

    click_three = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[4]/div/div/div[1]/input')

    click_frou = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[1]')

    click_five = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[5]/div/div/div[1]/input')

    click_six = (By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul/li')

    click_seven = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[6]/div/div/div[1]/input')

    click_eight = (By.XPATH, '/html/body/div[6]/div[1]/div[1]/ul/li')

    click_nine = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[7]/div/label/span[1]/span')

    click_all = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[8]/div/button')


    # 出口车道
    click_one_out = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[2]/div/div/div/input')

    click_two_out = (By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[1]')

    click_three_out = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[4]/div/div/div[1]/input')

    click_frou_out = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[1]')

    click_five_out = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[5]/div/div/div[1]/input')

    click_six_out = (By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul/li')

    click_seven_out = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[6]/div/div/div[1]/input')

    click_eight_out = (By.XPATH, '/html/body/div[6]/div[1]/div[1]/ul/li')

    click_nine_out = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[7]/div/label/span[1]/span')

    click_all_out = (By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/form/div[8]/div/button')

    def carnumber_load(self,car_name):

        self.click_loctor(self.car_guanli)
        self.click_loctor(self.car_)
        self.click_loctor(self.button)
        self.input_loctor(self.input_car,txt=car_name)
        self.click_loctor(self.click_one)
        self.click_loctor(self.click_two)
        self.click_loctor(self.click_three)
        self.click_loctor(self.click_frou)
        self.click_loctor(self.click_five)
        self.click_loctor(self.click_six)
        self.click_loctor(self.click_seven)
        self.click_loctor(self.click_eight)
        self.click_loctor(self.click_nine)
        self.click_loctor(self.click_all)
        self.wait(1)
        self.driver.get_screenshot_as_file('D:\\POM\\picture\\车道自动化测试-入口.png')
        allure.attach.file(r'D:\\POM\\picture\\车道自动化测试-入口.png', attachment_type=allure.attachment_type.PNG)
        # self.waiting(3)

        self.wait(3)
        self.quit()
