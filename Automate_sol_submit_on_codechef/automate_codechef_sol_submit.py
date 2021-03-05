from selenium import webdriver
from getpass import getpass
browser = webdriver.Chrome()
browser.get("https://www.codechef.com")
username_element = browser.find_element_by_id("edit-name")
username_element.send_keys("ashish_2710")
password_element = browser.find_element_by_id("edit-pass")
password_element.send_keys(getpass("Enter password :"))

browser.find_element_by_id("edit-submit").click()
browser.get("https://www.codechef.com/problems/TEST")
browser.get("https://www.codechef.com/submit/TEST")

#browser.find_element_by_id("edit_area_toggle_checkbox_edit-program").click()

with open("solution.cpp", 'r') as f:
    code = f.read()
code_element = browser.find_element_by_id("edit-program")
code_element.send_keys(code)

browser.find_element_by_xpath('//*[@id="edit-language"]/option[1]').click()
browser.find_element_by_id("edit-submit-1").click()
