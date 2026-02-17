import allure
from selenium.webdriver.remote.webdriver import WebDriver
from calculator_page import CalculatorPage


@allure.step("Открыть страницу калькулятора")
def open_calculator(driver: WebDriver) -> CalculatorPage:
    """Шаг открытия страницы калькулятора"""
    calc_page = CalculatorPage(driver)
    calc_page.open()
    
    allure.attach(
        name="URL",
        body=driver.current_url,
        attachment_type=allure.attachment_type.TEXT
    )
    
    return calc_page


@allure.step("Установить задержку {delay} секунд")
def set_calculator_delay(calc_page: CalculatorPage, delay: int) -> None:
    """Шаг установки задержки"""
    calc_page.set_delay(delay)
    
    allure.attach(
        name="Установленная задержка",
        body=f"{delay} секунд",
        attachment_type=allure.attachment_type.TEXT
    )


@allure.step("Выполнить вычисление: {expression}")
def perform_calculation(calc_page: CalculatorPage, expression: str) -> None:
    """Шаг выполнения вычисления"""
    for char in expression:
        calc_page.click_button(char)
        allure.attach(
            name=f"Нажата кнопка '{char}'",
            body=f"Текущее значение: {calc_page.get_current_display()}",
            attachment_type=allure.attachment_type.TEXT
        )


@allure.step("Ожидать результат и проверить что он равен {expected_result}")
def verify_calculation_result(
    calc_page: CalculatorPage, 
    expected_result: str, 
    timeout: int = 46
) -> str:
    """Шаг проверки результата вычисления"""
    actual_result = calc_page.get_result(timeout=timeout)
    
    assert actual_result == expected_result, \
        f"Ожидался результат '{expected_result}', получено '{actual_result}'"
    
    allure.attach(
        name="Результат вычисления",
        body=f"Ожидалось: {expected_result}\nФактически: {actual_result}",
        attachment_type=allure.attachment_type.TEXT
    )
    
    return actual_result