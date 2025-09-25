import pytest
import sys
import os
import json
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.models import Product, Category, load_data_from_json


def create_test_json_file():
    """Создает тестовый JSON файл в корне проекта"""
    test_data = [
        {
            "name": "Смартфоны",
            "description": "Мобильные телефоны и смартфоны",
            "products": [
                {
                    "name": "Samsung Galaxy S24",
                    "description": "Флагманский смартфон Samsung",
                    "price": 89990.0,
                    "quantity": 15
                }
            ]
        }
    ]

    json_path = project_root / "products.json"

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(test_data, f, ensure_ascii=False, indent=2)

    return json_path


class TestProduct:
    """Тесты для класса Product"""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом"""
        Category.category_count = 0
        Category.product_count = 0

    def test_product_initialization(self):
        """Тест корректной инициализации продукта"""
        product = Product("Телефон", "Смартфон", 50000.0, 10)

        assert product.name == "Телефон"
        assert product.description == "Смартфон"
        assert product.price == 50000.0  # Используем геттер
        assert product.quantity == 10

    def test_product_price_getter_setter(self):
        """Тест геттера и сеттера для цены"""
        product = Product("Телефон", "Смартфон", 50000.0, 10)

        # Проверяем геттер
        assert product.price == 50000.0

        # Проверяем сеттер с корректным значением
        product.price = 45000.0
        assert product.price == 45000.0

        # Проверяем сеттер с некорректным значением (цена не должна измениться)
        product.price = -1000.0
        assert product.price == 45000.0  # Цена осталась прежней

    def test_product_price_negative_value(self, capsys):
        """Тест обработки отрицательной цены"""
        product = Product("Телефон", "Смартфон", 50000.0, 10)

        product.price = -1000.0
        captured = capsys.readouterr()

        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 50000.0  # Цена не изменилась

    def test_product_price_zero_value(self, capsys):
        """Тест обработки нулевой цены"""
        product = Product("Телефон", "Смартфон", 50000.0, 10)

        product.price = 0
        captured = capsys.readouterr()

        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 50000.0  # Цена не изменилась

    def test_new_product_class_method(self):
        """Тест класс-метода new_product"""
        product_data = {
            "name": "Ноутбук",
            "description": "Игровой ноутбук",
            "price": 100000.0,
            "quantity": 5
        }

        product = Product.new_product(product_data)

        assert isinstance(product, Product)
        assert product.name == "Ноутбук"
        assert product.description == "Игровой ноутбук"
        assert product.price == 100000.0
        assert product.quantity == 5


class TestCategory:
    """Тесты для класса Category"""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом"""
        Category.category_count = 0
        Category.product_count = 0

    def test_private_products_attribute(self):
        """Тест приватности атрибута продуктов"""
        category = Category("Электроника", "Гаджеты")

        # Проверяем, что атрибут __products действительно приватный
        with pytest.raises(AttributeError):
            _ = category.__products

    def test_add_product_method(self):
        """Тест метода add_product"""
        category = Category("Электроника", "Гаджеты")
        product = Product("Телефон", "Смартфон", 50000.0, 10)

        initial_count = Category.product_count
        category.add_product(product)

        # Проверяем, что продукт добавлен и счетчик увеличился
        assert Category.product_count == initial_count + 1

    def test_add_product_invalid_type(self):
        """Тест добавления неверного типа в add_product"""
        category = Category("Электроника", "Гаджеты")

        with pytest.raises(TypeError):
            category.add_product("не продукт")

    def test_products_property(self):
        """Тест геттера products"""
        product1 = Product("Телефон", "Смартфон", 50000.0, 10)
        product2 = Product("Ноутбук", "Игровой ноутбук", 100000.0, 5)

        category = Category("Электроника", "Гаджеты", [product1, product2])

        products_str = category.products

        assert isinstance(products_str, str)
        assert "Телефон, 50000.0 руб. Остаток: 10 шт." in products_str
        assert "Ноутбук, 100000.0 руб. Остаток: 5 шт." in products_str

    def test_products_property_format(self):
        """Тест формата вывода геттера products"""
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        category = Category("Электроника", "Гаджеты", [product])

        products_str = category.products
        expected_format = "Телефон, 50000.0 руб. Остаток: 10 шт."

        assert products_str == expected_format

    def test_get_products_list_method(self):
        """Тест метода get_products_list"""
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        category = Category("Электроника", "Гаджеты", [product])

        products_list = category.get_products_list()

        assert isinstance(products_list, list)
        assert len(products_list) == 1
        assert products_list[0] == product


class TestJSONLoading:
    """Тесты загрузки данных из JSON"""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом"""
        Category.category_count = 0
        Category.product_count = 0
        self.json_path = create_test_json_file()

    def teardown_method(self):
        """Удаляем тестовый файл после каждого теста"""
        if os.path.exists(self.json_path):
            os.remove(self.json_path)

    def test_load_data_uses_new_product_method(self):
        """Тест что загрузка использует класс-метод new_product"""
        categories = load_data_from_json(str(self.json_path))

        assert len(categories) > 0
        assert len(categories[0].get_products_list()) > 0
        assert isinstance(categories[0].get_products_list()[0], Product)