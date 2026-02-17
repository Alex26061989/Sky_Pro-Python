import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Optional


@allure.step("Проверить, что элемент отображается на странице")
def assert_element_visible(
    element: WebElement, 
    element_name: str = "Элемент"
) -> None:
    """
    Проверка видимости элемента
    
    Args:
        element: веб-элемент
        element_name: название элемента для отчета
    """
    with allure.step(f"{element_name} должен быть видим"):
        assert element.is_displayed(), f"{element_name} не виден на странице"


@allure.step("Проверить текст элемента")
def assert_element_text(
    element: WebElement, 
    expected_text: str, 
    element_name: str = "Элемент"
) -> None:
    """
    Проверка текста элемента
    
    Args:
        element: веб-элемент
        expected_text: ожидаемый текст
        element_name: название элемента для отчета
    """
    actual_text = element.text
    with allure.step(f"Текст {element_name} должен быть '{expected_text}'"):
        assert actual_text == expected_text, \
            f"Текст не совпадает. Ожидалось: '{expected_text}', получено: '{actual_text}'"


@allure.step("Проверить, что URL содержит '{expected_part}'")
def assert_url_contains(
    driver: WebDriver, 
    expected_part: str, 
    message: Optional[str] = None
) -> None:
    """
    Проверка, что URL содержит определенную часть
    
    Args:
        driver: веб-драйвер
        expected_part: ожидаемая часть URL
        message: сообщение об ошибке
    """
    current_url = driver.current_url
    with allure.step(f"Текущий URL: {current_url}"):
        assert expected_part in current_url, \
            message or f"URL не содержит '{expected_part}'. Текущий URL: {current_url}"


@allure.step("Проверить количество элементов")
def assert_count(
    items: list, 
    expected_count: int, 
    items_name: str = "Элементов"
) -> None:
    """
    Проверка количества элементов
    
    Args:
        items: список элементов
        expected_count: ожидаемое количество
        items_name: название элементов для отчета
    """
    actual_count = len(items)
    with allure.step(f"{items_name} должно быть {expected_count}"):
        assert actual_count == expected_count, \
            f"{items_name} должно быть {expected_count}, но найдено {actual_count}"