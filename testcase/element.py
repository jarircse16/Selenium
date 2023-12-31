from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
class BasePageElement(object):
    locator = "q"
    def __set__(self,obj,value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(By.NAME, self.locator))
        lambda driver: driver.find_element(By.NAME, self.locator).clear() # Clear the input field
        lambda driver, value: driver.find_element(By.NAME, self.locator).send_keys(value) # Send keys to the input field

    def __get__(self,obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")
        
search_text_element = 5