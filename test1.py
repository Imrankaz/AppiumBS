#print(12)
from appium import webdriver
from selenium.webdriver.common.by import By

desired_capabilities = {
	"deviceName": "23b8b0b20204",
	"platformName": "android",
	"appPackage": "com.nopstation.nopcommerce.nopstationcart",
	"appActivity": "com.bs.ecommerce.main.SplashScreenActivity",
	"noReset": True
	}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_capabilities)