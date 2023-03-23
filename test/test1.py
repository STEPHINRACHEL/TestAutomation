
from saucedemo.browser import login, close, print_success, print_failure
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

user1 = 'standard_user'
user2 = 'locked_out_user'

# Test with standard_user
login(driver, 'standard_user')

actual_title = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span').text.upper()
print(f"Actual title is {actual_title}")
expected_title = "PRODUCTS"
print(f"Expected title is {expected_title}")

if actual_title == expected_title:
    print_success(user1)

else:
   print_failure(user1)


# Test with locked_out_user
login(driver, 'locked_out_user')

if driver.find_element(By.XPATH, '//*[@class="error-message-container error"]/h3').text.__contains__('locked out'):
    print_success(user2)
else:
    print_failure(user2)

close(driver)
