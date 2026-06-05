import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.driver_setup import get_driver
from page_objects.login_page import LoginPage

try:
    print("Iniciando entorno de pruebas...")
    driver = get_driver()
    
    login_page = LoginPage(driver)
    
    print("Abriendo el menú y buscando la pantalla de Login...")
    login_page.navigate_to_login()
    
    print("Ingresando credenciales...")
    login_page.enter_username("bod@example.com")
    login_page.enter_password("10203040")
    login_page.click_login()
    
    print("Validando aserción de estado...")
    assert login_page.is_login_successful(), "Error: El login falló, no se cargó el catálogo."
    
    print("¡Prueba de Login PASADA con éxito!")
    time.sleep(2) 

except Exception as e:
    print(f"Ocurrió un error en la prueba: {e}")
    
finally:

    if 'driver' in locals():
        driver.quit()
        print("Sesión de Appium cerrada correctamente.")