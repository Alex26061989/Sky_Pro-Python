import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    """
    Фикстура для параметризации браузеров.
    Можно запускать тесты в разных браузерах.
    
    Args:
        request: объект запроса pytest
        
    Returns:
        WebDriver: экземпляр драйвера
    """
    browser = request.param
    
    with allure.step(f"Запуск браузера {browser}"):
        if browser == "chrome":
            driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install())
            )
        elif browser == "firefox":
            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install())
            )
        else:
            raise ValueError(f"Неподдерживаемый браузер: {browser}")
        
        driver.maximize_window()
    
    yield driver
    
    with allure.step(f"Закрытие браузера {browser}"):
        driver.quit()


@pytest.fixture
def chrome_driver():
    """Фикстура только для Chrome."""
    with allure.step("Запуск Chrome браузера"):
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )
        driver.maximize_window()
    
    yield driver
    
    with allure.step("Закрытие Chrome браузера"):
        driver.quit()


@pytest.fixture
def firefox_driver():
    """Фикстура только для Firefox."""
    with allure.step("Запуск Firefox браузера"):
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )
        driver.maximize_window()
    
    yield driver
    
    with allure.step("Закрытие Firefox браузера"):
        driver.quit()