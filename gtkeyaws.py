from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import time
browser = webdriver.Firefox(executable_path="./drivers/geckodriver")

browser.get('https://654175463099.signin.aws.amazon.com/console?region=us-east-1')

browser.find_element_by_xpath('//*[@id="username"]').send_keys('cloud_user')
time.sleep(2)

browser.find_element_by_xpath('//*[@id="password"]').send_keys('%0Ajeshgec')
time.sleep(2)

browser.find_element_by_xpath('//*[@id="signin_button"]').click()
time.sleep(5)

browser.get('https://console.aws.amazon.com/iam/home?#/users/cloud_user?section=security_credentials')
time.sleep(7)

### Not being able to find a way to make the Create Access Key Button, 
### however the paintful repetitive step of login to the Console is considerably reduced:)
## Next step could be either to make the Create Access Key Button clickable or to build a CLI for this process
"""
browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[1]/userslist/parent-view/div[1]/user-details/div[2]/tabs/awsui-tabs/div/div/div/span/div/tab[3]/div/user-security-credentials/div/spin-while/div[2]/div/user-access-keys/div/awsui-button/button').click()
time.sleep(7)

browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[2]/modal-container/div/render-modal/new-access-keys-modal/awsui-modal/div[2]/div/div/div[2]/div/span/div/iam-table/div[2]/div/div[2]/div[1]/div/div/div[2]/hide-credential/span/span/a').click()
time.sleep(7)

keys = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[2]/modal-container/div/render-modal/new-access-keys-modal/awsui-modal/div[2]/div/div/div[2]/div/span/div/iam-table/div[2]/div')
print(keys)
"""