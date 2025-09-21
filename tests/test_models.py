import pytest
from src.models import Product, Category

@pytest.fixture
def sample_product():
    return Product("Телефон", "Смартфон", 50000.0, 10)

@pytest.fixture
def sample_category(sample_product):
    return Category("Электроника", "Гаджеты", [sample_product])

def test_product_initialization(sample_product):
    assert sample_product.name == "Телефон"
    assert sample_product.description == "Смартфон"
    assert sample_product.price == 50000.0
    assert sample_product.quantity == 10

def test_category_initialization(sample_category, sample_product):
    assert sample_category.name == "Электроника"
    assert sample_category.description == "Гаджеты"
    assert sample_category.products == [sample_product]

def test_category_count():
    initial_count = Category.category_count
    category = Category("Тест", "Тестовая категория")
    assert Category.category_count == initial_count + 1

def test_product_count():
    initial_count = Category.product_count
    product = Product("Тест", "Тест", 100, 1)
    category = Category("Тест", "Тест", [product])
    assert Category.product_count == initial_count + 1
