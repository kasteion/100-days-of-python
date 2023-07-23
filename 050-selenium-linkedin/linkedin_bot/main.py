from selenium import webdriver
from linkedin_bot import LinkedInBot
from time import sleep
import os

LINKEDIN_USER = os.environ.get("LINKEDIN_USER")
LINKEDIN_PASSWORD = os.environ.get("LINKEDIN_PASSWORD")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

linkedin_bot = LinkedInBot(driver)

driver.get("https://www.linkedin.com/login")
linkedin_bot.login(LINKEDIN_USER, LINKEDIN_PASSWORD)

sleep(2)

linkedin_bot.start_post()

sleep(2)

linkedin_bot.create_post("Hi, I'm doing a 100-day Python challenge; on day 49, "
                         "I'm playing with Selenium WebDriver to create this post automatically."
                         "\n--\n"
                         "Hola, estoy haciendo un desafío Python de 100 días; el día 49, "
                         "estoy jugando con Selenium WebDriver para crear esta publicación automáticamente.")


