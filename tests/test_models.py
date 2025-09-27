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

    def test_product_str_representation(self):
        """Тест строкового представления продукта"""
        product = Product("Телефон", "Смартфон", 50000.0, 10)

        expected_str = "Телефон, 50000.0 руб. Остаток: 10 шт."
        assert str(product) == expected_str

    def test_product_addition(self):
        """Тест сложения двух продуктов"""
        product1 = Product("Телефон", "Смартфон", 50000.0, 10)
        product2 = Product("Ноутбук", "Игровой ноутбук", 100000.0, 5)

        total_value = product1 + product2
        expected_value = (50000.0 * 10) + (100000.0 * 5)

        assert total_value == expected_value
        assert total_value == 1000000.0  # 500000 + 500000

    def test_product_addition_with_different_products(self):
        """Тест сложения продуктов с разными ценами и количествами"""
        product1 = Product("Товар1", "Описание1", 100.0, 3)
        product2 = Product("Товар2", "Описание2", 200.0, 2)

        total_value = product1 + product2
        expected_value = (100.0 * 3) + (200.0 * 2)

        assert total_value == expected_value
        assert total_value == 700.0

    def test_product_addition_invalid_type(self):
        """Тест сложения продукта с неверным типом"""
        product = Product("Телефон", "Смартфон", 50000.0, 10)

        with pytest.raises(TypeError):
            product + "не продукт"

    def test_product_initialization(self):
        """Тест корректной инициализации продукта"""
        product = Product("Телефон", "Смартфон", 50000.0, 10)

        assert product.name == "Телефон"
        assert product.description == "Смартфон"
        assert product.price == 50000.0
        assert product.quantity == 10


class TestCategory:
    """Тесты для класса Category"""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом"""
        Category.category_count = 0
        Category.product_count = 0

    def test_category_str_representation(self):
        """Тест строкового представления категории"""
        product1 = Product("Телефон", "Смартфон", 50000.0, 10)
        product2 = Product("Ноутбук", "Игровой ноутбук", 100000.0, 5)

        category = Category("Электроника", "Гаджеты", [product1, product2])

        expected_str = "Электроника, количество продуктов: 15 шт."
        assert str(category) == expected_str

    def test_category_str_empty_products(self):
        """Тест строкового представления категории без продуктов"""
        category = Category("Книги", "Художественная литература")

        expected_str = "Книги, количество продуктов: 0 шт."
        assert str(category) == expected_str

    def test_category_str_single_product(self):
        """Тест строкового представления категории с одним продуктом"""
        product = Product("Телефон", "Смартфон", 50000.0, 3)
        category = Category("Электроника", "Гаджеты", [product])

        expected_str = "Электроника, количество продуктов: 3 шт."
        assert str(category) == expected_str

    def test_products_property_uses_str(self):
        """Тест что геттер products использует __str__ продуктов"""
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        category = Category("Электроника", "Гаджеты", [product])

        products_str = category.products
        expected_str = "Телефон, 50000.0 руб. Остаток: 10 шт."

        assert products_str == expected_str

    def test_get_total_quantity_method(self):
        """Тест метода get_total_quantity"""
        product1 = Product("Товар1", "Описание1", 100.0, 3)
        product2 = Product("Товар2", "Описание2", 200.0, 2)
        category = Category("Категория", "Описание", [product1, product2])

        total_quantity = category.get_total_quantity()
        assert total_quantity == 5


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

    def test_loaded_products_have_str_method(self):
        """Тест что загруженные продукты имеют строковое представление"""
        categories = load_data_from_json(str(self.json_path))

        product = categories[0].get_products_list()[0]
        product_str = str(product)

        assert "Samsung Galaxy S24" in product_str
        assert "89990.0 руб." in product_str
        assert "15 шт." in product_str

    def test_loaded_categories_have_str_method(self):
        """Тест что загруженные категории имеют строковое представление"""
        categories = load_data_from_json(str(self.json_path))

        category_str = str(categories[0])
        assert "Смартфоны, количество продуктов: 15 шт." == category_str