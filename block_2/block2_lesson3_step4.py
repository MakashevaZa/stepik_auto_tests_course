from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button") 
    button.click()
    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element(By.ID, "input_value").text
    browser.find_element(By.ID, "answer").send_keys(calc(x))
    button = browser.find_element(By.CSS_SELECTOR, "button") 
    button.click()
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
