import unittest
import HtmlTestRunner
from selenium import webdriver
import sys
sys.path.append("C://Users//harsh//PycharmProjects//POMbasedUnitTest")
from PageObjects.LoginPage import LoginPage
import time


class LoginTest(unittest.TestCase):
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"
    driver = webdriver.Chrome(executable_path="..//Drivers//chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        lp = LoginPage(self.driver)
        # lp.setUsername(self.username)
        # lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(5)
        self.assertEqual("Dashboard / nopCommerce administration", self.driver.title, "Expected title not found")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="..//Reports"))
