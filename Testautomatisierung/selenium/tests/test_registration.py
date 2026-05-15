from selenium.webdriver.common.by import By
import time

def test_registration(driver):
    driver.get("https://automationexercise.com/")

    # Cookie Banner
    try:
        driver.find_element(By.XPATH, "//button[contains(., 'Accept')]").click()
    except:
        pass

    driver.find_element(By.XPATH, "//a[contains(text(),'Signup / Login')]").click()

    driver.find_element(By.XPATH, "//input[@name='name']").send_keys("Quincy Test")
    driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("quincy_test@example.com")
    driver.find_element(By.XPATH, "//button[contains(text(),'Signup')]").click()

    # Warte kurz, da die Seite langsam lädt
    time.sleep(2)

    assert "Enter Account Information" in driver.page_source