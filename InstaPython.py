from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from time import sleep

class LoginPage():
    def __init__(self, driver):
        self.driver = driver
    
    def login(self, username, password):
        username_input= self.driver.find_element_by_xpath("//input[@name='username']")
        username_input.send_keys(username)
        password_input = self.driver.find_element_by_xpath("//input[@name='password']")
        password_input.send_keys(password)
        submit_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        submit_button.click()
        sleep(200)

class HomePage():
    def __init__(self, driver):
        self.driver =driver
    def goTo_login_page(self):
        self.driver.get("https://www.instagram.com/")
        self.driver.implicitly_wait(5)
        return LoginPage(self.driver)


username = 'rudransh69420'
password = 'rudra1609'

browser = webdriver.Firefox(executable_path="C:/Users/gaura/Desktop/geckodriver")
home = HomePage(browser)
home = home.goTo_login_page()
home.login(username, password)





# browser.get('https://www.instagram.com/')
# browser.implicitly_wait(5)

# wait = WebDriverWait(browser, 10)
# print('Title: %s' % browser.title)
# username = browser.find_element_by_xpath("//input[@name='username']").send_keys(username)
# first_result = wait.until(presence_of_element_located((By.XPATH, "//input[@name='username']")))

# sleep(10)
browser.quit()