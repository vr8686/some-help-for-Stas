# code 1:
from selenium import webdriver

driver = webdriver.Chrome()

# Navigate to the ebay website
driver.get("https://www.ebay.com")

# Get the current URL and print it
current_url = driver.current_url
print("Current URL:", current_url)

# Close the browser
driver.quit()

# code 2:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Navigate to the ebay website
driver.get("https://www.ebay.com")

# Wait for the page to load (wait up to 10 seconds)
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

# Get the current URL and print it
current_url = driver.current_url
print("Current URL:", current_url)

# Close the browser
driver.quit()

# code 3:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Navigate to the ebay website
driver.get("https://www.ebay.com")

# Wait for the page to load (wait up to 10 seconds)
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

# Get the current URL and print it
current_url = driver.current_url
print("Current URL:", current_url)

# Find the search field by XPATH
search_field = driver.find_element(By.XPATH, '//*[@id="gh-ac"]')

# Wait for the search field to be clickable
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gh-ac"]')))

# Type "women watch" into it
search_field.send_keys("women watch")

# Press Enter to perform the search
search_field.send_keys(Keys.RETURN)

# Wait for the search results to load
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

# Close the browser
driver.quit()

# code 4:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Navigate to the ebay website
driver.get("https://www.ebay.com")

# Wait for the page to load (wait up to 10 seconds)
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

# Get the current URL and print it
current_url = driver.current_url
print("Current URL:", current_url)

# Find the search field by XPATH
search_field = driver.find_element(By.XPATH, '//*[@id="gh-ac"]')

# Wait for the search field to be clickable
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gh-ac"]')))

# Type "women watch" into it
search_field.send_keys("women watch")

# Press Enter to perform the search
search_field.send_keys(Keys.RETURN)

# Wait for the search results to load
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

# Verify the header contains "results for women watch"
header = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[1]/div[2]/div[2]')
assert "results for women watch" in header.text.lower(), "Header does not contain the expected text."

# Close the browser
driver.quit()