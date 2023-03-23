from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
driver.maximize_window()

driver.find_element(By.ID, "user-name").send_keys('standard_user')
driver.find_element(By.NAME, "password").send_keys('secret_sauce')
driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div').click()
description = driver.find_element(By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[2]').text
if description.__contains__("compromising style"):
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    if driver.find_element(By.XPATH, '//div[@id="shopping_cart_container"]/a/span').text == '1':
        print("Test for adding item to cart Passed")
    else:
        print("Test adding item to cart failed")

driver.close()