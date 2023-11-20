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

# Use WebDriverWait to wait for an element to be present on the page
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "ENTERTAINMENT"))
    )
    print("Element found!")
except:
    print("Timed out waiting for element")

link = driver.find_element(By.LINK_TEXT,"ENTERTAINMENT")
link.click()

# Use WebDriverWait to wait for an element to be present on the page
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Everything is valuable"))
    )
    print("Element found!")
except:
    print("Timed out waiting for element")

link = driver.find_element(By.LINK_TEXT,"Everything is valuable")

link.click() #clicks on the link

time.sleep(2) # Introduce a delay to wait for the page to load (adjust as needed)

driver.back() #goes to back page

time.sleep(2) # Introduce a delay to wait for the page to load (adjust as needed)

driver.forward() #goes to forward page

time.sleep(10) # Introduce a delay to wait for the page to load (adjust as needed)
