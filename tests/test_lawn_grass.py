import pytest
import src.models


def test_lawn_grass_creation():
    """Тест создания газонной травы."""
    grass = src.models.LawnGrass("Grass", "Lawn grass", 50, 100, "USA", "2 weeks", "Green")
    assert grass.name == "Grass"
    assert grass.country == "USA"
    assert grass.germination_period == "2 weeks"
    assert grass.color == "Green"


def test_lawn_grass_inheritance():
    """Тест наследования газонной травы от Product."""
    from src.models import Product
    grass = src.models.LawnGrass("Grass", "Lawn grass", 50, 100, "USA", "2 weeks", "Green")
    assert isinstance(grass, Product)


def test_lawn_grass_get_additional_info():
    """Тест дополнительной информации газонной травы."""
    grass = src.models.LawnGrass("Grass", "Lawn grass", 50, 100, "USA", "2 weeks", "Green")
    info = grass.get_additional_info()
    assert info["country"] == "USA"
    assert info["germination_period"] == "2 weeks"
    assert info["color"] == "Green"


def test_lawn_grass_addition_same_class():
    """Тест сложения газонной травы одного класса."""
    grass1 = src.models.LawnGrass("Grass1", "Desc", 50, 10, "USA", "2 weeks", "Green")
    grass2 = src.models.LawnGrass("Grass2", "Desc", 70, 5, "Germany", "1 week", "Dark Green")
    result = grass1 + grass2
    assert result == 50 * 10 + 70 * 5