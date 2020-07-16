#coding:utf-8
from selenium import webdriver
from PageObjects.loginPage import LoginPage
import unittest
from ddt import ddt,data
from TestData import ddt_data as dd
test_data=dd.login_error
@ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.driver.get("https://www.91testing.net/login")
        cls.driver.maximize_window()
        cls.po=LoginPage(cls.driver)

    def tearDown(cls):
        cls.driver.refresh()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @data(*test_data)
    def test_error_login(cls,data):
        """fffffff"""
        cls.po.login_flow(data["username"],data["password"])
        cls.assertIn(data["check"], cls.po.password_error())

if __name__ == '__main__':
    unittest.main()