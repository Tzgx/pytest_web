#coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from Common import dir_conf
import datetime
from Common.log import Log
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
logging=Log()
class BasePage(object):
    def  __init__(self,driver):
        self.driver=driver
        # self.driver=webdriver.Firefox()

    def wait_ele_visibility(self,model,loc):
        logging.info("{0}：等待元素{1}可见".format(model,loc))
        start_time=datetime.datetime.now()
        try:
            WebDriverWait(self.driver,10,0.5).until(Ec.visibility_of_element_located(loc))
            end_time=datetime.datetime.now()
            long_time=(end_time-start_time).seconds
            logging.info("{0}:元素{1}可见，识别开始时间{2}，识别结束时间{3}，识别总时长{4}".format(model,loc,start_time,end_time,long_time))
        except:
            logging.info("{0}:元素{1}不可见".format(model,loc))
            #截图
            self.get_screenshot(model)
            raise
    #截图函数
    def get_screenshot(self,model):
        now=time.strftime("%Y-%m_%d_%H_%M_%S")
        #D:\pytest_auto\Outputs\screenshot\登录_2020-05_13_15_40_54.png
        file_path=dir_conf.screen_path+"\\{0}_{1}.png".format(model,now)
        try:
            self.driver.get_screenshot_as_file(file_path)
            logging.info("截图成功，截图保存地址{}".format(file_path))
        except:
            logging.info("截图失败")
            raise
    #等待元素存在
    def wait_ele_exists(self,loc,model):
        logging.info("{0}:等待元素{1}存在".format(model,loc))
        try:
            WebDriverWait(self.driver,10,0.5).until(Ec.presence_of_element_located(loc))
        except:
            logging.info("{0}:元素{1}不存在".format(model,loc))
            self.get_screenshot(model)
            raise
    #查找元素
    def find_ele(self,loc,model):
        try:
            logging.info("{0}:查找元素{1}".format(model,loc))
            WebDriverWait(self.driver,10,0.5).until(Ec.visibility_of_element_located(loc))
            ele = self.driver.find_element(*loc)
            return ele
        except:
            logging.info("{0}:没有查找到元素{1}".format(model, loc))
            self.get_screenshot(model)
            raise
    def click_ele(self,loc,model):
        #查找元素
        ele=self.find_ele(loc,model)
        try:
            logging.info("{0}:点击元素{1}".format(model,loc))
            ele.click()
        except:
            logging("{0}:点击元素{1}失败".format(model,loc))
            self.get_screenshot(model)
            raise
    def input_text(self,loc,text,model):
        #查元素
        ele=self.find_ele(loc,model)
        logging.info("{0}：元素{1}输入{2}".format(model,loc,text))
        try:
            ele.send_keys(text)
        except:
            logging.info("{0}：元素{1}输入{2}失败".format(model,loc,text))
            self.get_screenshot(model)
            raise

    #获取元素属性
    def get_attr(self,loc,model,attr):
        ele=self.find_ele(loc,model)
        ele.get_attribute(attr)
    #获取text
    def get_text(self,loc,model):
        ele=self.find_ele(loc,model)
        return ele.text
if __name__ == '__main__':
    driver=webdriver.Firefox()
    driver.get("https://www.baidu.com")
    po=BasePage(driver)
    time.sleep(3)



# \\192.168.0.209