from selenium.webdriver.common.by import By


def login(driver):
    # driver = webdriver.Chrome();
    driver.find_element(By.ID, "user-name").send_keys('standard_user')
    driver.find_element(By.NAME, "password").send_keys('secret_sauce')
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()


def close(driver):
    driver.close()
