
from saucedemo.browser import login, close
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://www.saucedemo.com/')

login(driver, 'standard_user')

driver.find_element(By.XPATH, '//div[@class="bm-burger-button"]/button').click()
driver.find_element(By.XPATH, '//div[@class="bm-menu"]/nav/a[3]').click()
if driver.find_element(By.XPATH, '//input[@id="login-button"]').is_displayed():
    print("Logout successful.....!")
else:
    print("Logout failed......!")

close(driver)

