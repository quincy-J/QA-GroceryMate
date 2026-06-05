import pytest
from selenium.webdriver.common.by import By

USERS = [
    "standard_user",
    "locked_out_user",
    "problem_user",
    "performance_glitch_user",
    "error_user",
    "visual_user"
]

@pytest.mark.parametrize("username", USERS)
def test_login_with_all_users(driver, username):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    if username == "locked_out_user":
        assert "locked out" in driver.page_source.lower()
    else:
        assert "inventory" in driver.current_url
