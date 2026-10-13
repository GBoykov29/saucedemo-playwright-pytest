class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.add_to_cart_sauce_labs_backpack = page.locator(
            "#add-to-cart-sauce-labs-backpack")
        self.remove_sauce_labs_backpack = page.locator(
            "#remove-sauce-labs-backpack")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_icon = page.locator(".shopping_cart_link")

        self.twitter_link = page.locator("[data-test='social-x']")

        self.sort_dropdown = page.locator(
            "[data-test='product-sort-container']")
        self.item_names = page.locator(".inventory_item_name")

    def add_backpack_to_cart(self):
        self.add_to_cart_sauce_labs_backpack.click()

    def remove_backpack_from_cart(self):
        self.remove_sauce_labs_backpack.click()

    def sort_products(self, sort_option):
        self.sort_dropdown.select_option(sort_option)
