import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.driver_setup import get_driver
from page_objects.cart_page import CartPage
from page_objects.catalog_page import CatalogPage
from page_objects.checkout_address_page import CheckoutAddressPage
from page_objects.checkout_payment_page import CheckoutPaymentPage
from page_objects.checkout_review_page import CheckoutReviewPage
from page_objects.product_page import ProductPage

try:
    print("Iniciando prueba de compra...")
    driver = get_driver()
    
    catalogo_page = CatalogPage(driver)
    producto_page = ProductPage(driver)
    carrito_page = CartPage(driver)
    direccion_page = CheckoutAddressPage(driver)
    pago_page = CheckoutPaymentPage(driver)
    revision_page = CheckoutReviewPage(driver)
    
    print("Seleccion del producto...")
    catalogo_page.select_product()
    
    print("Seleccion de color y agregar al carro...")
    producto_page.select_blue_color()
    producto_page.click_add_to_cart()
    producto_page.go_to_cart()
    
    print("Confirmar producto...")
    carrito_page.proceed_to_checkout()
    
    print("Completar formulario...")
    direccion_page.fill_shipping_details("Miguel Diaz", "Cra 1A No 27A-35", "Bogota", "Bogota", "110011", "Colombia")
    direccion_page.continue_to_payment()
    
    print("Completar datos de la tarjeta...")
    pago_page.fill_payment_details("Credit Card", "5555 5555 5555 4444", "12/30", "357")
    pago_page.continue_to_review()
    
    print("Confirmar pedido...")
    revision_page.click_place_order()

    assert revision_page.is_order_successful() is True, "Error: La pantalla de confirmación de pedido no se mostró."
    
    revision_page.click_continue_shopping()
    
    print("¡Flujo de compra completado con éxito!")
    
except Exception as e:
    print(f"Ocurrió un error en la prueba: {e}")
    
finally:
    if 'driver' in locals():
        driver.quit()
        print("Sesión de Appium cerrada correctamente.")