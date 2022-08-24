from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x=int(browser.find_element(By.ID, "input_value").text)
    y=calc(x)


    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y);

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)


    option2 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    option2.click()

    button.click()
    
finally:
    time.sleep(10)
    browser.quit()
