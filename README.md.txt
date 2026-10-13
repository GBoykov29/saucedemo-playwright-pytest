# SauceDemo Playwright Pytest Automation Framework

A professional UI automation testing framework built with **Python**, **Playwright**, and **Pytest**, following the **Page Object Model (POM)** design pattern. The project automates end-to-end (E2E) test scenarios for the [SauceDemo](https://www.saucedemo.com/) online shop.

---

## 🚀 Features

* **Page Object Model (POM):** Clean separation of test logic and web element locators for high maintainability.
* **Pytest Fixtures:** Centralized environment setup and teardown, including reusable authentication fixtures (`conftest.py`).
* **Comprehensive Test Scenarios:**
  * Successful and negative login flows (including parametrized tests and locked-out user validation).
  * Inventory sorting and cart management (adding and removing items).
  * E2E checkout workflow with validation checks.
  * Handling multi-tab browsing (`expect_page`) for social media links.
* **HTML Reporting:** Integrated `pytest-html` for generating visual test execution reports.

---

## Tech Stack

* **Language:** Python 3.13+
* **Automation Tool:** Playwright for Python
* **Test Framework:** Pytest
* **Reporting:** pytest-html

---

##  Project Structure


saucedemo-playwright-pytest/
│
├── pages/                  # Page Object Model classes
│   ├── checkout_page.py
│   ├── inventory_page.py
│   └── login_page.py
│
├── tests/                  # Test suites
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_login.py
│   ├── test_login_parametrized.py
│   ├── test_social.py
│   └── test_sorting.py
│
├── .gitignore              # Ignored files (cache, reports)
├── conftest.py             # Global fixtures & configurations
├── requirements.txt        # Project dependencies
└── report.html             # Generated test execution report




Installation & Setup
Clone the repository:

Bash
git clone [https://github.com/YOUR-USERNAME/saucedemo-playwright-pytest.git](https://github.com/YOUR-USERNAME/saucedemo-playwright-pytest.git)
cd saucedemo-playwright-pytest
Install dependencies:
Bash
pip install -r requirements.txt

Install Playwright browsers:
Bash
playwright install

 Running Tests
To run all tests and automatically generate an HTML report, execute the following command in your terminal:
Bash
pytest --html=report.html --self-contained-html