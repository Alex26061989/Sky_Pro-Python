from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    # Перейти на страницу
    driver.get("http://uitestingplayground.com/ajax")
    print("Страница загружена")
    
    # Найти и нажать на синюю кнопку
    blue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary"))
    )
    blue_button.click()
    print("Синяя кнопка нажата")
    
    # Дождаться появления зеленой плашки с текстом
    # Плашка появляется после AJAX-запроса
    green_alert = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
    )
    
    # Получить текст из зеленой плашки
    alert_text = green_alert.text
    print(f"Текст из зеленой плашки: {alert_text}")
    
    # Проверить, что текст соответствует ожидаемому
    expected_text = "Data loaded with AJAX get request."
    if alert_text == expected_text:
        print("✓ Текст совпадает с ожидаемым")
    else:
        print(f"✗ Текст не совпадает. Ожидалось: '{expected_text}'")
    
except Exception as e:
    print(f"Произошла ошибка: {e}")
    
finally:
    # Закрыть браузер
    driver.quit()
    print("Браузер закрыт")