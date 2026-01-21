import pytest


def test_slow_calculator_45_seconds():
    """
    Тест калькулятора с задержкой 45 секунд
    Шаги:
    1. Открыть страницу калькулятора
    2. Ввести значение 45 в поле задержки
    3. Нажать кнопки: 7, +, 8, =
    4. Проверить, что в окне отобразится результат 15 через 45 секунд
    """
    # Фикстуры будут подставлены автоматически
    pass


def test_calculator_7_plus_8(calculator_page):
    """Основной тест калькулятора"""
    
    # 1. Страница уже открыта через фикстуру calculator_page
    
    # 2. Ввести значение 45 в поле задержки
    calculator_page.set_delay(45)
    
    # 3. Нажать кнопки: 7, +, 8, =
    calculator_page.click_7()
    calculator_page.click_plus()
    calculator_page.click_8()
    calculator_page.click_equals()
    
    # 4. Проверить (assert), что в окне отобразится результат 15 через 45 секунд
    # Ждем до 46 секунд (45 + 1 запас)
    result_found = calculator_page.wait_for_result("15", timeout=46)
    
    assert result_found, "Результат 15 не появился на экране в течение 46 секунд"
    
    # Получаем финальный текст с экрана для точной проверки
    final_result = calculator_page.get_screen_text()
    
    assert final_result == "15", f"Ожидался результат 15, но получено: {final_result}"