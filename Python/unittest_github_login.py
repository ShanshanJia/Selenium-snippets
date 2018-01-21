import unittest, time
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class LoginTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://github.com/login")
        self.driver.maximize_window()
    
    def test_login(self):
        driver = self.driver
        userName = input('Enter your Username for GitHub: ')
        passWd = getpass('Enter Password: ')
        
        userNameBox = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("login_field"))
        passWdBox = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("password"))
        loginButton = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_name("commit"))
        userNameBox.clear()
        userNameBox.send_keys(userName)
        passWdBox.clear()
        passWdBox.send_keys(passWd)
        loginButton.click()
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//a[@class='header-logo-invertocat']"))

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
