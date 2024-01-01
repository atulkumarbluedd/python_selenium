import time
from _ast import Assert

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

link5 = 'https://www.rahulshettyacademy.com/dropdownsPractise/'

service = Service()
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(link5)
time.sleep(5)

drop_down = driver.find_element(By.CSS_SELECTOR, '#autosuggest')
drop_down.send_keys('ab')

time.sleep(5)
element = driver.find_elements(By.CSS_SELECTOR, 'ul li.ui-menu-item')
for el in element:
    print(el.text)
    if (el.text == 'Saudi Arabia'):
        el.click()

selected_value = drop_down.text
assert selected_value in 'Saudi Arabia'

# handle allert like below -> it has accept and dismiss methods

# driver.switch_to.alert
# implicit waits and explicit waits
# driver.implicitly_wait(5) - wait for 5 sec


# expicit wait >>>>>>>>>>>>>>>>>>>>>>>>>>

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located(By.CSS_SELECTOR, '.promoInfo'))

# mouse hover
actions = ActionChains(driver)
actions.move_to_element(driver.find_element(By.CLASS_NAME, 'jkjkj')).click().perform()
# or
actions.move_to_element(driver.find_element(By.CLASS_NAME, 'jkjkj')).send_keys('hello').perform()

# other operations
actions.double_click(driver.find_element(By.CLASS_NAME, '.abcd'))
actions.context_click(driver.find_element(By.CLASS_NAME, 'ads')).perform()

# window handeling
windows_List = driver.window_handles
driver.switch_to.window(windows_List[1])

# frame handling
driver.switch_to.frame('name_of_frame')
driver.switch_to.default_content() # this is to switch back

'''
java script executor (scrolling)
'''

# scroll to height
driver.execute_script('window.scrollBy(0,document.body.scrollHeight);')
driver.get_screenshot_as_file("screen.png")


# run chrome in headless
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('headless')
driver=webdriver.chrome(service=service,options=chrome_options)

# handle ssl cerificate
chrome_options.add_argument('--ignore-certificate-errors') # it will ignore all ssl certificate errors

# maximize chrome using chrome options
chrome_options.add_argument('--start-maximized')

# read about user agent
# https://www.programcreek.com/python/example/95511/selenium.webdriver

# css for containing text --> a[href*='shop']
# note in assertion if we are using 'in' then it means this text is present in the text captured, but it does not mean that
# we have only this text is present
