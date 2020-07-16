#coding:utf-8
from selenium import webdriver
import time
from Common.basepage import BasePage
from PageLocator.login_locator import Loginpage as Lp
class LoginPage(BasePage):
    def login_flow(self,username,password,model):
        #输入用户名
        self.input_text(Lp.username_loc,username,model)
        #输入密码
        self.input_text(Lp.password_loc,password,model)
        #点击登录
        self.click_ele(Lp.loginButton_loc,model)
    #用户名错误
    def username_error(self,model):
        return self.get_text(Lp.username_null_loc,model)
    #密码错误
    def pwd_error(self):
        return self.get_text(Lp.pwd_error_loc,model)


if __name__ == '__main__':
    driver=webdriver.Firefox()
    driver.get("https://www.91testing.net/login")
    po=LoginPage(driver)
    po.login_flow("","Z5201314","登录模块")
    time.sleep(3)
    print(po.username_error("用户名为空"))
