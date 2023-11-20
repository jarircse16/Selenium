from selenium import webdriver
import time

# Path to the Chrome executable
PATH = r"G:\Past\chrome-win32\chrome-win32\chrome.exe"

# Create an instance of ChromeOptions
chrome_options = webdriver.ChromeOptions()

# Specify the path to the Chrome executable
chrome_options.binary_location = PATH

# Pass the ChromeOptions to the Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://techwithtim.net")
print(driver.title)

# Introduce a delay to keep the browser open for 10 seconds (adjust as needed)
time.sleep(1000)

# Quit the driver
driver.quit()
