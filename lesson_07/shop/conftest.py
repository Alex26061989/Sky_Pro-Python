import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture(scope="function")
def driver():
    """Фикстура для создания драйвера Firefox"""
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login_page(driver):
    """Фикстура для страницы авторизации"""
    page = LoginPage(driver)
    page.open()
    return page


@pytest.fixture(scope="function")
def main_page(login_page):
    """Фикстура для главной страницы (после авторизации)"""
    # Авторизуемся
    login_page.login("standard_user", "secret_sauce")
    return MainPage(login_page.driver)


@pytest.fixture(scope="function")
def cart_page(main_page):
    """Фикстура для страницы корзины"""
    main_page.go_to_cart()
    return CartPage(main_page.driver)


@pytest.fixture(scope="function")
def checkout_page(cart_page):
    """Фикстура для страницы оформления заказа"""
    cart_page.click_checkout()
    return CheckoutPage(cart_page.driver)