import pytest
import allure
from ..pages.inventory_page import InventoryPage
from ..pages.login_page import LoginPage

@allure.feature("Интернет-магащзин Swag Labs")
@allure.story("Покупка товаров")
@allure.title("Успешныц вход и добавление товаров в корзину")
def test_buy_backpack(driver):
    login_page = LoginPage(driver).open_page()
    inventory_page = login_page.login_success("standard_user", "secret_sauce")
    assert inventory_page.is_header_visible(), "Баг! заголовок страницы не соответствует"
    inventory_page.add_backpack_to_cart()
    assert inventory_page.get_cart_count() == "1", "Баг! Товар не добавился в корзину"

@allure.feature("Интернет-магазин Swag Labs")
@allure.story("Покупка товаров")
@allure.title("Успешныц вход и добавление товаров в корзину")
def test_buy_all_items(driver):
    login_page = LoginPage(driver).open_page()

    inventory_page = login_page.login_success("standard_user", "secret_sauce")

    all_count = len(inventory_page.get_all_carts())

    inventory_page.add_all_items_to_cart()

    assert int(inventory_page.get_cart_count()) == all_count, "Баг: не все товары добавились в корзину!"

@allure.feature("Интернет-магазин Swag Labs")
@allure.story("Корзина")
@allure.title("Проверка целостности данных: каталог - корзина")
def test_cart_items_match(driver):
    login_page = LoginPage(driver).open_page()
    inventory_page = login_page.login_success("standard_user", "secret_sauce")

    expected_names = inventory_page.get_all_items_names()
    inventory_page.add_all_items_to_cart()
    cart_page = inventory_page.go_to_cart()

    actual_names = cart_page.get_cart_item_name()
    with allure.step('Сверяем списки товаров'):
        assert expected_names == actual_names, "Баг: Названия товаров в корзине не совпадает"