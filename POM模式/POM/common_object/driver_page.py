# from selenium import webdriver
# from time import sleep
#
#
# class BaseTestCase():
#     def setUp(self) -> None:
#         self.driver = webdriver.Chrome()
#         self.driver.implicitly_wait(10)
#         self.driver.maximize_window()
#
#
#     def tearDown(self) -> None:
#         sleep(3)
#         self.driver.close()