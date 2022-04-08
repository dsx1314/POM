from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

class LoginPage:
    url = 'http://ws.appykt.com/#/'

    username_xpath = (By.XPATH, '//input[@type="text"]')
    password_xpath = (By.XPATH, '//input[@type="password"]')
    button_click = (By.XPATH, '//button[@type="button"]')
    text_loctore = (By.XPATH, '//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[2]/div/span')

    def __init__(self,driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def input_name(self,username):
        self.driver.find_element(*self.username_xpath).send_keys(username)

    def input_pwd(self,password):
        self.driver.find_element(*self.password_xpath).send_keys(password)

    def click_button(self):
        self.driver.find_element(*self.button_click).click()

    def get_text(self):
        text = self.driver.find_element(*self.text_loctore).text
        return text









