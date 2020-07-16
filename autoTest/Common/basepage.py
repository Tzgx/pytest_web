#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime
from Common import dirpath_conf as df
from Common.logs import TestLog
logging=TestLog().getlog()
import time
class Basepage(object):
    def __init__(self,driver):
        # self.driver=webdriver.Firefox()
        self.driver=driver
    def eleVisibility(self,loc,timeout=10,poll_frequency=0.5,model=""):
        #元素判断 、日志输出、失败截图 、识别元素时长\
        logging.info("等待元素{}可见".format(loc))
        try:
            start_time=datetime.time()
            WebDriverWait(self.driver,timeout,poll_frequency).until(Ec.visibility_of_element_located(loc))
            end_time=datetime.time()
            long_time=(end_time-start_time).seconds
            logging.info("{0}:元素{1}已可见，元素开始识别时间{2}，结束识别时间{3}，识别时长{4}".format(model,loc,start_time,end_time,long_time))
        except:
            logging.info("没有识别该元素{}".format(loc))
            self.get_screenshot(model)
            raise

    def eleExists(self,loc,timeout=10,poll_frequency=0.5,model=""):
        #元素判断 、日志输出、失败截图 、识别元素时长\
        logging.info("等待元素{}可见".format(loc))
        try:
            start_time=datetime.time()
            WebDriverWait(self.driver,timeout,poll_frequency).until(Ec.visibility_of_element_located(loc))
            end_time=datetime.time()
            long_time=(end_time-start_time).seconds
            logging.info("{0}:元素{1}已可见，元素开始识别时间{2}，结束识别时间{3}，识别时长{4}".format(model,loc,start_time,end_time,long_time))
        except:
            logging.info("没有识别该元素{}".format(loc))
            self.get_screenshot(model)
            raise

    def get_element(self,loc,model):
        logging.info("{0}：查找元素{1}开始".format(model,loc))
        try:
            # WebDriverWait(self.driver,30,0.5).until(Ec.visibility_of_element_located(loc))
            self.eleVisibility(loc,model)
            ele=self.driver.find_element(*loc)
            return ele
        except:
            logging.info("{0}：没有找到元素:{1}".format(model,loc))
            self.get_screenshot(model)
            raise
    def ele_click(self,loc,model):
        #找元素
        ele=self.get_element(loc,model)
        logging.info("{0}：点击元素{1}".format(model,loc))
        try:
            ele.click()
        except:
            logging.info("{}：点击元素失败{}".format(model,loc))
            self.get_screenshot(model)
            raise
    def ele_sendKeys(self,loc,model,text):
        #找元素
        ele=self.get_element(loc,model)
        logging.info("{0}：找元素{1}，输入内容{2}".format(model,loc,text))
        try:
            ele.clear()
            ele.send_keys(text)
        except:
            logging.info("{0}：找元素{1}，输入内容{2}，失败".format(model,loc,text))
            self.get_screenshot("model")
        pass
    def get_screenshot(self,model):
        now=time.strftime("%Y-%m-%d_%H_%M_%S")
        file_path = df.screen_path + '\\{0}_{1}.png'.format(model, now)
        try:
            self.driver.get_screenshot_as_file(file_path)
            logging.info("截图成功，图片保存路径为{}".format(file_path))
        except:
            logging.info("截取图片失败")
            raise
    #获取元素text
    def get_text(self,loc,model):
        #找元素
        ele=self.get_element(loc,model)
        try:
            logging.info("{0}:获取元素{1}的text属性".format(model,loc))
            return  ele.text
        except:
            logging.info("获取元素text属性失败")
            self.get_screenshot(model)
            raise

    def move_to_ele(self,loc,model):
        #找元素
        ele=self.get_element(loc,model)
        logging.info("{0}:鼠标悬浮到元素{1}".format(model,loc))
        try:
            ActionChains(self.driver).move_to_element(ele).perform()
        except:
            logging.info("鼠标悬浮失败！")
            self.get_screenshot(model)
            raise

    def switch_to_window(self,model):
        try:
            #判断是否有新的句柄产生，获取最新的句柄
            WebDriverWait(self.driver,10,0.5).until(Ec.new_window_is_opened)
            handles=self.driver.window_handles
            logging.info("获取当前所有句柄{}".format(handles))
            logging.info("切换句柄{}".format(handles[-1]))
            self.driver.switch_to.window(handles[-1])
        except:
            logging.info("没有打开新窗口")
            self.get_screenshot(model)
            raise

    def cur_win_handle(self):
       return self.driver.current_window_handle
    
    def win_handles(self):
        return  self.driver.window_handles
