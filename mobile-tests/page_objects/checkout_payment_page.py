from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPaymentPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
        self.full_name_card = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/nameET')
        self.number_card = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/cardNumberET')
        self.expiration_date = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/expirationDateET')
        self.security_code = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/securityCodeET')
        self.review_order_button = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/paymentBtn')

    def fill_payment_details(self, name, card, exp, cvv):
        self.wait.until(EC.visibility_of_element_located(self.full_name_card)).send_keys(name)
        self.driver.find_element(*self.number_card).send_keys(card)
        self.driver.find_element(*self.expiration_date).send_keys(exp)
        self.driver.find_element(*self.security_code).send_keys(cvv)

    def continue_to_review(self):
        self.driver.find_element(*self.review_order_button).click()