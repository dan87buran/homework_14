import pytest
import sys
import os
import json
from pathlib import Path
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


class TestBaseProduct:
    """Тесты для абстрактного базового класса BaseProduct."""

    def test_base_product_is_abstract(self):
        """Тест что BaseProduct является абстрактным классом."""
        with pytest.raises(TypeError):
            src.models.BaseProduct("Тест", "Описание", 100, 1)

    def test_product_inherits_from_base_product(self):
        """Тест что Product наследуется от BaseProduct."""
        product = src.models.Product("Тест", "Описание", 100, 1)
        assert isinstance(product, src.models.BaseProduct)


class TestPrintObjectMixin:
    """Тесты для миксина PrintObjectMixin."""

    def test_mixin_output_on_creation(self, capsys):
        """Тест вывода информации при создании объекта."""
        product = src.models.Product("Тестовый товар", "Описание", 1000.0, 5)
        captured = capsys.readouterr()

        expected_output = "Создан объект Product('Тестовый товар', 'Описание', 1000.0, 5)"
        assert expected_output in captured.out
        # Используем переменную product, чтобы избежать F841
        assert product is not None

    def test_mixin_with_smartphone(self, capsys):
        """Тест миксина со смартфоном."""
        smartphone = src.models.Smartphone(
            name="Тест",
            description="Описание",
            price=1000.0,
            quantity=1,
            efficiency=2.0,
            model="Модель",
            memory=128,
            color="черный",
        )
        captured = capsys.readouterr()

        assert "Создан объект Smartphone(" in captured.out
        assert "'Тест'" in captured.out
        # Используем переменную smartphone, чтобы избежать F841
        assert smartphone is not None


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

    def test_product_str_representation(self):
        """Тест строкового представления продукта."""
        product = src.models.Product("Телефон", "Смартфон", 50000.0, 10)
        expected_str = "Телефон, 50000.0 руб. Остаток: 10 шт."
        assert str(product) == expected_str


class TestSmartphone:
    """Тесты для класса Smartphone."""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом."""
        src.models.Category.category_count = 0
        src.models.Category.product_count = 0

    def test_smartphone_initialization(self):
        """Тест корректной инициализации смартфона."""
        smartphone = src.models.Smartphone(
            name="iPhone 15",
            description="Смартфон Apple",
            price=99990.0,
            quantity=5,
            efficiency=3.2,
            model="15 Pro",
            memory=512,
            color="синий",
        )

        assert smartphone.name == "iPhone 15"
        assert smartphone.description == "Смартфон Apple"
        assert smartphone.price == 99990.0
        assert smartphone.quantity == 5
        assert smartphone.efficiency == 3.2
        assert smartphone.model == "15 Pro"
        assert smartphone.memory == 512
        assert smartphone.color == "синий"

    def test_smartphone_inheritance(self):
        """Тест что Smartphone наследуется от Product и BaseProduct."""
        smartphone = src.models.Smartphone("Тест", "Тест", 1000, 1, 1.0, "Модель", 128, "черный")
        assert isinstance(smartphone, src.models.Product)
        assert isinstance(smartphone, src.models.BaseProduct)


class TestLawnGrass:
    """Тесты для класса LawnGrass."""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом."""
        src.models.Category.category_count = 0
        src.models.Category.product_count = 0

    def test_lawn_grass_initialization(self):
        """Тест корректной инициализации газонной травы."""
        lawn_grass = src.models.LawnGrass(
            name="Газонная трава Премиум",
            description="Качественная газонная трава",
            price=1500.0,
            quantity=100,
            country="Германия",
            germination_period=14,
            color="зеленый",
        )

        assert lawn_grass.name == "Газонная трава Премиум"
        assert lawn_grass.description == "Качественная газонная трава"
        assert lawn_grass.price == 1500.0
        assert lawn_grass.quantity == 100
        assert lawn_grass.country == "Германия"
        assert lawn_grass.germination_period == 14
        assert lawn_grass.color == "зеленый"

    def test_lawn_grass_inheritance(self):
        """Тест что LawnGrass наследуется от Product и BaseProduct."""
        lawn_grass = src.models.LawnGrass("Трава", "Описание", 1000, 1, "Россия", 10, "зеленый")
        assert isinstance(lawn_grass, src.models.Product)
        assert isinstance(lawn_grass, src.models.BaseProduct)


class TestOrder:
    """Тесты для класса Order."""

    def test_order_initialization(self):
        """Тест корректной инициализации заказа."""
        product = src.models.Product("Телефон", "Смартфон", 50000.0, 10)
        order = src.models.Order(product, 2)

        assert order.product == product
        assert order.quantity == 2
        assert order.total_price == 100000.0
        assert "Заказ Телефон" in order.name
        assert "Заказ товара Телефон" in order.description

    def test_order_str_representation(self):
        """Тест строкового представления заказа."""
        product = src.models.Product("Телефон", "Смартфон", 50000.0, 10)
        order = src.models.Order(product, 2)

        order_str = str(order)
        assert "Заказ: Телефон" in order_str
        assert "Количество: 2" in order_str
        assert "Итоговая стоимость: 100000.0 руб." in order_str

    def test_order_inheritance(self):
        """Тест что Order наследуется от BaseEntity."""
        product = src.models.Product("Тест", "Описание", 100, 1)
        order = src.models.Order(product, 1)
        assert isinstance(order, src.models.BaseEntity)


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

    def test_category_str_representation(self):
        """Тест строкового представления категории."""
        product = src.models.Product("Телефон", "Смартфон", 50000.0, 10)
        category = src.models.Category("Электроника", "Гаджеты", [product])

        expected_str = "Электроника, количество продуктов: 10 шт."
        assert str(category) == expected_str


class TestProductAddition:
    """Тесты для сложения продуктов."""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом."""
        src.models.Category.category_count = 0
        src.models.Category.product_count = 0

    def test_add_same_product_types(self):
        """Тест сложения товаров одного типа."""
        product1 = src.models.Product("Товар1", "Описание1", 100.0, 3)
        product2 = src.models.Product("Товар2", "Описание2", 200.0, 2)

        total_value = product1 + product2
        expected_value = (100.0 * 3) + (200.0 * 2)
        assert total_value == expected_value

    def test_add_different_product_types(self):
        """Тест сложения товаров разных типов (должна быть ошибка)."""
        smartphone = src.models.Smartphone("Смартфон", "Описание", 50000.0, 2, 2.5, "Модель", 128, "черный")
        lawn_grass = src.models.LawnGrass("Трава", "Описание", 1000.0, 10, "Россия", 14, "зеленый")

        with pytest.raises(TypeError, match="Нельзя складывать товары разных типов"):
            smartphone + lawn_grass


class TestCategoryAddProduct:
    """Тесты для метода add_product в категории."""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом."""
        src.models.Category.category_count = 0
        src.models.Category.product_count = 0

    def test_add_product_to_category(self):
        """Тест добавления продукта в категорию."""
        category = src.models.Category("Электроника", "Гаджеты")
        product = src.models.Product("Телефон", "Смартфон", 50000.0, 10)

        initial_count = src.models.Category.product_count
        category.add_product(product)

        assert src.models.Category.product_count == initial_count + 1
        assert len(category.get_products_list()) == 1

    def test_add_invalid_type_to_category(self):
        """Тест добавления неверного типа в категорию (должна быть ошибка)."""
        category = src.models.Category("Электроника", "Гаджеты")

        with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product или его наследников"):
            category.add_product("не продукт")


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
