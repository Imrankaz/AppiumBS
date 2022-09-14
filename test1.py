#print(12)
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By


desired_capabilities = {
	"deviceName": "23b8b0b20204",
	"platformName": "android",
	"appPackage": "com.nopstation.nopcommerce.nopstationcart",
	"appActivity": "com.bs.ecommerce.main.SplashScreenActivity",
	"noReset": True
	}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_capabilities)


#Scenario: 01 Customer add products in his shopping cart
#Mike on home page after opening nopCart mobile app

time.sleep(10)


#Mike click "electronics" from our categories list from home page

#driver.swipe(1012,962,55,962,300)
#time.sleep(5)

#driver.find_element(By.XPATH, "(//android.widget.ImageView[@content-desc='Placeholder'])[2]").click()
#driver.find_element(By.XPATH, "//*[text()='Electronics']").click()
#driver.find_element(By.XPATH, "//*[contains(text(),'Electronics')]").click()



el1 = driver.find_element(By.XPATH, "//android.widget.FrameLayout[@content-desc=\"Category\"]/android.widget.FrameLayout/android.widget.ImageView")
el1.click()
time.sleep(5)
el2 = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[7]/android.widget.TextView")
el2.click()
time.sleep(10)


#
driver.swipe(903,1660,903,350,300)
time.sleep(5)

#Mike click to "Nokia Lumia 1020" product details page

#driver.find_element(By.XPATH, '//*[text()="Nokia Lumia 1020"]').click()
#driver.find_element(By.XPATH, "//*[text='Nokia Lumia 1020']").click()
#driver.find_element(By.XPATH, "//android.widget.ImageView[text()='Nokia Lumia 1020']").click()
#driver.find_element(By.XPATH, "(//android.widget.ImageView[@content-desc='Placeholder'])[5]").click()

#ele_xapth = driver.find_element(AppiumBy.XPATH,'//*[text()="Nokia Lumia 1020"]')

ele_Nokia_xapth = driver.find_element(AppiumBy.XPATH,'//*[@text="Nokia Lumia 1020"]')
#ele_xapth = driver.find_element(AppiumBy.XPATH,"(//android.widget.ImageView[@content-desc='Placeholder'])[5]")
ele_Nokia_xapth.click()
time.sleep(5)


driver.swipe(750,1500,750,900,300)
time.sleep(5)

#Mike select size "Large" from product details page

ele_Size_xapth = driver.find_element(AppiumBy.XPATH,'//*[@text="Size"]')
ele_Size_xapth.click()
time.sleep(5)

ele_Large_xapth = driver.find_element(AppiumBy.XPATH,'//*[@text="Large "]')
ele_Large_xapth.click()
time.sleep(5)

ele_Done_xapth = driver.find_element(AppiumBy.XPATH,'//*[@text="Done"]')
ele_Done_xapth.click()
time.sleep(5)

#Mike click plus button to increase Qty by "2"

ele_Done_xapth = driver.find_element(AppiumBy.ID,'com.nopstation.nopcommerce.nopstationcart:id/btnPlus')
ele_Done_xapth.click()
time.sleep(5)

#new_Quantity = driver.find_element(AppiumBy.ID,'com.nopstation.nopcommerce.nopstationcart:id/tvQuantity').text
#if new_Quantity  == 2:
#	assert True
#else:
#	assert False

#Then: Mike click add to cart button to add the product in his cart
#driver.swipe(750,1500,750,900,300)
#time.sleep(5)

#ele_AddToCart_xapth = driver.find_element(AppiumBy.ID,'com.nopstation.nopcommerce.nopstationcart:id/btnPlus')
#ele_AddToCart_xapth .click()
#time.sleep(5)

driver.quit()
print("test completed")