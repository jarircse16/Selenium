from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Specify the path to the Chrome executable directly
chrome_executable_path = r"G:\Past\chrome-win32\chrome-win32\chrome.exe"

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()

# Pass the executable path to the options
chrome_options.binary_location = chrome_executable_path

# Open a browser window
driver = webdriver.Chrome(options=chrome_options)

# Navigate to a website
driver.get("https://news478.000webhostapp.com")

# Find and extract data from HTML elements
title = driver.title
print("Page Title:", title)

# Introduce a delay to wait for the page to load (adjust as needed)
time.sleep(5)


# Find a specific element using XPath
search = driver.find_element(By.NAME, "search")
search.clear() # Clears all input boxes
search.send_keys("Jarir")
search.send_keys(Keys.RETURN)

# Use WebDriverWait to wait for an element to be present on the page
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "logo"))
    )
    print("Element found!")
except:
    print("Timed out waiting for element")
#finally:
    # Don't forget to close the browser
   # driver.quit()

#element = driver.find_element(By.ID,"logo")
#print(element.text)

#Access Page Source
print(driver.page_source)
# Introduce another delay to keep the browser open for 5 seconds (adjust as needed)
time.sleep(5)

postinfo = driver.find_elements(By.CLASS_NAME,"post-information")
for post in postinfo:
    description = post.find_element(By.CLASS_NAME,"fa-tags")
    print(description.text)

# Wait for the elements to be present
wait = WebDriverWait(driver, 10)
postinfo = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "description")))

# Iterate over the found elements
for post in postinfo:
    # Print the text content of each element
    print(post.text)


#Close the browser
driver.quit()
