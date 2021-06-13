from selenium import webdriver
import os
import time

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    name = browser.find_element_by_name('firstname').send_keys("Ivan")
    name2 = browser.find_element_by_name('lastname').send_keys("Kudryashov")
    mail = browser.find_element_by_name('email').send_keys("ivan@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    file = browser.find_element_by_id('file').send_keys(file_path)

    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()