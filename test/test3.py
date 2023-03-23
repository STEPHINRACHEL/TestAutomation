
from saucedemo.browser import login, close
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://www.saucedemo.com/')

login(driver)




close(driver)
