#coding:utf-8
import os
base_path=os.path.dirname(os.getcwd())
testcase_path=os.path.join(os.path.split(os.path.dirname(os.path.realpath(__file__)))[0],"TestCase")
log_path=os.path.join(os.path.split(os.path.dirname(os.path.realpath(__file__)))[0],"Output\\logs")
report_path=os.path.join(os.path.split(os.path.dirname(os.path.realpath(__file__)))[0],"Output\\report")
screen_path=os.path.join(base_path,"Output\\screenshot")
