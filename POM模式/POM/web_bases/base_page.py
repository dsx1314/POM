from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep


class WebPage:
    STYLE = "backgroup: pink;border: 2px solid red"
    #
    def get(self,driver):
        self.driver = webdriver.Chrome()


    def open(self,url):
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(url)

    def loctor(self,loc):
        return self.driver.find_element(*loc)

    # 元素颜色
    def color(self,loc):
        element = self.loctor(loc)
        self.driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",element,WebPage.STYLE)
        return element

    def clear_input(self,loc):
        self.color(loc).clear()


    def input_loctor(self,loc,txt):
        self.color(loc).send_keys(txt)

    # 定位指定元素
    def exceute_loctor(self,loc):
        ele = self.color(loc)
        self.driver.execute_script("arguments[0].scrollIntoView(false)",ele)

    # 截图操作
    def exce_png(self,file):
        self.driver.get_screenshot_as_file(file)


    def click_loctor(self,loc):
        try:
            self.color(loc).click()
            return True
        except NoSuchElementException:
            return False

    def handle(self,n):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[n])

    def iframe(self,loc):
        self.driver.switch_to.frame(self.loctor(loc))

    def quit_iframe(self):
        self.driver.switch_to.default_content()

    def wait(self,minute):
        sleep(minute)

    def close_window(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()