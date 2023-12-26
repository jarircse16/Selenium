from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Path to the Chrome executable
PATH = r"G:\Past\chrome-win32\chrome-win32\chrome.exe"

# Create an instance of ChromeOptions
chrome_options = webdriver.ChromeOptions()

# Specify the path to the Chrome executable
chrome_options.binary_location = PATH

# Pass the ChromeOptions to the Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://allfreetools.000webhostapp.com/login.php")
print(driver.title)

# Find the username and password input fields and the login button
username_input = driver.find_element("name", "username")
password_input = driver.find_element("name", "password")
login_button = driver.find_element("css selector", "input[type='submit']")

# Fill in the username and password fields
username_input.send_keys("admin")
password_input.send_keys("password")  # Replace with the actual password

# Click the login button
login_button.click()

# Introduce a delay to keep the browser open for 10 seconds (adjust as needed)
time.sleep(10)

# Quit the driver
driver.quit()
