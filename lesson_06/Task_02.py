from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

try:
    # Перейти на страницу
    driver.get("http://uitestingplayground.com/textinput")
    print("Страница загружена")
    
    # Найти поле ввода и дождаться его доступности
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "newButtonName"))
    )
    
    # Очистить поле (если там есть текст) и ввести "SkyPro"
    input_field.clear()
    input_field.send_keys("SkyPro")
    print('В поле ввода введен текст: "SkyPro"')
    
    # Найти синюю кнопку и нажать на нее
    blue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "updatingButton"))
    )
    blue_button.click()
    print("Синяя кнопка нажата")
    
    # Дождаться изменения текста кнопки
    # Используем ожидание, пока текст кнопки не станет "SkyPro"
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
    )
    
    # Получить обновленный текст кнопки
    updated_button = driver.find_element(By.ID, "updatingButton")
    button_text = updated_button.text
    
    # Вывести текст кнопки в консоль
    print(f'Текст кнопки: "{button_text}"')
    
    # Проверить, что текст соответствует ожидаемому
    if button_text == "SkyPro":
        print("✓ Текст кнопки успешно изменен на 'SkyPro'")
    else:
        print(f"✗ Ошибка: текст кнопки '{button_text}' не соответствует ожидаемому 'SkyPro'")
    
except Exception as e:
    print(f"Произошла ошибка: {e}")
    
finally:
    # Закрыть браузер
    driver.quit()
    print("Браузер закрыт")