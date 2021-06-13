import math
import time
from selenium import webdriver

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    pic = browser.find_element_by_id('treasure')
    
    x = pic.get_attribute('valuex')

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)

    element = browser.find_element_by_id('answer').send_keys(y)

    option = browser.find_element_by_id('robotCheckbox')
    option.click()

    option = browser.find_element_by_id('robotsRule')
    option.click()

    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()