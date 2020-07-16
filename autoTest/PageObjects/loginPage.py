#coding:utf-8
from selenium import webdriver
from PageLocator.loginpageLoc import Loginpage as Lp
from Common.basepage import Basepage
import time
class LoginPage(Basepage):
    #登录流程  输入用户名、输入密码、点击登录按钮
    def login_flow(self,username,password):
        model="登录模块"
        self.ele_sendKeys(Lp.username_loc,model,username)
        self.ele_sendKeys(Lp.password_loc,model,password)
        self.ele_click(Lp.loginButton_loc,model)
    #用户名为空
    def username_null(self):
        model="登录模块"
        return self.get_text(Lp.username_null_loc,model)
    #密码错误
    def password_error(self):
        model="登录模块"
        return self.get_text(Lp.pwd_error_loc,model)
    #密码为空
    def password_null(self):
        model="登录模块"
        return self.get_text(Lp.pwd_null_loc,model)

if __name__ == '__main__':
    driver=webdriver.Firefox()
    driver.get("https://www.91testing.net/login")
    po=LoginPage(driver)
    po.login_flow("15179062604","Z5201314666")
    print(po.password_error())
    time.sleep(3)
    driver.quit()