import pytest
from selenium import webdriver
from pages.calculator_page import CalculatorPage


@pytest.fixture(scope="function")
def driver():
    """Фикстура для создания драйвера Google Chrome"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def calculator_page(driver):
    """Фикстура для создания Page Object калькулятора"""
    page = CalculatorPage(driver)
    page.open()
    return page