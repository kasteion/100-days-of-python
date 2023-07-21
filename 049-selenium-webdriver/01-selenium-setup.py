# Install Google Chrome https://www.google.com/intl/en_uk/chrome/
# Download chrome webdriver https://chromedriver.chromium.org/downloads
# Install selenium: pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By

# chrome_driver_path = "/Users/kasteion/Documents/selenium/chromedriver"
driver = webdriver.Chrome()

driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")

price_whole = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_fraction = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

print(price_whole.text, price_fraction.text, price_whole.get_attribute("class"))

by_css_selector = driver.find_element(By.CSS_SELECTOR, value=".priceToPay")
print(by_css_selector.text)

# https://www.w3schools.com/xml/xpath_intro.asp
by_x_path = driver.find_element(By.XPATH, value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[1]/span[2]')
print(by_x_path.text)

# driver.close()
driver.quit()
