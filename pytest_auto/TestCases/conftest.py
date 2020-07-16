#coding:utf-8
import pytest
from selenium import webdriver
from Common.basepage import BasePage


driver=None
@pytest.fixture(scope="class")
def access_web():
    global driver
    #########################所有用例测试之前#只执行一次setup########################
    driver=webdriver.Firefox()
    driver.get("https://www.91testing.net/login")
    driver.maximize_window()
    yield (driver,)
    #########################所有用例执行之后#只执行一次teardown########################
    driver.quit()

@pytest.fixture()
def refresh_web():
    global driver
    #前置操作
    yield
    #后置操作，每个用例执行完成之后执行刷新操作############
    driver.refresh()


