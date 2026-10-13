import pytest
from pages.login_page import LoginPage


def test_successful_login(logged_in_page):

    assert logged_in_page.url == "https://www.saucedemo.com/inventory.html"


def test_invalid_password(page):

    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "wrong_password")

    assert login_page.error_message.is_visible()
    assert "Username and password do not match" in login_page.error_message.inner_text()


def test_locked_out_user(page):

    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("locked_out_user", "secret_sauce")

    assert login_page.error_message.is_visible()
    assert "Sorry, this user has been locked out" in login_page.error_message.inner_text()
