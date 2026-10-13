from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_sort_products_z_to_a(logged_in_page):

    inventory_page = InventoryPage(logged_in_page)
    inventory_page.sort_products("za")

    # 3. Взимаме списъка с всички имена на продукти след сортирането
    names = inventory_page.item_names.all_inner_texts()

    # 4. ПРОВЕРКА: Проверяваме дали списъкът е сортиран обратно на азбучен ред (Z до A)
    # Сравняваме го с предварително сортиран списък в Python в обратен ред
    sorted_names = sorted(names, reverse=True)

    assert names == sorted_names
