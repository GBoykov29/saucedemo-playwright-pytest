from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_sort_products_z_to_a(logged_in_page):

    inventory_page = InventoryPage(logged_in_page)
    inventory_page.sort_products("za")

    names = inventory_page.item_names.all_inner_texts()

 
    sorted_names = sorted(names, reverse=True)

    assert names == sorted_names
