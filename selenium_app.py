import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class SeleniumApp:
    def __init__(self, url) -> None:
        self.driver = webdriver.Chrome(os.getenv("CHROME_DRIVER_PATH"))
        self.driver.get(url)

    def click_via_xpath(self, xpath):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        ).click()

    def click_via_css_selector(self, css_selector):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        ).click()

    def input_text_into_field_via_name(self, name, text):
        self.driver.find_element(By.NAME, name).send_keys(text)

    def exit_automation(self):
        self.driver.quit()
