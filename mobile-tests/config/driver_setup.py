# Archivo: mobile-tests/config/driver_setup.py

from appium import webdriver
from appium.options.android import UiAutomator2Options

def get_driver():
    """Inicializa y retorna el driver de Appium con las capacidades base."""
    capabilities = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": "emulator-5554",
        "appPackage": "com.saucelabs.mydemoapp.android",
        "appActivity": "com.saucelabs.mydemoapp.android.view.activities.SplashActivity",
        "appWaitActivity": "com.saucelabs.mydemoapp.android.view.activities.MainActivity",
        "noReset": True,
        #"dontStopAppOnReset": True,
        "uiautomator2ServerLaunchTimeout": 90000
    }
    
    options = UiAutomator2Options().load_capabilities(capabilities)
    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    
    return driver