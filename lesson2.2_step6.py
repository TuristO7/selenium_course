from selenium import webdriver
import math

browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)

x_element = browser.find_element_by_id('input_value')
x = x_element.text
def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
y = calc(x)

element = browser.find_element_by_id('answer').send_keys(y)

footer = browser.find_element_by_tag_name("footer")
browser.execute_script('arguments[0].style.visibility = \'hidden\'', footer)

option = browser.find_element_by_id('robotCheckbox')
option.click()

option1 = browser.find_element_by_id('robotsRule')
option1.click()

button = browser.find_element_by_xpath('//button[text()="Submit"]')
button.click()

#button = browser.find_element_by_tag_name("button")
#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#button.click()