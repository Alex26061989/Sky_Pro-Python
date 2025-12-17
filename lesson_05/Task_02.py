from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Открыть браузер Google Chrome.
driver = webdriver.Chrome()

# Перейти на страницу.
driver.get('http://uitestingplayground.com/dynamicid')

sleep(5)

# Кликнуть на синюю кнопку.
blue_button_selector = "button.btn-primary"

wait = WebDriverWait(driver, 10)
blue_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, blue_button_selector))
    )
blue_button.click()