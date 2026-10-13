from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage


def test_complete_checkout_flow(logged_in_page):
    # 1. Добавяме раницата и отиваме в количката
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_backpack_to_cart()
    inventory_page.cart_icon.click()

    # 2. Преминаваме през целия процес на плащане
    checkout_page = CheckoutPage(logged_in_page)
    checkout_page.start_checkout()
    checkout_page.fill_shipping_info("Ivan", "Ivanov", "1000")
    checkout_page.finish_checkout()

    assert checkout_page.complete_header.inner_text() == "Thank you for your order!"


def test_checkout_missing_first_name(logged_in_page):

    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_backpack_to_cart()
    inventory_page.cart_icon.click()

    checkout_page = CheckoutPage(logged_in_page)

    checkout_page.start_checkout()

    checkout_page.continue_button.click()

    assert checkout_page.error_message.inner_text() == "Error: First Name is required"
