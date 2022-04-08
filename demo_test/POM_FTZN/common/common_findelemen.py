from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select

class Driver:

    # 初始化 driver
    def __init__(self,driver):
        self.driver = driver

    # 定位元素，返回调用
    def loctor(self,loc):
        return self.driver.find_element(*loc)

    # 文本输入
    def input(self,loc,txt):
        self.loctor(loc).send_keys(txt)

    # 点击
    def click_demo(self,loc):
        self.loctor(loc).click()

    # 下拉框选择
    def select_demo(self,loc,txt):
        Select(self.loctor(loc)).select_by_visible_text(txt)

    # 下拉取消选择
    def dismiss(self,loc,txt):
        Select(self.loctor(loc)).deselect_by_visible_text(txt)

    # 时间强制等待
    def waiting(self,wait):
        sleep(wait)

    # 推出浏览器
    def out(self):
        self.driver.quit()

    # 切换窗口
    def handle(self):
        windows = self.driver.window_handles
        return self.driver.switch_to.window(windows[-1])

    # 切换进入iframe框架
    def iframe_demo(self,loc):
        self.driver.switch_to.frame(self.driver.find_element(loc))
    # 推出iframe
    def quit_iframe(self):
        self.driver.switch_to.default_content()

#     处理弹窗
    def alert_demo(self,loc):
        # 切换弹框
        alert = self.driver.switch_to.alert
        # 点击确定
#         alert.accept()
# #         或点击取消
#         alert.dismiss()
# #         获取alert的内容
#         alert.getText()

#     滚动条设置,滚动到指定元素
    def execute(self,loc):
        target = self.loctor(loc)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
