import pytest
from src.models import BaseProduct


def test_base_product_is_abstract():
    """Тест, что нельзя создать экземпляр абстрактного класса."""
    with pytest.raises(TypeError):
        BaseProduct("Test", "Description", 100, 5)


def test_base_product_has_abstract_methods():
    """Тест, что абстрактный класс имеет необходимые методы."""
    # Проверяем, что методы существуют как абстрактные
    assert hasattr(BaseProduct, 'get_additional_info')
    # Проверяем, что метод является абстрактным
    import inspect
    assert inspect.isabstract(BaseProduct)