from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from typing import Any, List, Tuple, Optional

class BasePage:
    """Базовый класс для всех страниц проекта"""
    
    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        """
        Инициализация базовой страницы
        
        Args:
            driver: экземпляр веб-драйвера
            timeout: базовое время ожидания в секундах
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
    
    def find_element(self, locator: Tuple[By, str], timeout: Optional[int] = None) -> Any:
        """
        Поиск одного элемента на странице с ожиданием
        
        Args:
            locator: кортеж с (By.ЧТО_ИЩЕМ, "значение")
            timeout: время ожидания в секундах
            
        Returns:
            WebElement: найденный элемент
        """
        wait = WebDriverWait(self.driver, timeout) if timeout else self.wait
        return wait.until(EC.presence_of_element_located(locator))
    
    def click_element(self, locator: Tuple[By, str], timeout: Optional[int] = None) -> None:
        """
        Клик по элементу с ожиданием
        
        Args:
            locator: кортеж с (By.ЧТО_ИЩЕМ, "значение")
            timeout: время ожидания в секундах
        """
        element = self.find_element(locator, timeout)
        element.click()
    
    def input_text(self, locator: Tuple[By, str], text: str, timeout: Optional[int] = None) -> None:
        """
        Ввод текста в поле с предварительной очисткой
        
        Args:
            locator: кортеж с (By.ЧТО_ИЩЕМ, "значение")
            text: текст для ввода
            timeout: время ожидания в секундах
        """
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator: Tuple[By, str], timeout: Optional[int] = None) -> str:
        """
        Получение текста элемента
        
        Args:
            locator: кортеж с (By.ЧТО_ИЩЕМ, "значение")
            timeout: время ожидания в секундах
            
        Returns:
            str: текст элемента
        """
        element = self.find_element(locator, timeout)
        return element.text
    
    def is_element_visible(self, locator: Tuple[By, str], timeout: int = 5) -> bool:
        """
        Проверка видимости элемента на странице
        
        Args:
            locator: кортеж с (By.ЧТО_ИЩЕМ, "значение")
            timeout: время ожидания в секундах
            
        Returns:
            bool: True если элемент видим
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False