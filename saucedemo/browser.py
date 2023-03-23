from selenium.webdriver.common.by import By

#
# class Login:
#     def open(self, driver):
#         driver.get('https://www.saucedemo.com/')
#         driver.maximize_window()
#


def login(driver, user):
    # open_url = Login()
    # open_url.open(driver)
    driver.get('https://www.saucedemo.com/')
    driver.maximize_window()
    driver.find_element(By.ID, "user-name").send_keys(f'{user}')
    driver.find_element(By.NAME, "password").send_keys('secret_sauce')
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()


def print_success(user):
    print(f"Login Test with {user} Passed................. :)")


def print_failure(user):
    print(f"Login Test with {user} Failed...................:(")


def close(driver):
    driver.close()
