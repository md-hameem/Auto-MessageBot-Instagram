# Importing necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initializing WebDriver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Define receiver usernames and message
usernames = ['User_name', 'User_name']
message_content = "final message test"


class InstagramBot:
    def __init__(self, username, password, usernames, message):
        self.username = username
        self.password = password
        self.usernames = usernames
        self.message = message
        self.base_url = 'https://www.instagram.com/'
        self.bot = driver
        self.login()

    def login(self):
        # Opening Instagram login page
        self.bot.get(self.base_url)

        # Entering username
        enter_username = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'username')))
        enter_username.send_keys(self.username)

        # Entering password
        enter_password = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)
        enter_password.send_keys(Keys.RETURN)
        time.sleep(5)

        # Handling first pop-up
        self.bot.find_element(By.XPATH,
                              '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button').click()
        time.sleep(5)

        # Handling second pop-up
        self.bot.find_element(By.XPATH,
                              '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
        time.sleep(5)

        # Clicking on direct button
        self.bot.find_element(By.XPATH,
                              '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[4]/div/a').click()
        time.sleep(3)

        # Clicking on pencil icon to start a new message
        self.bot.find_element(By.XPATH,
                              '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[1]/div/div[3]/button').click()
        time.sleep(2)

        # Iterating over each user to send message
        for user in self.usernames:
            # Entering the username
            self.bot.find_element(By.XPATH,
                                  '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input').send_keys(user)
            time.sleep(3)

            # Clicking on the username
            self.bot.find_element(By.XPATH,
                                  '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div[3]/button').click()
            time.sleep(4)

            # Clicking next
            self.bot.find_element(By.XPATH,
                                  '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/button').click()
            time.sleep(4)

            # Typing message
            send = self.bot.find_element(By.XPATH,
                                         '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
            send.send_keys(self.message)
            time.sleep(1)

            # Sending message
            send.send_keys(Keys.RETURN)
            time.sleep(2)

            # Clicking on direct option or pencil icon
            self.bot.find_element(By.XPATH,
                                  '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[1]/div/div[3]/button').click()
            time.sleep(4)


def init():
    # Initializing bot
    bot = InstagramBot('username', 'password', usernames, message_content)

    # Displaying "DONE" when the program ends
    input("DONE")


# Calling the initialization function
init()
