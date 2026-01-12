from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_task():
    # 1. Открыть браузер FireFox
    driver = webdriver.Firefox()
    
    try:
        # 2. Перейти на страницу логина
        driver.get('http://the-internet.herokuapp.com/login')
        print("Открыта страница логина")
        
        # Инициализируем ожидание
        wait = WebDriverWait(driver, 10)
        
        # 3. Ввести username
        username_field = wait.until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        username_field.send_keys("tomsmith")
        print("Введен username: tomsmith")
        
        # 4. Ввести password
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("SuperSecretPassword!")
        print("Введен password: SuperSecretPassword!")
        
        # 5. Нажать кнопку Login
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        print("Нажата кнопка Login")
        
        # 6. Вывести текст с зеленой плашки в консоль
        # Ждем появления сообщения об успехе
        success_message = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success"))
        )
        
        # Получаем полный текст (может содержать "×" для закрытия)
        flash_text = success_message.text
        
        # Очищаем текст от символа закрытия
        cleaned_text = flash_text.replace("×", "").strip()
        
        print("\n" + "="*50)
        print("ТЕКСТ С ЗЕЛЕНОЙ ПЛАШКИ:")
        print(cleaned_text)
        print("="*50)
        
        # Даем время увидеть результат
        import time
        time.sleep(2)
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        # 7. Закрыть браузер
        driver.quit()
        print("\nБраузер закрыт")

