from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)




    # price = browser.find_element(By.ID, "price")
    expected_price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)


    browser.find_element(By.ID, "answer").send_keys(f"{y}")

    button = browser.find_element(By.ID, "solve")
    button.click()
    time.sleep(10)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()