from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    elements = browser.find_elements(By.CSS_SELECTOR, "input.form-control")
    for element in elements:
        element.send_keys("test")

    file_el = browser.find_element(By.ID, "file")
    file_el.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(10)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()