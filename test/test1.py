
from saucedemo import browser
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://www.saucedemo.com/')
browser.login(driver)

actual_title = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span').text.upper()
print(f"Actual title is {actual_title}")
expected_title = "PRODUCTS"
print(f"Expected title is {expected_title}")

if actual_title == expected_title:
    print("Login Test Passed")

else:
    print("Login Test Failed")

browser.close(driver)
