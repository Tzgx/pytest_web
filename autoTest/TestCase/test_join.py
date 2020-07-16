#coding:utf-8
from selenium import webdriver
import unittest
from PageObjects.indexPage import IndexPage as Ip
from PageObjects.loginPage import LoginPage as Lp
from TestData import login_data as Ld
class TestJoin(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get("https://www.91testing.net/login")
        #先登录
        Lp(self.driver).login_flow(Ld.login_suc["username"],Ld.login_suc["password"])
        self.po=Ip(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_join_study(self):
        try:
           self.po.jion_study()
        except Exception as e:
            print(e)
            raise

if __name__ == '__main__':
    unittest.main()
