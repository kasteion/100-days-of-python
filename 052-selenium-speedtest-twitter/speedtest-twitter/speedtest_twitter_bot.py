from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class SpeedTestTwitterBot:
    def __init__(self, twitter_username: str, twitter_password: str):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.twitter_username = twitter_username
        self.twitter_password = twitter_password

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        start_button = self.driver.find_element(by=By.CSS_SELECTOR, value="div.start-button a.js-start-test")
        start_button.click()

        sleep(60)

        download_speed = self.driver.find_element(
            by=By.CSS_SELECTOR,
            value="span.result-data-large.number.result-data-value.download-speed")
        upload_speed = self.driver.find_element(
            by=By.CSS_SELECTOR,
            value="span.result-data-large.number.result-data-value.upload-speed")
        return {
            "download_speed": download_speed.text,
            "upload_speed": upload_speed.text,
        }

    def twitter_login_flow(self):
        self.driver.get("https://twitter.com/i/flow/login")
        sleep(2)

        username_input = self.driver.find_element(by=By.CSS_SELECTOR, value='input')
        username_input.send_keys(self.twitter_username)

        next_button = [div for div in self.driver.find_elements(by=By.CSS_SELECTOR, value='div')
                        if div.get_attribute("role") == "button" and div.text == "Next"]
        next_button[0].click()
        sleep(2)

        password_input = self.driver.find_element(by=By.NAME, value="password")
        password_input.send_keys(self.twitter_password)

        next_button = [div for div in self.driver.find_elements(by=By.CSS_SELECTOR, value='div')
                       if div.get_attribute("role") == "button" and div.text == "Log in"]
        next_button[0].click()
        sleep(2)

        verification_code = input("Enter your verification code: ")
        verification_code_input = self.driver.find_element(by=By.CSS_SELECTOR, value='input')
        verification_code_input.send_keys(verification_code)

        next_button = [div for div in self.driver.find_elements(by=By.CSS_SELECTOR, value='div')
                       if div.get_attribute("role") == "button" and div.text == "Next"]
        next_button[0].click()
        sleep(2)

    def tweet_internet_speed(self, tweet_message: str):
        tweet_content = self.driver.find_element(
            by=By.CSS_SELECTOR,
            value="div.public-DraftStyleDefault-block.public-DraftStyleDefault-ltr")
        tweet_content.send_keys(tweet_message)

        tweet_button = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]')
        tweet_button.click()
