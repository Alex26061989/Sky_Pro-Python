from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    """
    Page Object для страницы авторизации.
    """
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
        # Локаторы
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR, "[data-test='error']")
    
    def open(self):
        """Открыть сайт магазина."""
        self.driver.get("https://www.saucedemo.com/")
        return self
    
    def enter_username(self, username):
        """Ввести логин."""
        self.driver.find_element(*self.username_input).send_keys(username)
        return self
    
    def enter_password(self, password):
        """Ввести пароль."""
        self.driver.find_element(*self.password_input).send_keys(password)
        return self
    
    def click_login(self):
        """Нажать кнопку входа."""
        self.driver.find_element(*self.login_button).click()
    
    def login(self, username, password):
        """Метод для быстрой авторизации."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()