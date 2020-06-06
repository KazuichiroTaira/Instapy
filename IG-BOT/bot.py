from selenium import webdriver
import os
import time

class InstagramBot:

    def __init__(self, username, password):

        """
        Initializes an instance of the Instagram Bot class.

        Call the login method to authenticate a user with IG

        Args:
            username:str: The Instagram username for a user
            password:str: The Instagram password for a user

        Attribute:
            driver: Selenium.webdriver.Chrom: The Chromedriver that is used to autmate brower actions
        """

        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'
        self.driver = webdriver.Chrome('./chromedriver')

        self.login()



    def login(self):
        self.driver.get('{}/accounts/login/'.format(self.base_url))
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div[1]/button').click()
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_elements_by_xpath("//div[contains(text(),'Log In')]")[0].click()


    def nav_user(self, user):
        self.driver.get('{}/{}/'.format(self.base_url, user))

    def follow_user(self, user):
        self.nav_user(user)

        follow_botton = self.driver.find_elemets_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[2]/div/span/span[1]/button')
        follow_botton.click()


if __name__ == '__main__':

    config_path = './config.ini'
    cparser = configparser.ConfigPerser()
    cparser.read('config_path')
    username = cparser['AUTH']['USERNAME']
    password = cparser['AUTH']['PASSWORD']

    ig_bot = InstagramBot('username', 'password')
    # ig_bot.nav_user(('temp_username','temp_password'))

    ig_bot.nav_user('username')

    ig_bot.follow_user('costoaccessories')

    print(ig_bot.username)


