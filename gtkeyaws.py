from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import time
browser = webdriver.Firefox(executable_path="./drivers/geckodriver")

browser.get('https://275976089985.signin.aws.amazon.com/console?region=us-east-1')

browser.find_element_by_xpath('//*[@id="username"]').send_keys('username')
time.sleep(2)

browser.find_element_by_xpath('//*[@id="password"]').send_keys('password')
time.sleep(2)

browser.find_element_by_xpath('//*[@id="signin_button"]').click()
time.sleep(5)
