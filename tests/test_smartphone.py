import pytest
from src.models import Smartphone


def test_smartphone_creation():
    """Тест создания смартфона."""
    phone = Smartphone("iPhone", "Smartphone", 1000, 10, "High", "14", "128GB", "Black")
    assert phone.name == "iPhone"
    assert phone.performance == "High"
    assert phone.model == "14"
    assert phone.memory == "128GB"
    assert phone.color == "Black"


def test_smartphone_inheritance():
    """Тест наследования смартфона от Product."""
    from src.models import Product
    phone = Smartphone("iPhone", "Smartphone", 1000, 10, "High", "14", "128GB", "Black")
    assert isinstance(phone, Product)


def test_smartphone_get_additional_info():
    """Тест дополнительной информации смартфона."""
    phone = Smartphone("iPhone", "Smartphone", 1000, 10, "High", "14", "128GB", "Black")
    info = phone.get_additional_info()
    assert info["performance"] == "High"
    assert info["model"] == "14"
    assert info["memory"] == "128GB"
    assert info["color"] == "Black"


def test_smartphone_addition_same_class():
    """Тест сложения смартфонов одного класса."""
    phone1 = Smartphone("Phone1", "Desc", 1000, 2, "High", "X", "128GB", "Black")
    phone2 = Smartphone("Phone2", "Desc", 800, 3, "Medium", "Y", "256GB", "White")
    result = phone1 + phone2
    assert result == 1000 * 2 + 800 * 3