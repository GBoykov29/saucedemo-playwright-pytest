from pages.inventory_page import InventoryPage


def test_social_media_link(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)

    with logged_in_page.context.expect_page() as new_tab_info:
        inventory_page.twitter_link.click()

    new_page = new_tab_info.value

    new_page.wait_for_load_state()

    assert "twitter.com" in new_page.url or "x.com" in new_page.url
