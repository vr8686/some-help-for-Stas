from selenium import webdriver
from automated_search.base import Base
from automated_search.filter import Filter

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Open the eBay watch page
url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=watch&_sacat=0"
driver.get(url)

# Create instances of the Base and Filter classes
base = Base(driver)
filter = Filter(driver)

# Task 1: Select "Rolex" option in Filter Pane
filter.select_option("Brand / Rolex")

# Task 2: Verify the first two results contain "rolex" in their title
# You can use the find_elements() method to get a list of results and verify the titles.

# Task 3: Store title and price of the first two results in a variable
# You can use find_elements() and extract the data from the elements.

# Task 4: Open the first item and verify the title and the price by comparing them with the stored data

# Task 5: Uncheck “Rolex“ option
filter.unselect_option("Brand / Rolex")

# Task 6: Check “Casio“ option
filter.select_option("Brand / Casio")

# Task 7: Verify the last two result items contain “Casio“ in their title

# Task 8: Save and print ALL the mismatches if any

# Close the WebDriver
driver.quit()