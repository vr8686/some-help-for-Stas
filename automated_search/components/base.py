from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()

    def navigate(self):
        self.driver.get(self.url)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//body")))

    def close(self):
        self.driver.quit()
