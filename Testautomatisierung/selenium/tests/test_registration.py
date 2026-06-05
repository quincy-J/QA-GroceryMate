from selenium.webdriver.common.by import By

def test_registration(driver):
    driver.get("https://automationexercise.com/")

    # 3. Home sichtbar
    assert "Automation Exercise" in driver.title

    # 4. Signup/Login klicken
    driver.find_element(By.XPATH, "//a[text()=' Signup / Login']").click()

    # 5. 'New User Signup!' sichtbar
    assert driver.find_element(By.XPATH, "//h2[text()='New User Signup!']").is_displayed()

    # 6. Name + Email
    driver.find_element(By.NAME, "name").send_keys("Quincy Test")
    driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("quincy_test@example.com")

    # 7. Signup
    driver.find_element(By.XPATH, "//button[text()='Signup']").click()

    # 8. ENTER ACCOUNT INFORMATION sichtbar
    assert driver.find_element(By.XPATH, "//b[text()='Enter Account Information']").is_displayed()

    # 9. Account Details
    driver.find_element(By.ID, "id_gender1").click()
    driver.find_element(By.ID, "password").send_keys("Test1234")
    driver.find_element(By.ID, "days").send_keys("10")
    driver.find_element(By.ID, "months").send_keys("May")
    driver.find_element(By.ID, "years").send_keys("1990")

    # 10. Newsletter Checkbox
    driver.find_element(By.ID, "newsletter").click()

    # 11. Offers Checkbox
    driver.find_element(By.ID, "optin").click()

    # 12. Address Details
    driver.find_element(By.ID, "first_name").send_keys("Quincy")
    driver.find_element(By.ID, "last_name").send_keys("Tester")
    driver.find_element(By.ID, "company").send_keys("QA GmbH")
    driver.find_element(By.ID, "address1").send_keys("Teststraße 1")
    driver.find_element(By.ID, "address2").send_keys("Wohnung 2")
    driver.find_element(By.ID, "country").send_keys("Germany")
    driver.find_element(By.ID, "state").send_keys("Hamburg")
    driver.find_element(By.ID, "city").send_keys("Hamburg")
    driver.find_element(By.ID, "zipcode").send_keys("20095")
    driver.find_element(By.ID, "mobile_number").send_keys("0123456789")

    # 13. Create Account
    driver.find_element(By.XPATH, "//button[text()='Create Account']").click()

    # 14. ACCOUNT CREATED sichtbar
    assert driver.find_element(By.XPATH, "//b[text()='Account Created!']").is_displayed()

    # 15. Continue
    driver.find_element(By.XPATH, "//a[text()='Continue']").click()

    # 16. Logged in as sichtbar
    assert driver.find_element(By.XPATH, "//a[contains(text(),'Logged in as')]").is_displayed()

    # 17. Delete Account
    driver.find_element(By.XPATH, "//a[text()=' Delete Account']").click()

    # 18. ACCOUNT DELETED sichtbar
    assert driver.find_element(By.XPATH, "//b[text()='Account Deleted!']").is_displayed()

    driver.find_element(By.XPATH, "//a[text()='Continue']").click()
