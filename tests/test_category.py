import pytest
from src.models import Category, Product


import pytest
from src.models import Product, Category, Smartphone, LawnGrass


@pytest.fixture
def sample_product():
    return Product("Test Product", "Description", 100, 5)


@pytest.fixture
def sample_category():
    return Category("Test Category", "Test Description")


@pytest.fixture
def sample_smartphone():
    return Smartphone("iPhone", "Smartphone", 1000, 10, "High", "14", "128GB", "Black")


@pytest.fixture
def sample_lawn_grass():
    return LawnGrass("Grass", "Lawn grass", 50, 100, "USA", "2 weeks", "Green")