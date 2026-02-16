from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from typing import Optional


class LoginPage(BasePage):
    """
    Класс для работы со страницей авторизации.
    """
    
    # Локаторы элементов
    USERNAME_INPUT: tuple = (By.ID, "user-name")
    PASSWORD_INPUT: tuple = (By.ID, "password")
    LOGIN_BUTTON: tuple = (By.ID, "login-button")
    ERROR_MESSAGE: tuple = (By.CSS_SELECTOR, "[data-test='error']")
    
    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы авторизации"""
        super().__init__(driver)
    
    def open(self) -> 'LoginPage':
        """Открыть страницу авторизации"""
        self.driver.get("https://www.saucedemo.com/")
        return self
    
    def enter_username(self, username: str) -> 'LoginPage':
        """Ввести имя пользователя"""
        self.input_text(self.USERNAME_INPUT, username)
        return self
    
    def enter_password(self, password: str) -> 'LoginPage':
        """Ввести пароль"""
        self.input_text(self.PASSWORD_INPUT, password)
        return self
    
    def click_login(self) -> None:
        """Нажать кнопку входа"""
        self.click_element(self.LOGIN_BUTTON)
    
    def login(self, username: str, password: str) -> None:
        """Выполнить полный процесс авторизации"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
    
    def get_error_message(self) -> Optional[str]:
        """Получить текст сообщения об ошибке"""
        if self.is_element_visible(self.ERROR_MESSAGE, timeout=3):
            return self.get_text(self.ERROR_MESSAGE)
        return None
    
    def is_login_successful(self) -> bool:
        """Проверить, успешно ли выполнен вход"""
        return "inventory" in self.driver.current_url