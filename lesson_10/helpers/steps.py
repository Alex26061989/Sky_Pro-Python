import allure
from selenium.webdriver.remote.webdriver import WebDriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from typing import List


@allure.step("Открыть сайт и авторизоваться под пользователем {username}")
def login(driver: WebDriver, username: str, password: str) -> LoginPage:
    """Шаг авторизации на сайте"""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)
    assert login_page.is_login_successful(), "Авторизация не удалась"
    return login_page


@allure.step("Добавить товары в корзину: {products}")
def add_products_to_cart(driver: WebDriver, products: List[str]) -> InventoryPage:
    """Шаг добавления товаров в корзину"""
    inventory_page = InventoryPage(driver)
    inventory_page.add_products_to_cart(products)
    
    cart_count = inventory_page.get_cart_item_count()
    assert cart_count == len(products), \
        f"Ожидалось {len(products)} товаров, получено {cart_count}"
    
    allure.attach(
        name="Добавленные товары",
        body="\n".join(products),
        attachment_type=allure.attachment_type.TEXT
    )
    
    return inventory_page


@allure.step("Перейти в корзину и начать оформление заказа")
def go_to_cart_and_checkout(driver: WebDriver) -> CartPage:
    """Шаг перехода в корзину и нажатия кнопки Checkout"""
    inventory_page = InventoryPage(driver)
    inventory_page.go_to_cart()
    
    cart_page = CartPage(driver)
    cart_page.click_checkout()
    
    assert "checkout-step-one" in driver.current_url, \
        "Не удалось перейти к оформлению заказа"
    
    return cart_page


@allure.step("Заполнить информацию о доставке: {first_name} {last_name}, {postal_code}")
def fill_shipping_info(
    driver: WebDriver, 
    first_name: str, 
    last_name: str, 
    postal_code: str
) -> CheckoutPage:
    """Шаг заполнения информации о доставке"""
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_shipping_info(first_name, last_name, postal_code)
    checkout_page.click_continue()
    
    assert "checkout-step-two" in driver.current_url, \
        "Не удалось перейти к обзору заказа"
    
    return checkout_page


@allure.step("Проверить итоговую сумму заказа (ожидаем ${expected_total})")
def verify_total_price(driver: WebDriver, expected_total: float) -> float:
    """Шаг проверки итоговой суммы"""
    checkout_page = CheckoutPage(driver)
    actual_total = checkout_page.get_total_price()
    
    assert actual_total == expected_total, \
        f"Ожидалась сумма ${expected_total}, получено ${actual_total}"
    
    allure.attach(
        name="Итоговая сумма",
        body=f"Ожидалось: ${expected_total}\nФактически: ${actual_total}",
        attachment_type=allure.attachment_type.TEXT
    )
    
    return actual_total