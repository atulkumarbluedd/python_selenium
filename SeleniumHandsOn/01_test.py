import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# below websites we can use for practice selenium
from selenium.webdriver.support.select import Select

link1='https://www.rahulshettyacademy.com/angularpractice/'
link2='https://www.rahulshettyacademy.com/angularpractice/shop'
link3='https://www.rahulshettyacademy.com/AutomationPractice/'
link4='https://www.rahulshettyacademy.com/seleniumPractise/#/'
link5='https://www.rahulshettyacademy.com/dropdownsPractise/'


chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--start-maximized')
service = Service()
driver = webdriver.Chrome(service=service,options=chrome_options)

# driver.maximize_window()

 # driver.get('https://www.rahulshettyacademy.com/seleniumPractise/#/')
# driver.find_element(By.CLASS_NAME, 'login-btn').click()
# driver.find_element(By.CSS_SELECTOR, '.login-btn').click()

# in case of failure to locate element
# selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element:
# locators are -> classname, name, id, linkText, xpath, cssselector
# for css id use hash and for class dot
# assert "Rahul Shetty Academy" in driver.title.strip()

# for css to move downwards give spaces i.e : form div:nth-child(2) input

# static dropdown
driver.get(link1)
time.sleep(5)
element=driver.find_element(By.CSS_SELECTOR,'#exampleFormControlSelect1')
dropdown=Select(element)
dropdown.select_by_visible_text('Female')
time.sleep(5)
element.is_displayed()
print(element.is_displayed())

# take screen shot
driver.get_screenshot_as_file("screen.png")


