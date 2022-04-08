from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from common.common_findelemen import Driver


class SearchObject:


    dingdan = (By.XPATH, '//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[3]/div')

    linting = (By.XPATH, '//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[3]/ul/li[1]')

    chechang = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/h4/div/div[1]/input')

    choose_chechang = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[2]')

    input_carnumber = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[1]/div/div/input')

    input_date = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[2]/div/div[1]/div/div/div/input')

    input_txt = (By.XPATH, '/html/body/div[3]/div[1]/div/div[1]/span[1]/div/input')

    date_button = (By.XPATH, '/html/body/div[3]/div[2]/button[2]')

    zhankai_button = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[10]/div/button[3]')

    quyu_demo = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[3]/div/div/div/input')

    quyu = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[2]')

    zhifuchchangjing_button = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[4]/div/div/div[1]/input')

    choose_chajing = (By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul/li[3]')

    zhifufangshi = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[5]/div/div/div[1]/input')

    chose_zhifufangshi = (By.XPATH, '/html/body/div[6]/div[1]/div[1]/ul/li[2]')

    zhifuzhuangtai = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[6]/div/div/div[1]/input')

    chose_zhuangtai = (By.XPATH, '/html/body/div[7]/div[1]/div[1]/ul/li[3]')

    kaipiaozhuangtai = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[7]/div/div/div[1]/input')

    chose_kaipiao = (By.XPATH, '/html/body/div[8]/div[1]/div[1]/ul/li[2]')

    qudao = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[8]/div/div/div[1]/input')

    qudao_chose =(By.XPATH, '/html/body/div[9]/div[1]/div[1]/ul/li[2]')

    pay = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[9]/div/div/div/input')

    chose_pay = (By.XPATH, '/html/body/div[10]/div[1]/div[1]/ul/li[2]')

    chaxun = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[10]/div/button[1]')

    text = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[2]/div/div/div[7]/div/div[2]/h3/div/span[2]')


    def __init__(self,driver):
        self.driver = driver
        self.Driver = Driver(self.driver)


    def dingdan_click(self):
        self.driver.find_element(*self.dingdan).click()

    def linting_click(self):
        self.driver.find_element(*self.linting).click()

    def chechang_click(self):
        self.driver.find_element(*self.chechang).click()

    def choose_chang(self):
        self.driver.find_element(*self.choose_chechang).click()

    def carnumber_input(self,number):
        self.driver.find_element(*self.input_carnumber).send_keys(number)

    def date_input(self):
        # self.Driver.loctor(self.input_date).clear()
        self.Driver.loctor(self.input_date).click()

    def date_txt_demo(self):
        self.Driver.loctor(self.input_txt).clear()
        # self.Driver.loctor(self.input_txt).click()

    def date_txt_input(self,txt):
        self.Driver.loctor(self.input_txt).send_keys(txt)

    def date_click(self):
        self.Driver.loctor(self.date_button).click()

    def zhankai(self):
        self.driver.find_element(*self.zhankai_button).click()

    def quyu_click(self):
        self.driver.find_element(*self.quyu_demo).click()

    def quyu_button(self):
        self.driver.find_element(*self.quyu).click()

    def zhifuchangjing(self):
        self.driver.find_element(*self.zhifuchchangjing_button).click()

    def chose_chajing(self):
        self.driver.find_element(*self.choose_chajing).click()

    def zhifushi_button(self):
        self.driver.find_element(*self.zhifufangshi).click()

    def chose_zhifushi(self):
        self.Driver.loctor(self.chose_zhifufangshi).click()

    # def chose_zhifufangshi(self):
    #     Driver(self.driver).common(self.zhifufangshi).click()
    def zhaungtai_button(self):
        self.Driver.loctor(self.zhifuzhuangtai).click()

    def chose_zhuang(self):
        self.Driver.loctor(self.chose_zhuangtai).click()

    def dingdanzhaungtai(self):
        self.Driver.loctor(self.kaipiaozhuangtai).click()

    def chose_kaipiao_demo(self):
        self.Driver.loctor(self.chose_kaipiao).click()

    def qudao_click(self):
        self.Driver.loctor(self.qudao).click()

    def qudaochoose(self):
        self.Driver.loctor(self.qudao_chose).click()

    def pay_fenlei(self):
        self.Driver.loctor(self.pay).click()

    def pay_click(self):
        self.Driver.loctor(self.chose_pay).click()



    def chaxun_click(self):
        self.driver.find_element(*self.chaxun).click()

    def get_text_linting(self):
        get_text = self.driver.find_element(*self.text).text
        return get_text