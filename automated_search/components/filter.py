from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LeftFilterPane:
    def __init__(self, driver):
        self.driver = driver

    def apply_filter(self, filter_name):
        filter_xpath = f"//span[contains(text(), '{filter_name}')]"
        filter_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, filter_xpath))
        )
        filter_element.click()

    def select_rolex(self):
        rolex_xpath = '//*[@id="x-refine__group_1__2"]/ul/li[1]/div/a/div/span/input'
        rolex_checkbox = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, rolex_xpath))
        )
        rolex_checkbox.click()

    def uncheck_rolex(self):
        rolex_xpath = '//*[@id="x-refine__group_1__2"]/ul/li[1]/div/a/div/span/input'
        rolex_checkbox = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, rolex_xpath))
        )
        if rolex_checkbox.is_selected():
            rolex_checkbox.click()

    def check_casio(self):
        casio_xpath = '//*[@id="x-refine__group_1__0"]/ul/li[4]/div/a/div/span'
        casio_checkbox = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, casio_xpath))
        )
        if not casio_checkbox.is_selected():
            casio_checkbox.click()
