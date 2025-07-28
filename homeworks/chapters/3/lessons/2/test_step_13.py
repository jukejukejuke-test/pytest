from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import unittest


def test_unique_fields_1():
    try:
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        expected_fields = ["First name*", "Last name*", "Email*"]

        for field_name in expected_fields:

            label = browser.find_element(By.XPATH, f"//label[text()='{field_name}']")
            assert label.is_displayed(), f"Поле '{field_name}' не отображается"

            input_field = browser.find_element(By.XPATH, f"//label[text()='{field_name}']/../input")
            assert input_field.is_displayed()

        elements = browser.find_elements(By.TAG_NAME, "input")
        for element in elements:
            element.send_keys("test")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

def test_unique_fields_2():
    try:
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        expected_fields = ["First name*", "Last name*", "Email*"]

        for field_name in expected_fields:

            label = browser.find_element(By.XPATH, f"//label[text()='{field_name}']")
            assert label.is_displayed(), f"Поле '{field_name}' не отображается"

            input_field = browser.find_element(By.XPATH, f"//label[text()='{field_name}']/../input")
            assert input_field.is_displayed()

        elements = browser.find_elements(By.TAG_NAME, "input")
        for element in elements:
            element.send_keys("test")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()