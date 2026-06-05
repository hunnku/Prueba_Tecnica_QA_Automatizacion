from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.confirm_products = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/cartBt')

    def proceed_to_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.confirm_products)).click()