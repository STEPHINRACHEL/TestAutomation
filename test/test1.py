from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
# driver = webdriver.Chrome();
driver.get('https://www.saucedemo.com/')

driver.find_element(By.ID, "user-name").send_keys('standard_user')
driver.find_element(By.NAME, "password").send_keys('secret_sauce')
driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

actual_title = (driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span').text).upper()
print(f"Actual title is {actual_title}")
expected_title = "PRODUCTS"
print(f"Expected title is {expected_title}")

if actual_title == expected_title:
    print("Login Test Passed")

else:
    print("Login Test Failed")

driver.close()
