from selenium.webdriver.common.by import By

from web_bases.base_page import WebPage

class LoginPage(WebPage):
    def __init__(self,driver):
        self.driver = driver
    url = 'http://ws.appykt.com/#/'
    user = (By.XPATH, '//input[@type="text"]')
    pwd = (By.XPATH, '//input[@type="password"]')
    button = (By.XPATH, '//button[@type="button"]')

    def login(self,username,password):

        self.open(self.url)
        self.input_loctor(self.user,txt=username)
        self.input_loctor(self.pwd,txt=password)
        self.click_loctor(self.button)
        self.wait(3)
        # self.quit()