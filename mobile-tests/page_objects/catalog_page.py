from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CatalogPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.product_1 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.saucelabs.mydemoapp.android:id/productIV").instance(0)')

    def select_product(self):
        element = self.wait.until(EC.element_to_be_clickable(self.product_1))
        element.click()