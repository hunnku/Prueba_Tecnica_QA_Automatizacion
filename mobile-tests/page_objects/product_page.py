from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.change_color = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Blue color")')
        self.add_to_cart = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/cartBt')
        self.cart_icon = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/cartIV')

    def select_blue_color(self):
        self.wait.until(EC.element_to_be_clickable(self.change_color)).click()

    def click_add_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.add_to_cart)).click()
        
    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.cart_icon)).click()