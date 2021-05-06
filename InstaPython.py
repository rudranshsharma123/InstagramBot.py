from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from time import sleep

class Interactions():
    def __init__(self, driver):
        self.driver = driver
    
    def search(self, to_search):
        search_box = self.driver.find_element_by_xpath("//input[@placeholder='Search']")
        sleep(6)
        search_box.send_keys(to_search)
        sleep(5)
        d = self.driver.find_element_by_xpath("//a[@class='-qQT3']")
        sleep(8)
        d.click()
        
    def like_many(self, number):
        first_image = self.driver.find_element_by_class_name("v1Nh3")
        first_image.click()
        for i in range(number):
            sleep(6+i)
            like_button = self.driver.find_element_by_xpath("//*[@aria-label='Like']")
            like_button.click()
            if i == 0:
                next_button = self.driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a")
            else:
                next_button = self.driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a[2]")
            next_button.click()
        sleep(20)
        
    def comment(self, content):
        comment_button = self.driver.find_element_by_xpath("//*[@aria-label='Comment']")
        comment_button.click()
        comment_area = self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea")
        comment_area.send_keys(content)
        sleep(10)
        # sleep(10)
        post_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        post_button.click()
        sleep(10)
        
    def like_and_comment_many_save(self, number, content):
        first_image = self.driver.find_element_by_class_name("v1Nh3")
        first_image.click()
        for i in range(number):
            sleep(6+i)
            like_button = self.driver.find_element_by_xpath("//*[@aria-label='Like']")
            like_button.click()
            self.comment(content)
            sleep(10)
            self.save_post()
            if i == 0:
                next_button = self.driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a")
            else:
                next_button = self.driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a[2]")
            next_button.click()
        sleep(20)
        
    def like_and_comment_many(sefl, number, content):
        first_image = self.driver.find_element_by_class_name("v1Nh3")
        first_image.click()
        for i in range(number):
            sleep(6+i)
            like_button = self.driver.find_element_by_xpath("//*[@aria-label='Like']")
            like_button.click()
            self.comment(content)
            sleep(10)
            if i == 0:
                next_button = self.driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a")
            else:
                next_button = self.driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a[2]")
            next_button.click()
        sleep(20)



    def save_post(self):
        sleep(10)
        save_button = self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[4]/div/div/button")
        save_button.click()
        sleep(10)


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
        sleep(10)
        
        return Interactions(self.driver)
        
        
        # return Interactions(self.driver)
        # driver.execute_script("arguments[0].click()", like_button)
        # sleep(10)
        # self.driver.get('https://www.instagram.com/explore/tags/dogs/')


class HomePage():
    def __init__(self, driver):
        self.driver =driver
    def goTo_login_page(self):
        self.driver.get("https://www.instagram.com/")
        self.driver.implicitly_wait(5)
        return LoginPage(self.driver)


username = 'your_username'
password = 'your_password'
search_text = "#cats"
comment_text = 'Amazing!'
number_of_posts_to_be_liked = 3

browser = webdriver.Firefox(executable_path="geckodriver.exe_filePath")
home = HomePage(browser)
home = home.goTo_login_page()
dogs = home.login(username, password)
dogs.search(search_text)
# dogs.save_post()
dogs.like_and_comment_many_save(number_of_posts_to_be_liked, comment_text)






# browser.get('https://www.instagram.com/')
# browser.implicitly_wait(5)

# wait = WebDriverWait(browser, 10)
# print('Title: %s' % browser.title)
# username = browser.find_element_by_xpath("//input[@name='username']").send_keys(username)
# first_result = wait.until(presence_of_element_located((By.XPATH, "//input[@name='username']")))

# sleep(10)
browser.quit()
