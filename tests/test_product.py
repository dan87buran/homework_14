import pytest
from src.models import Product


def test_product_creation():
    """Тест создания продукта."""
    product = Product("Test Product", "Description", 100, 5)
    assert product.name == "Test Product"
    assert product.description == "Description"
    assert product.price == 100
    assert product.quantity == 5


def test_product_creation_with_zero_quantity():
    """Тест создания продукта с нулевым количеством."""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Test Product", "Description", 100, 0)


def test_product_creation_with_negative_price():
    """Тест создания продукта с отрицательной ценой."""
    # Если у вас есть валидация цены, добавьте соответствующий тест
    product = Product("Test Product", "Description", -50, 5)
    assert product.price == -50


def test_product_str_representation():
    """Тест строкового представления продукта."""
    product = Product("Test Product", "Description", 100, 5)
    assert "Test Product" in str(product)
    assert "100" in str(product)


def test_product_repr_representation():
    """Тест repr представления продукта."""
    product = Product("Test Product", "Description", 100, 5)
    assert "Product" in repr(product)
    assert "Test Product" in repr(product)


def test_product_addition_same_class():
    """Тест сложения продуктов одного класса."""
    product1 = Product("Product1", "Desc", 100, 2)
    product2 = Product("Product2", "Desc", 200, 3)
    result = product1 + product2
    assert result == 100 * 2 + 200 * 3


def test_product_addition_different_classes():
    """Тест, что нельзя складывать продукты разных классов."""
    product = Product("Product", "Desc", 100, 2)

    # Импортируем здесь, чтобы избежать циклических импортов
    from src.models import Smartphone
    phone = Smartphone("Phone", "Desc", 1000, 1, "High", "X", "128GB", "Black")

    with pytest.raises(TypeError):
        product + phone


def test_product_get_additional_info():
    """Тест получения дополнительной информации о продукте."""
    product = Product("Test Product", "Description", 100, 5)
    info = product.get_additional_info()
    assert info == {"type": "basic_product"}