import json
import os
import sys
from pathlib import Path

import pytest
import src.models

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


def create_test_json_file():
    """Создает тестовый JSON файл в корне проекта."""
    test_data = [
        {
            "name": "Смартфоны",
            "description": "Мобильные телефоны и смартфоны",
            "products": [
                {
                    "name": "Samsung Galaxy S24",
                    "description": "Флагманский смартфон Samsung",
                    "price": 89990.0,
                    "quantity": 15,
                    "efficiency": 2.5,
                    "model": "Galaxy S24",
                    "memory": 256,
                    "color": "черный",
                }
            ],
        }
    ]

    json_path = project_root / "products.json"

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(test_data, f, ensure_ascii=False, indent=2)

    return json_path


class TestProductExceptions:
    """Тесты для обработки исключений в классе Product."""

    def test_product_zero_quantity_raises_value_error(self):
        """Тест что создание продукта с нулевым количеством вызывает ValueError."""
        with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
            src.models.Product("Тестовый товар", "Описание", 1000.0, 0)

    def test_product_positive_quantity_creates_successfully(self):
        """Тест что создание продукта с положительным количеством работает нормально."""
        product = src.models.Product("Тестовый товар", "Описание", 1000.0, 5)
        assert product.quantity == 5
        assert product.name == "Тестовый товар"


class TestCategoryAveragePrice:
    """Тесты для метода average_price в классе Category."""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом."""
        src.models.Category.category_count = 0
        src.models.Category.product_count = 0

    def test_average_price_with_products(self):
        """Тест расчета средней цены при наличии товаров."""
        product1 = src.models.Product("Товар1", "Описание1", 100.0, 3)
        product2 = src.models.Product("Товар2", "Описание2", 200.0, 2)
        category = src.models.Category("Тест", "Описание", [product1, product2])

        average = category.average_price()
        expected_average = (100.0 + 200.0) / 2
        assert average == expected_average

    def test_average_price_single_product(self):
        """Тест расчета средней цены для одного товара."""
        product = src.models.Product("Товар", "Описание", 150.0, 1)
        category = src.models.Category("Тест", "Описание", [product])

        average = category.average_price()
        assert average == 150.0

    def test_average_price_empty_category(self):
        """Тест расчета средней цены для пустой категории."""
        category = src.models.Category("Тест", "Описание")

        average = category.average_price()
        assert average == 0

    def test_average_price_different_prices(self):
        """Тест расчета средней цены для товаров с разными ценами."""
        products = [
            src.models.Product(f"Товар{i}", f"Описание{i}", float(i * 100), 1)
            for i in range(1, 6)
        ]
        category = src.models.Category("Тест", "Описание", products)

        average = category.average_price()
        expected_average = (100 + 200 + 300 + 400 + 500) / 5
        assert average == expected_average


class TestZeroQuantityError:
    """Тесты для пользовательского исключения ZeroQuantityError."""

    def test_zero_quantity_error_inheritance(self):
        """Тест что ZeroQuantityError наследуется от Exception."""
        assert issubclass(src.models.ZeroQuantityError, Exception)

    def test_zero_quantity_error_can_be_raised(self):
        """Тест что ZeroQuantityError можно вызвать."""
        with pytest.raises(src.models.ZeroQuantityError):
            raise src.models.ZeroQuantityError("Тестовое сообщение")

    def test_zero_quantity_error_message(self):
        """Тест сообщения в ZeroQuantityError."""
        try:
            raise src.models.ZeroQuantityError("Товар не может быть с нулевым количеством")
        except src.models.ZeroQuantityError as e:
            assert str(e) == "Товар не может быть с нулевым количеством"


class TestBaseProduct:
    """Тесты для абстрактного базового класса BaseProduct."""

    def test_base_product_is_abstract(self):
        """Тест что BaseProduct является абстрактным классом."""
        with pytest.raises(TypeError):
            src.models.BaseProduct("Тест", "Описание", 100, 1)


class TestPrintObjectMixin:
    """Тесты для миксина PrintObjectMixin."""

    def test_mixin_output_on_creation(self, capsys):
        """Тест вывода информации при создании объекта."""
        product = src.models.Product("Тестовый товар", "Описание", 1000.0, 5)
        captured = capsys.readouterr()

        expected_output = "Создан объект Product('Тестовый товар', 'Описание', 1000.0, 5)"
        assert expected_output in captured.out
        assert product is not None


class TestProduct:
    """Тесты для базового класса Product."""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом."""
        src.models.Category.category_count = 0
        src.models.Category.product_count = 0

    def test_product_initialization(self):
        """Тест корректной инициализации продукта."""
        product = src.models.Product("Телефон", "Смартфон", 50000.0, 10)

        assert product.name == "Телефон"
        assert product.description == "Смартфон"
        assert product.price == 50000.0
        assert product.quantity == 10


class TestCategory:
    """Тесты для класса Category."""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом."""
        src.models.Category.category_count = 0
        src.models.Category.product_count = 0

    def test_category_inheritance(self):
        """Тест что Category наследуется от BaseEntity."""
        category = src.models.Category("Электроника", "Гаджеты")
        assert isinstance(category, src.models.BaseEntity)


class TestJSONLoading:
    """Тесты загрузки данных из JSON."""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом."""
        src.models.Category.category_count = 0
        src.models.Category.product_count = 0
        self.json_path = create_test_json_file()

    def teardown_method(self):
        """Удаляем тестовый файл после каждого теста."""
        if os.path.exists(self.json_path):
            os.remove(self.json_path)

    def test_load_smartphone_from_json(self):
        """Тест загрузки смартфона из JSON."""
        categories = src.models.load_data_from_json(str(self.json_path))

        product = categories[0].get_products_list()[0]
        assert isinstance(product, src.models.Smartphone)
        assert product.name == "Samsung Galaxy S24"
        assert product.model == "Galaxy S24"
        assert product.memory == 256
