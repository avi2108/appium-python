import options
from appium import webdriver
from appium.webdriver import appium_service
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

desired_caps = {
    "platformName": "Android",
    "platformVersion": "14",
    "deviceName": "RZCX51FAPFM",
    "browserName": "Chrome",
    'automationName': 'UiAutomator2',
    "app": "C:\\Users\\admin\\Downloads\\app-tejimandibeta-release-ga4-events.apk"

}



driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

email = driver.find_element_by_name('email').send_keys('ayadv@gmail.com')

time.sleep(4)
driver.quit()

