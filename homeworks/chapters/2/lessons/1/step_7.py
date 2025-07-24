from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(f"{y}")
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(10)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()