from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutReviewPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
        self.place_order_button = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/paymentBtn')
        self.continue_shop_button = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/shoopingBt')

    def click_place_order(self):
        self.wait.until(EC.element_to_be_clickable(self.place_order_button)).click()

    def click_continue_shopping(self):
        self.wait.until(EC.element_to_be_clickable(self.continue_shop_button)).click()