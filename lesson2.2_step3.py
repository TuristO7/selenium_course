import math
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x1 = int(browser.find_element_by_id("num1").text)
    y1 = int(browser.find_element_by_id("num2").text)

    def sum(x,y):
        return str(x+y)
    
    z = sum(x1, y1)

    consl = Select(browser.find_element_by_tag_name('select'))
    consl.select_by_value(z)


    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()