from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutAddressPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
        self.full_name = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/fullNameET')
        self.address_1 = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/address1ET')
        self.city = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/cityET')
        self.state_region = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/stateET')
        self.zip_code = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/zipET')
        self.country = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/countryET')
        self.to_pay_button = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/paymentBtn')

    def fill_shipping_details(self, name, address, city, state, zip_c, country):
        self.wait.until(EC.visibility_of_element_located(self.full_name)).send_keys(name)
        self.driver.find_element(*self.address_1).send_keys(address)
        self.driver.find_element(*self.city).send_keys(city)
        self.driver.find_element(*self.state_region).send_keys(state)
        self.driver.find_element(*self.zip_code).send_keys(zip_c)
        self.driver.find_element(*self.country).send_keys(country)

    def continue_to_payment(self):
        self.driver.find_element(*self.to_pay_button).click()