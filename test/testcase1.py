from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
# driver = webdriver.Chrome();
driver.get('https://www.saucedemo.com/')

driver.find_element(By.ID, "user-name").send_keys('standard_user')
driver.find_element(By.NAME, "password").send_keys('secret_sauce')
driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

actual_title = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span').text
expected_title = "PRODUCTS"

if actual_title==expected_title:
    print("Login Test Passed")
    driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div').click()
    description = driver.find_element(By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[2]').text
    if description.__contains__("compromising style"):
        driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
        if driver.find_element(By.XPATH, '//div[@id="shopping_cart_container"]/a/span').text == '1':
            print("Test Passed for adding item to cart")
        else:
            print("Test failed to add item to cart")
else:
    print("Login Test Failed")



driver.close()