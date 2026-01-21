from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    """Page Object для главной страницы магазина"""
    
    # Локаторы
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn_inventory")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_COUNT = (By.CLASS_NAME, "shopping_cart_badge")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def is_loaded(self):
        """Проверить, что страница загрузилась"""
        try:
            self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
            )
            return True
        except:
            return False
    
    def add_item_to_cart_by_name(self, item_name):
        """Добавить товар в корзину по названию"""
        items = self.driver.find_elements(*self.INVENTORY_ITEMS)
        
        for item in items:
            name_element = item.find_element(*self.ITEM_NAME)
            if name_element.text == item_name:
                add_button = item.find_element(*self.ADD_TO_CART_BUTTON)
                add_button.click()
                return True
        
        return False
    
    def add_items_to_cart(self, item_names):
        """Добавить несколько товаров в корзину"""
        added_items = []
        for item_name in item_names:
            if self.add_item_to_cart_by_name(item_name):
                added_items.append(item_name)
        return added_items
    
    def get_cart_count(self):
        """Получить количество товаров в корзине"""
        try:
            element = self.driver.find_element(*self.CART_COUNT)
            return int(element.text)
        except:
            return 0
    
    def go_to_cart(self):
        """Перейти в корзину"""
        element = self.wait.until(
            EC.element_to_be_clickable(self.CART_ICON)
        )
        element.click()