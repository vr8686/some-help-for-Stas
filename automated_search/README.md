1. Changes in filter.py
def uncheck_rolex(self):
- Changed rolex_xpath to '//span[@class="cbx x-refine__multi-select-cbx" and contains(text(), "Rolex")]' #  previous Xpath was for a checkbox which technically is not a link, easier to manipulate with Rolex text
- Removed “if rolex_checkbox.is_selected(): #  this line was preventing the webdriver from clicking 

2. Changes in 15_Automated_Search.py
if __name__ == "__main__":
   […]
    try:
   […]
- Added ebay_automation.verify_titles_contain_rolex()  #  this function was never called
   […]

3. Changes in 15_Automated_Search.py
def verify_titles_contain_rolex(self):
- Fixed XPaths for both items and put them in the list to make the rest of your code work
- Removed WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="s-item__info"]/h3[@class="s-item__title"]')))  # the script stops here because of wrong XPath

4. Changes in 15_Automated_Search.py
if __name__ == "__main__":
   […]
    try:
   […]
- Added ebay_automation.store_first_two_results()  # this function was never called
[…]

5. Changes in 15_Automated_Search.py
def store_first_two_results(self):
- Removed WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="s-item__info"]/h3[@class="s-item__title"]')))  # the script stops here because of wrong XPath
- Fixed “titles” list. Modified XPaths 
- Fixed “prices” list. Modified XPaths 
