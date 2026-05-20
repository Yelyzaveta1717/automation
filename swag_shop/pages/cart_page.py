import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class CartPage(BasePage):
    CART_ITEM_NAMES = (By.CLASS_NAME, 'inventory_item_name')

    @allure.step("Получаем список названий товаров в корщине")
    def get_cart_item_name(self):
        return self.get_all_texts(self.CART_ITEM_NAMES)
