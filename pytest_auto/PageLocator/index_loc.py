#coding:utf-8
from selenium.webdriver.common.by import By
class Indexpage:
    free_study_loc=(By.LINK_TEXT,"免费课程")
    autoTest_loc=(By.LINK_TEXT,"自动化测试")
    select_class_loc=(By.XPATH,"//*[contains(text(),'Python3.0教程')]")
    jion_study=(By.XPATH,"// *[contains(text(), '去学习')]")
