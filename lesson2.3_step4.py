from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    button = browser.find_element_by_xpath('//button[text()="I want to go on a magical journey!"]')
    button.click()

    #alert = browser.switch_to.alert
    #alert.accept()

    sec_window = browser.window_handles[1]
    browser.switch_to.window(sec_window)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    def calc(x):
            return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)

    element = browser.find_element_by_id('answer').send_keys(y)


    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()