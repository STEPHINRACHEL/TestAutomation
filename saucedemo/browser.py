from selenium.webdriver.common.by import By


class Login:
    def __init__(self, driver):
        self.driver = driver
        driver.get('https://www.saucedemo.com/')
        driver.maximize_window()


def login(driver, user):
    Login(driver)
    driver.find_element(By.ID, "user-name").send_keys(f'{user}')
    driver.find_element(By.NAME, "password").send_keys('secret_sauce')
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()


def close(driver):
    driver.close()
