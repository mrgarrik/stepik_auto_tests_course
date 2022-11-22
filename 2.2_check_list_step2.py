from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element=browser.find_element(By.CSS_SELECTOR, "#num1")
    y_element=browser.find_element(By.CSS_SELECTOR, "#num2")
    x=x_element.text
    y=y_element.text
    z=str(str(int(x)+int(y)))
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(z)               
    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()