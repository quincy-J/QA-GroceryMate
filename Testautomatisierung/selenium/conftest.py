import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    # Cookie-Banner Handling (falls vorhanden)
    try:
        cookie_btn = driver.find_element(By.XPATH, "//button[contains(., 'Accept')]")
        cookie_btn.click()
    except:
        pass

    yield driver
    driver.quit()
