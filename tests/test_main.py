import os
import sys
import pytest

# Добавляем путь к src в sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from main import Product, Category, load_data_from_json


def test_product_init():
    product = Product("Телефон", "Смартфон", 50000.0, 10)
    assert product.name == "Телефон"
    assert product.description == "Смартфон"
    assert product.price == 50000.0
    assert product.quantity == 10


def test_category_init():
    products = [Product("Телефон", "Смартфон", 50000.0, 10)]
    category = Category("Электроника", "Гаджеты", products)
    assert category.name == "Электроника"
    assert category.description == "Гаджеты"
    assert len(category.products) == 1


def test_category_counters():
    Category.total_categories = 0
    Category.total_products = 0

    products1 = [Product("Товар1", "Описание1", 100.0, 5)]
    category1 = Category("Категория1", "Описание", products1)

    products2 = [
        Product("Товар2", "Описание2", 200.0, 3),
        Product("Товар3", "Описание3", 300.0, 7)
    ]
    category2 = Category("Категория2", "Описание", products2)

    assert Category.total_categories == 2
    assert Category.total_products == 3


def test_json_loading():
    # Получаем путь к корню проекта
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'products.json')

    categories = load_data_from_json(file_path)
    assert len(categories) > 0
    for category in categories:
        assert isinstance(category, Category)
        for product in category.products:
            assert isinstance(product, Product)