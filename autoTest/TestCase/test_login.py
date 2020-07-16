#coding:utf-8
from selenium import webdriver
from PageObjects.loginPage import LoginPage
import unittest
from ddt import ddt,data
from TestData import login_data as ld
from Common.logs import TestLog
logging=TestLog().getlog()

# data=ld.login_error
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

    def test_05_passLogin(cls):
        """用户名密码正确，登录成功"""
        logging.info("测试日志")
        cls.po.login_flow(ld.login_suc["username"],ld.login_suc["password"])


    def test_02_password_null(cls):
        """密码为空"""
        logging.info("测试日志")
        cls.po.login_flow(ld.login_password_null["username"],ld.login_password_null["password"])
        cls.assertEqual(cls.po.password_null(),ld.login_password_null["check"])

    def t1est_03_username_null(cls):
        """用户名为空"""
        logging.info("测试日志")
        cls.po.login_flow(ld.login_username_null["username"],ld.login_username_null["password"])
        cls.assertEqual(cls.po.username_null(),ld.login_username_null["check"])

    @data(*ld.login_error)
    def t1est_04_errorLogin(cls,data):
        """用户名密码错误"""
        logging.info("测试日志")
        cls.po.login_flow(data["username"],data["password"])
        cls.assertIn(data["check"],cls.po.password_error())

if __name__ == '__main__':
    unittest.main()

