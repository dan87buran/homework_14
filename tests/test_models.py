import pytest
import sys
import os
import json
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.models import Product, Smartphone, LawnGrass, Category, load_data_from_json


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
                    "quantity": 15,
                    "efficiency": 2.5,
                    "model": "Galaxy S24",
                    "memory": 256,
                    "color": "черный"
                }
            ]
        }
    ]

    json_path = project_root / "products.json"

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(test_data, f, ensure_ascii=False, indent=2)

    return json_path


class TestProduct:
    """Тесты для базового класса Product"""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом"""
        Category.category_count = 0
        Category.product_count = 0

    def test_product_initialization(self):
        """Тест корректной инициализации продукта"""
        product = Product("Телефон", "Смартфон", 50000.0, 10)

        assert product.name == "Телефон"
        assert product.description == "Смартфон"
        assert product.price == 50000.0
        assert product.quantity == 10


class TestSmartphone:
    """Тесты для класса Smartphone"""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом"""
        Category.category_count = 0
        Category.product_count = 0

    def test_smartphone_initialization(self):
        """Тест корректной инициализации смартфона"""
        smartphone = Smartphone(
            name="iPhone 15",
            description="Смартфон Apple",
            price=99990.0,
            quantity=5,
            efficiency=3.2,
            model="15 Pro",
            memory=512,
            color="синий"
        )

        # Проверяем наследование от Product
        assert smartphone.name == "iPhone 15"
        assert smartphone.description == "Смартфон Apple"
        assert smartphone.price == 99990.0
        assert smartphone.quantity == 5

        # Проверяем специфичные атрибуты
        assert smartphone.efficiency == 3.2
        assert smartphone.model == "15 Pro"
        assert smartphone.memory == 512
        assert smartphone.color == "синий"

    def test_smartphone_inheritance(self):
        """Тест что Smartphone наследуется от Product"""
        smartphone = Smartphone("Тест", "Тест", 1000, 1, 1.0, "Модель", 128, "черный")
        assert isinstance(smartphone, Product)

    def test_smartphone_str_representation(self):
        """Тест строкового представления смартфона"""
        smartphone = Smartphone(
            name="iPhone",
            description="Смартфон",
            price=99990.0,
            quantity=5,
            efficiency=3.2,
            model="15 Pro",
            memory=512,
            color="синий"
        )

        smartphone_str = str(smartphone)
        assert "iPhone 15 Pro" in smartphone_str
        assert "99990.0 руб." in smartphone_str
        assert "5 шт." in smartphone_str
        assert "512ГБ" in smartphone_str
        assert "синий" in smartphone_str


class TestLawnGrass:
    """Тесты для класса LawnGrass"""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом"""
        Category.category_count = 0
        Category.product_count = 0

    def test_lawn_grass_initialization(self):
        """Тест корректной инициализации газонной травы"""
        lawn_grass = LawnGrass(
            name="Газонная трава Премиум",
            description="Качественная газонная трава",
            price=1500.0,
            quantity=100,
            country="Германия",
            germination_period=14,
            color="зеленый"
        )

        # Проверяем наследование от Product
        assert lawn_grass.name == "Газонная трава Премиум"
        assert lawn_grass.description == "Качественная газонная трава"
        assert lawn_grass.price == 1500.0
        assert lawn_grass.quantity == 100

        # Проверяем специфичные атрибуты
        assert lawn_grass.country == "Германия"
        assert lawn_grass.germination_period == 14
        assert lawn_grass.color == "зеленый"

    def test_lawn_grass_inheritance(self):
        """Тест что LawnGrass наследуется от Product"""
        lawn_grass = LawnGrass("Трава", "Описание", 1000, 1, "Россия", 10, "зеленый")
        assert isinstance(lawn_grass, Product)

    def test_lawn_grass_str_representation(self):
        """Тест строкового представления газонной травы"""
        lawn_grass = LawnGrass(
            name="Газонная трава",
            description="Качественная трава",
            price=1500.0,
            quantity=100,
            country="Германия",
            germination_period=14,
            color="зеленый"
        )

        lawn_grass_str = str(lawn_grass)
        assert "Газонная трава" in lawn_grass_str
        assert "1500.0 руб." in lawn_grass_str
        assert "100 шт." in lawn_grass_str
        assert "Германия" in lawn_grass_str
        assert "14 дней" in lawn_grass_str


class TestProductAddition:
    """Тесты для сложения продуктов"""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом"""
        Category.category_count = 0
        Category.product_count = 0

    def test_add_same_product_types(self):
        """Тест сложения товаров одного типа"""
        product1 = Product("Товар1", "Описание1", 100.0, 3)
        product2 = Product("Товар2", "Описание2", 200.0, 2)

        total_value = product1 + product2
        expected_value = (100.0 * 3) + (200.0 * 2)
        assert total_value == expected_value

    def test_add_smartphones(self):
        """Тест сложения смартфонов"""
        smartphone1 = Smartphone("Смартфон1", "Описание1", 50000.0, 2, 2.5, "Модель1", 128, "черный")
        smartphone2 = Smartphone("Смартфон2", "Описание2", 70000.0, 3, 3.0, "Модель2", 256, "белый")

        total_value = smartphone1 + smartphone2
        expected_value = (50000.0 * 2) + (70000.0 * 3)
        assert total_value == expected_value

    def test_add_lawn_grass(self):
        """Тест сложения газонной травы"""
        grass1 = LawnGrass("Трава1", "Описание1", 1000.0, 10, "Россия", 14, "зеленый")
        grass2 = LawnGrass("Трава2", "Описание2", 1500.0, 5, "Германия", 10, "темно-зеленый")

        total_value = grass1 + grass2
        expected_value = (1000.0 * 10) + (1500.0 * 5)
        assert total_value == expected_value

    def test_add_different_product_types(self):
        """Тест сложения товаров разных типов (должна быть ошибка)"""
        smartphone = Smartphone("Смартфон", "Описание", 50000.0, 2, 2.5, "Модель", 128, "черный")
        lawn_grass = LawnGrass("Трава", "Описание", 1000.0, 10, "Россия", 14, "зеленый")

        with pytest.raises(TypeError, match="Нельзя складывать товары разных типов"):
            smartphone + lawn_grass

    def test_add_product_with_smartphone(self):
        """Тест сложения базового продукта со смартфоном (должна быть ошибка)"""
        product = Product("Товар", "Описание", 100.0, 3)
        smartphone = Smartphone("Смартфон", "Описание", 50000.0, 2, 2.5, "Модель", 128, "черный")

        with pytest.raises(TypeError, match="Нельзя складывать товары разных типов"):
            product + smartphone


class TestCategoryAddProduct:
    """Тесты для метода add_product в категории"""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом"""
        Category.category_count = 0
        Category.product_count = 0

    def test_add_product_to_category(self):
        """Тест добавления продукта в категорию"""
        category = Category("Электроника", "Гаджеты")
        product = Product("Телефон", "Смартфон", 50000.0, 10)

        initial_count = Category.product_count
        category.add_product(product)

        assert Category.product_count == initial_count + 1
        assert len(category.get_products_list()) == 1

    def test_add_smartphone_to_category(self):
        """Тест добавления смартфона в категорию"""
        category = Category("Электроника", "Гаджеты")
        smartphone = Smartphone("Смартфон", "Описание", 50000.0, 2, 2.5, "Модель", 128, "черный")

        category.add_product(smartphone)
        assert len(category.get_products_list()) == 1
        assert isinstance(category.get_products_list()[0], Smartphone)

    def test_add_lawn_grass_to_category(self):
        """Тест добавления газонной травы в категорию"""
        category = Category("Сад", "Товары для сада")
        lawn_grass = LawnGrass("Трава", "Описание", 1000.0, 10, "Россия", 14, "зеленый")

        category.add_product(lawn_grass)
        assert len(category.get_products_list()) == 1
        assert isinstance(category.get_products_list()[0], LawnGrass)

    def test_add_invalid_type_to_category(self):
        """Тест добавления неверного типа в категорию (должна быть ошибка)"""
        category = Category("Электроника", "Гаджеты")

        with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product или его наследников"):
            category.add_product("не продукт")

    def test_add_dict_to_category(self):
        """Тест добавления словаря в категорию (должна быть ошибка)"""
        category = Category("Электроника", "Гаджеты")

        with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product или его наследников"):
            category.add_product({"name": "тест", "price": 100})


class TestJSONLoading:
    """Тесты загрузки данных из JSON"""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом"""
        Category.category_count = 0
        Category.product_count = 0
        self.json_path = create_test_json_file()

    def teardown_method(self):
        """Удаляем тестовый файл после каждого теста"""
        if os.path.exists(self.json_path):
            os.remove(self.json_path)

    def test_load_smartphone_from_json(self):
        """Тест загрузки смартфона из JSON"""
        categories = load_data_from_json(str(self.json_path))

        product = categories[0].get_products_list()[0]
        assert isinstance(product, Smartphone)
        assert product.name == "Samsung Galaxy S24"
        assert product.model == "Galaxy S24"
        assert product.memory == 256