from appium import webdriver
desired_caps={}
desired_caps["platformName"]="Android"
desired_caps["platformVersion"]="5.1.1"
desired_caps["deviceName"]="127.0.0.1:62001"
desired_caps["appPackage"]="com.tal.kaoyan"
desired_caps["appActivity"]="com.tal.kaoyan.ui.activity.SplashActivity"
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)