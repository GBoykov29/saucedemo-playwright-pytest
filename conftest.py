import pytest
from pages.login_page import LoginPage


@pytest.fixture
def logged_in_page(page):
    """Тази фикстура автоматично отваря сайта и прави вход за тестовете, които я изискват."""
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    return page
