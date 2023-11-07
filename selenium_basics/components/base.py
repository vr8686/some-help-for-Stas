""" #0
class Base:
    pass"""

""" #1
from selenium.webdriver.remote.webdriver import WebDriver

class Base:
    def __init__(self, driver: WebDriver):
        self.driver = driver"""

""" #2
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()"""

#4
class Base:
    BASE_VAR = "Base Var"

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        # Previous code for the click method (if any)

    def select_option(self, option, visible=False):
        print(self.BASE_VAR)
        print(option)
        print(visible)
