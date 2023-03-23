from saucedemo import browser
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://www.saucedemo.com/')
browser.login(driver)

driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div').click()
description = driver.find_element(By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[2]').text
if description.__contains__("compromising style"):
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    if driver.find_element(By.XPATH, '//div[@id="shopping_cart_container"]/a/span').text == '1':
        print("Test for adding item to cart Passed")
    else:
        print("Test adding item to cart failed")

browser.close(driver)
