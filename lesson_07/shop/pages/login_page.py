from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Page Object для страницы авторизации"""
    
    # Локаторы
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message-container")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open(self):
        """Открыть сайт магазина"""
        self.driver.get("https://www.saucedemo.com/")
    
    def enter_username(self, username):
        """Ввести логин"""
        element = self.wait.until(
            EC.presence_of_element_located(self.USERNAME_INPUT)
        )
        element.clear()
        element.send_keys(username)
    
    def enter_password(self, password):
        """Ввести пароль"""
        element = self.driver.find_element(*self.PASSWORD_INPUT)
        element.clear()
        element.send_keys(password)
    
    def click_login(self):
        """Нажать кнопку входа"""
        element = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        element.click()
    
    def login(self, username, password):
        """Полный процесс авторизации"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
    
    def get_error_message(self):
        """Получить текст ошибки авторизации"""
        try:
            element = self.driver.find_element(*self.ERROR_MESSAGE)
            return element.text
        except:
            return None