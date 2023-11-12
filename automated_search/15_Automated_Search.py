from components.base import Base
from components.filter import LeftFilterPane
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EbayWatchAutomation(Base):
    def __init__(self, url):
        super().__init__(url)
        self.left_filter_pane = LeftFilterPane(self.driver)
        self.mismatches = []

    def apply_filters(self):
        filters_to_apply = ["Brand"]

        for filter_name in filters_to_apply:
            self.left_filter_pane.apply_filter(filter_name)

        # Check Rolex option
        self.left_filter_pane.select_rolex()

    def verify_titles_contain_rolex(self):
        # Wait for the search results to load
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, '//div[@class="s-item__info"]/h3[@class="s-item__title"]'))
        # )
        #
        # # Get the titles of the first two items
        # titles = self.driver.find_elements(By.XPATH, '//div[@class="s-item__info"]/h3[@class="s-item__title"]')[:2]
        titles = [WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//li[@data-gr4="2"]//span[@role="heading"]'))),
                  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//li[@data-gr4="3"]//span[@role="heading"]')))]
        # Verify that each title contains "rolex"
        for title in titles:
            if "rolex" not in title.text.lower():
                self.mismatches.append(f"Title '{title.text}' does not contain 'rolex'")

    def store_first_two_results(self):
        # Wait for the search results to load
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, '//div[@class="s-item__info"]/h3[@class="s-item__title"]'))
        # )

        # Get the titles and prices of the first two items
        titles = [WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//li[@data-gr4="2"]//span[@role="heading"]'))),
                  WebDriverWait(self.driver, 10).until(
                      EC.visibility_of_element_located((By.XPATH, '//li[@data-gr4="3"]//span[@role="heading"]')))]
        prices = [WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//li[@data-gr4="2"]//span[@class="s-item__price"]'))),
                  WebDriverWait(self.driver, 10).until(
                      EC.visibility_of_element_located((By.XPATH, '//li[@data-gr4="3"]//span[@class="s-item__price"]')))]

        # Store titles and prices in variables
        first_title = titles[0].text
        second_title = titles[1].text
        first_price = prices[0].text
        second_price = prices[1].text

        return first_title, first_price, second_title, second_price

    def open_and_verify_item(self, item_number, stored_title, stored_price):
        # Open the item in a new tab
        self.driver.execute_script(f"window.open('https://www.ebay.com/itm/{item_number}')")
        # Switch to the newly opened tab
        self.driver.switch_to.window(self.driver.window_handles[1])

        # Wait for the item details to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mainContent"]/div/div[1]/h1'))
        )

        # Get the title and price of the opened item
        opened_title = self.driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div[1]/h1').text
        opened_price = self.driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div[3]/div/div/div[1]/span').text

        # Verify the title and price
        if opened_title != stored_title:
            self.mismatches.append(f"Opened title '{opened_title}' does not match stored title '{stored_title}'")
        if opened_price != stored_price:
            self.mismatches.append(f"Opened price '{opened_price}' does not match stored price '{stored_price}'")

    def uncheck_rolex_option(self):
        # Switch to the main tab
        self.driver.switch_to.window(self.driver.window_handles[0])
        # Uncheck Rolex option
        self.left_filter_pane.uncheck_rolex()

    def check_casio_option(self):
        # Switch to the main tab
        self.driver.switch_to.window(self.driver.window_handles[0])
        # Check Casio option
        self.left_filter_pane.check_casio()

    def verify_last_two_results_contain_casio(self):
        # Wait for the search results to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="s-item__info"]/h3[@class="s-item__title"]'))
        )

        # Get the titles of the last two items
        titles = self.driver.find_elements(By.XPATH, '//div[@class="s-item__info"]/h3[@class="s-item__title"]')[-2:]

        # Verify that each title contains "casio"
        for title in titles:
            if "casio" not in title.text.lower():
                self.mismatches.append(f"Title '{title.text}' does not contain 'casio'")

    def print_mismatches(self):
        for mismatch in self.mismatches:
            print(mismatch)

if __name__ == "__main__":
    ebay_automation = EbayWatchAutomation(
        "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=watch&_sacat=0")

    try:
        ebay_automation.navigate()
        ebay_automation.uncheck_rolex_option()
        ebay_automation.verify_titles_contain_rolex()
        ebay_automation.store_first_two_results()
        ebay_automation.check_casio_option()
        ebay_automation.verify_last_two_results_contain_casio()
        ebay_automation.print_mismatches()

    finally:
        ebay_automation.close()