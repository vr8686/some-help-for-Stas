from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from automated_search.base import Base

class Filter(Base):
    def select_option(self, option_text):
        option_locator = (By.XPATH, f"//span[text()='{option_text}']")
        option_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(option_locator)
        )
        option_element.click()

    def unselect_option(self, option_text):
        option_locator = (By.XPATH, f"//span[text()='{option_text}']")
        option_element = WebDriverWait(this.driver, 10).until(
            EC.element_to_be_clickable(option_locator)
        )
        option_element.click()