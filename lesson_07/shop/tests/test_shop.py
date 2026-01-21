import pytest


def test_shop_total_amount(checkout_page):
    """
    Тест интернет-магазина
    Проверяем, что итоговая сумма равна $58.29
    """
    
    # Тест уже выполнил предыдущие шаги через фикстуры:
    # 1. Открыл сайт магазина
    # 2. Авторизовался как standard_user
    # 3. Добавил в корзину товары (через main_page fixture)
    # 4. Перешел в корзину
    # 5. Нажал кнопку Checkout
    
    # 6. Заполнить форму своими данными
    checkout_page.fill_form("Иван", "Петров", "123456")
    
    # 7. Нажать Continue
    checkout_page.click_continue()
    
    # 8. Прочитать со страницы итоговую стоимость
    total_text = checkout_page.get_total_amount()
    print(f"Итоговая сумма на странице: {total_text}")
    
    # 9. Извлечь числовое значение
    total_value = checkout_page.extract_total_value()
    print(f"Числовое значение итоговой суммы: ${total_value}")
    
    # 10. Проверить (assert), что итоговая сумма равна $58.29
    expected_total = 58.29
    assert total_value == expected_total, \
        f"Ожидалась сумма ${expected_total}, получено ${total_value}"
    
    print(f"✅ Тест пройден! Итоговая сумма корректна: ${total_value}")