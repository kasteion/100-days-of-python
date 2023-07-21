from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.python.org/")

# events = [
#     {
#         'time': event.find_element(By.CSS_SELECTOR, value="time").text,
#         'name': event.find_element(By.CSS_SELECTOR, value="a").text,
#     } for event in driver.find_element(By.CLASS_NAME, value="event-widget").find_elements(By.CSS_SELECTOR, value="li")
# ]

event_list = driver.find_elements(By.CLASS_NAME, value="event-widget li")
event_map = {
    i: {
        "time": event_list[i].find_element(By.CSS_SELECTOR, value="time").text,
        "name": event_list[i].find_element(By.CSS_SELECTOR, value="a").text,
    } for i in range(len(event_list))
}

print(event_map)

driver.quit()
