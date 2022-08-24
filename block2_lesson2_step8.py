from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "//label[contains(text(),'First name')]//following-sibling::input")
    input1.send_keys("ok")

    input2 = browser.find_element(By.XPATH, "//label[contains(text(),'Last name')]//following-sibling::input")
    input2.send_keys("ok")

    input3 = browser.find_element(By.XPATH, "//label[contains(text(),'Email')]//following-sibling::input")
    input3.send_keys("ok")

    file1 = browser.find_element(By.CSS_SELECTOR, "input[type='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'fff.txt')           # добавляем к этому пути имя файла 
    file1.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)


    button.click()
    
finally:
    time.sleep(10)
    browser.quit()
