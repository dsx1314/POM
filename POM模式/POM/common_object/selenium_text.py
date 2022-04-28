from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchFrameException

def page_contains(driver:webdriver.Chrome, text:str):
    xpath_expr = f"//*[contains(text(),'{text}')]"

    try:
        driver.find_element(By.XPATH,xpath_expr)
        return True

    except NoSuchFrameException:
        return False