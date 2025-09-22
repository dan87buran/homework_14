import pytest
import sys
import os
import json
from pathlib import Path

# Добавляем корень проекта в Python path
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
                },
                {
                    "name": "Xiaomi Redmi Note 13",
                    "description": "Бюджетный смартфон с хорошей камерой",
                    "price": 24990.0,
                    "quantity": 25
                }
            ]
        },
        {
            "name": "Ноутбуки",
            "description": "Портативные компьютеры",
            "products": [
                {
                    "name": "ASUS ROG Strix",
                    "description": "Игровой ноутбук",
                    "price": 149990.0,
                    "quantity": 8
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

    def test_product_initialization(self):
        """Тест корректной инициализации продукта"""
        product = Product("Телефон", "Смартфон", 50000.0, 10)

        assert product.name == "Телефон"
        assert product.description == "Смартфон"
        assert product.price == 50000.0
        assert product.quantity == 10

    def test_product_attributes_types(self):
        """Тест типов атрибутов продукта"""
        product = Product("Ноутбук", "Игровой ноутбук", 100000.0, 5)

        assert isinstance(product.name, str)
        assert isinstance(product.description, str)
        assert isinstance(product.price, float)
        assert isinstance(product.quantity, int)


class TestCategory:
    """Тесты для класса Category"""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом"""
        Category.category_count = 0
        Category.product_count = 0

    def test_category_initialization(self):
        """Тест корректной инициализации категории"""
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        category = Category("Электроника", "Гаджеты", [product])

        assert category.name == "Электроника"
        assert category.description == "Гаджеты"
        assert len(category.products) == 1
        assert category.products[0].name == "Телефон"

    def test_category_empty_products(self):
        """Тест создания категории без товаров"""
        category = Category("Книги", "Художественная литература")

        assert category.name == "Книги"
        assert category.description == "Художественная литература"
        assert category.products == []

    def test_category_count(self):
        """Тест подсчета количества категорий"""
        initial_count = Category.category_count
        category1 = Category("Категория 1", "Описание 1")
        category2 = Category("Категория 2", "Описание 2")

        assert Category.category_count == initial_count + 2
        assert Category.category_count == 2

    def test_product_count(self):
        """Тест подсчета количества товаров"""
        initial_count = Category.product_count

        product1 = Product("Товар 1", "Описание 1", 100, 1)
        product2 = Product("Товар 2", "Описание 2", 200, 2)
        product3 = Product("Товар 3", "Описание 3", 300, 3)

        category1 = Category("Категория 1", "Описание 1", [product1, product2])
        category2 = Category("Категория 2", "Описание 2", [product3])

        assert Category.product_count == initial_count + 3
        assert Category.product_count == 3


class TestJSONLoading:
    """Тесты загрузки данных из JSON"""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом"""
        Category.category_count = 0
        Category.product_count = 0
        # Создаем тестовый JSON файл перед каждым тестом
        self.json_path = create_test_json_file()

    def teardown_method(self):
        """Удаляем тестовый файл после каждого теста"""
        if os.path.exists(self.json_path):
            os.remove(self.json_path)

    def test_load_data_from_json(self):
        """Тест загрузки данных из JSON файла"""
        categories = load_data_from_json(str(self.json_path))

        assert len(categories) > 0
        assert isinstance(categories[0], Category)
        assert isinstance(categories[0].products[0], Product)

    def test_json_loading_counts(self):
        """Тест корректности подсчетов после загрузки из JSON"""
        categories = load_data_from_json(str(self.json_path))

        total_products = sum(len(category.products) for category in categories)

        assert Category.category_count == len(categories)
        assert Category.product_count == total_products