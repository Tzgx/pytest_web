#coding:utf-8
from Common.basepage import Basepage
from selenium import webdriver
from PageLocator.indexpage import Indexpage as Ip
import time
class IndexPage(Basepage):
    def jion_study(self):
        model="加入学习"
        self.move_to_ele(Ip.free_study_loc,model)
        self.ele_click(Ip.autoTest_loc,model)
        self.switch_to_window(model)
        #获取当前句柄
        print(self.cur_win_handle())
        #获取所有句柄
        print(self.win_handles())
        #获取href属性，解决多窗口问题
        att=self.get_element(Ip.select_class_loc,model).get_attribute("href")
        self.driver.get(att)
        time.sleep(3)
        self.ele_click(Ip.jion_study,model)

if __name__ == '__main__':
    driver=webdriver.Firefox()
    driver.get("https://www.91testing.net/")
    driver.maximize_window()
    po=IndexPage(driver)
    po.jion_study()

