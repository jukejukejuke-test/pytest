from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    select = Select(browser.find_element(By.ID, "dropdown"))
    num_1 = int(browser.find_element(By.ID, "num1").text)
    num_2 = int(browser.find_element(By.ID, "num2").text)

    _sum = num_1 + num_2

    select.select_by_value(str(_sum))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(10)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()