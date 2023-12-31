# from selenium import webdriver
# from selenium.webdriver.firefox.service import service
import selenium

selenium.__version__
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

if __name__ == '__main__':
    service = Service()  # this service class is responsible for starting and stopping the chrome driver
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.get('https://rahulshettyacademy.com')

    print(driver.title)
    print(driver.current_url)
    driver.minimize_window()
    driver.get('https://google.com')
    driver.back()
    driver.refresh()
    driver.forward()

# if you have chrome driver then you can use the same path as service(path_chromedriver)
# here it will close automatichally no need to call driver.close
