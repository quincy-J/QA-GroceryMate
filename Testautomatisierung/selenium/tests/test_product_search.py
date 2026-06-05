from selenium.webdriver.common.by import By

def test_product_search_after_login(driver):
    # 1. Login
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 1b. Überprüfen, dass Login erfolgreich war
    assert "inventory" in driver.current_url

    # 2. Produktname überprüfen
    product_name = "Sauce Labs Backpack"

    # Das Produkt steht in einem div mit class="inventory_item_name"
    product_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_name")

    # Wir prüfen, ob einer der Texte genau dem Produktnamen entspricht
    product_texts = [p.text for p in product_elements]

    assert product_name in product_texts


