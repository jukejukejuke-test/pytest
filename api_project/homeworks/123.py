import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    service = Service(executable_path="c:/chromedriver/chromedriver.exe")
    browser = webdriver.Chrome(service=service)

    browser.get(link)

    time.sleep(5)
finally:
    browser.quit()