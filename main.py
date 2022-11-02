from selenium import webdriver #tool that is used to automate browsers
import os
import time
from selenium.webdriver.common.by import By #used to locate elements within the documents
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys #provides keys in keyboard such as enter, alt, etc.
from webdriver_manager.chrome import ChromeDriverManager #this will install chrome driver from other web drivers

driver = webdriver.Chrome(ChromeDriverManager().install())

class bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'
        self.bot = driver
        self.login()


    def login(self):
        self.bot.get(self.base_url)

        enter_username = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'username')))
        enter_username.send_keys(self.username)

        enter_password = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)
        enter_password.send_keys(Keys.RETURN)

        time.sleep(3)

        not_now = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button'))
        )
        not_now.click()

        time.sleep(5)

        turn_on = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'))
        )
        turn_on.click()
def init():
        bot('niyati_shah2601', 'niyati@2601')

        input("Done")
init()