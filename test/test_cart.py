from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_cart(login_in_driver):
    driver = login_in_driver

    # Agregar un producto al carrito
    driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()

    # Verificar que el contador del carrito se actualice correctamente
    contador_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

    # Mostrar mensaje de error si el producto no se ha agregado al carrito correctamente
    assert contador_cart.text == "1", "El producto no se ha agregado al carrito correctamente"

    # Obtener el nombre del producto agregado al carrito
    product_name = driver.find_elements(By.CLASS_NAME, "inventory_item_name")[0].text

    # Dirigirse al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Obtener el nombre del producto en el carrito
    cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    # Verificar que el nombre del producto en el carrito sea el mismo que el producto agregado
    assert cart_item == product_name, "El producto en el carrito no coincide"
