from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    # Перейти на страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    print("Страница загружена")
    
    # Дождаться загрузки всех картинок
    # Ждем, пока не исчезнет индикатор загрузки и появятся все изображения
    print("Ожидаем загрузки изображений...")
    
    # Вариант A: Ждем исчезновения спиннера загрузки (если есть)
    try:
        spinner = WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.ID, "spinner"))
        )
        print("Индикатор загрузки исчез")
    except:
        print("Индикатор загрузки не найден или уже исчез")
    
    # Вариант B: Ждем, пока все изображения не будут загружены
    # Проверяем, что у всех img элементов есть атрибут src, и он не пустой
    images = WebDriverWait(driver, 15).until(
        lambda d: len(d.find_elements(By.TAG_NAME, "img")) >= 4  # Должно быть минимум 4 картинки
    )
    
    print(f"Найдено изображений: {len(driver.find_elements(By.TAG_NAME, 'img'))}")
    
    # Получить все изображения
    all_images = driver.find_elements(By.TAG_NAME, "img")
    
    if len(all_images) >= 3:
        # Получить значение атрибута src у 3-й картинки (индекс 2)
        third_image = all_images[2]
        src_value = third_image.get_attribute("src")
        
        # Вывести значение в консоль
        print(f"Атрибут src 3-й картинки: {src_value}")
        
        # Дополнительная проверка
        if src_value and src_value != "":
            print("✓ Атрибут src успешно получен")
        else:
            print("✗ Атрибут src пустой или не найден")
    else:
        print(f"✗ Недостаточно изображений. Найдено только: {len(all_images)}")
        
except Exception as e:
    print(f"Произошла ошибка: {e}")
    
finally:
    # Закрыть браузер
    driver.quit()
    print("Браузер закрыт")