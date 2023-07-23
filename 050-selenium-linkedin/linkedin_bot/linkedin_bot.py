import selenium.webdriver.chrome.webdriver
from selenium.webdriver.common.by import By
from time import sleep


class LinkedInBot:
    def __init__(self, driver: selenium.webdriver.chrome.webdriver.WebDriver):
        self.driver = driver

    def login(self, username: str, password: str):
        username_input = self.driver.find_element(value="username")
        username_input.send_keys(username)

        password_input = self.driver.find_element(value="password")
        password_input.send_keys(password)

        signin_button = self.driver.find_element(by=By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
        signin_button.click()

    def start_post(self):
        start_post_button = self.driver.find_element(
            by=By.CSS_SELECTOR, value="div .share-box-feed-entry__top-bar button")
        start_post_button.click()

    def create_post(self, text):
        share_box = self.driver.find_element(by=By.CLASS_NAME, value="share-box")
        editor = share_box.find_element(by=By.CSS_SELECTOR, value="div.ql-editor.ql-blank")
        editor.send_keys(text)
        sleep(2)
        post_button = share_box.find_element(by=By.CSS_SELECTOR, value="button.share-actions__primary-action")
        post_button.click()



