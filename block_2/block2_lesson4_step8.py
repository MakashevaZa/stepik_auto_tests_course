from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)



    
    element = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element(By.ID, "book")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


    button2 = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
    x = browser.find_element(By.ID, "input_value").text
    browser.find_element(By.ID, "answer").send_keys(calc(x)) 
    button2.click()
    # ждем загрузки страницы


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(40)
    # закрываем браузер после всех манипуляций
    browser.quit()

