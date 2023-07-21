from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime as dt
# import threading


# def fun(interval):
#     if interval > 60:
#         cps = driver.find_element(By.ID, value="cps")
#         print(cps.text)
#         driver.quit()
#     else:
#         store_items = driver.find_element(By.ID, value="store").find_elements(By.CSS_SELECTOR, value="div")
#         store_items.reverse()
#         items_can_buy = [item for item in store_items if item.get_attribute("class") != "grayed"]
#         if len(items_can_buy) > 0:
#             items_can_buy[0].click()
#         s = threading.Timer(5, fun, [interval + 1])
#         s.start()


driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# start_time = threading.Timer(5, fun, [1])
# start_time.start()

cookie = driver.find_element(By.ID, value="cookie")

play = True
start_time = dt.datetime.now()
interval = 0


while play:
    cookie.click()
    delta = dt.datetime.now() - start_time
    if delta.seconds >= 300:
        cps = driver.find_element(By.ID, value="cps")
        print(cps.text)
        play = False
    elif delta.seconds % 5 == 0 and delta.seconds > interval:
        interval = delta.seconds
        store_items = driver.find_element(By.ID, value="store").find_elements(By.CSS_SELECTOR, value="div")
        store_items.reverse()
        items_can_buy = [item for item in store_items if item.get_attribute("class") != "grayed"]
        if len(items_can_buy) > 0:
            items_can_buy[0].click()


driver.quit()
