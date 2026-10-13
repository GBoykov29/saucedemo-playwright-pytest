from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_add_item_to_cart(page):

    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_backpack_to_cart()

    assert inventory_page.cart_badge.inner_text() == "1"


def test_remove_item_from_cart(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_backpack_to_cart()

    inventory_page.remove_backpack_from_cart()

    assert not inventory_page.cart_badge.is_visible()
