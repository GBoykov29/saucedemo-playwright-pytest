import pytest
from pages.login_page import LoginPage


test_data = [
    ("standard_user", "secret_sauce", True),
    ("locked_out_user", "secret_sauce", False),
    ("standard_user", "wrong_password_123", False),
]


@pytest.mark.parametrize("username, password, should_succeed", test_data)
def test_login_flow(page, username, password, should_succeed):
    login_page = LoginPage(page)
    login_page.navigate()

    login_page.login(username, password)

    if should_succeed:

        assert page.url == "https://www.saucedemo.com/inventory.html"
    else:

        assert login_page.error_message.is_visible()
