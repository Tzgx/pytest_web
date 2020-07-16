#coding:utf-8
from selenium.webdriver.common.by import By
class Loginpage():
    username_loc=(By.ID,"login_username")
    password_loc=(By.ID,"login_password")
    loginButton_loc=(By.CLASS_NAME,"js-btn-login")
    #用户名或密码错误    你还有4次机会？匹配部分 assin
    pwd_error_loc=(By.CLASS_NAME,"alert-danger")
    #密码为空：请输入密码；
    pwd_null_loc=(By.ID,"login_password-error")
    #用户名为空：请输入帐号
    username_null_loc = (By.ID, "login_username-error")
