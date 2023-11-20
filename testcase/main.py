import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):

    def setUp(self): # It will be called for each test cases
        chrome_executable_path = r"G:\Past\chrome-win32\chrome-win32\chrome.exe"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = chrome_executable_path
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("http://www.python.org")

    def test_title(self):
        mainPage = page.MainPage
        assert mainPage.is_title_matches(self)

    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    def test_example(self):
        print("Test")
        assert True
    
    #def test_example_2(self):
      #  print("Not a test")
      #  raise AssertionError("This test intentionally fails")

    def not_a_test(self):
        print("This is invisible")

    def tearDown(self): # It will be called for each test cases
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
