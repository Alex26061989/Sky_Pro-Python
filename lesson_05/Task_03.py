from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


# Открыть браузер FireFox
driver = webdriver.Firefox()
    
try:
    # Перейти на страницу
    driver.get('http://the-internet.herokuapp.com/inputs')
        
    # Ждем загрузки страницы и появления поля ввода
    wait = WebDriverWait(driver, 10)
        
    # Находим поле ввода
    input_field = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="number"]'))
        )
        
    # Ввести в поле текст "Sky"
    input_field.send_keys("Sky")
    print("Введен текст 'Sky'")
        
    # Очистить это поле
    input_field.clear()
    print("Поле очищено")
        
    # Ввести в поле текст "Pro"
    input_field.send_keys("Pro")
    print("Введен текст 'Pro'")
        
    # Даем время увидеть результат
    import time
    time.sleep(2)
        
except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    # Закрыть браузер
    driver.quit()
    print("Браузер закрыт")
