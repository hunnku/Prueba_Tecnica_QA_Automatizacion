from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10) 
        self.menu_button = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/menuIV')
        self.option_login_button = (AppiumBy.XPATH, "//*[@text='Log In']")
        self.username_input = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/nameET')
        self.password_input = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/passwordET')
        self.login_submit = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/loginBtn')
        self.catalog_title = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/productTV')


    def navigate_to_login(self):
        menu = self.wait.until(EC.element_to_be_clickable(self.menu_button))
        menu.click()
        login_option = self.wait.until(EC.element_to_be_clickable(self.option_login_button))
        login_option.click()

    def enter_username(self, username):
        element = self.wait.until(EC.visibility_of_element_located(self.username_input))
        element.clear()
        element.send_keys(username)

    def enter_password(self, password):
        element = self.driver.find_element(*self.password_input)
        element.clear()
        element.send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_submit).click()
        
    def is_login_successful(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.catalog_title))
            return True
        except:
            return False
        
    