from src.models import Product, Category, load_data_from_json
from pathlib import Path


def demonstrate_private_attributes():
    """Демонстрация работы с приватными атрибутами"""
    print("=== Демонстрация приватных атрибутов и методов ===\n")

    # Сброс счетчиков
    Category.category_count = 0
    Category.product_count = 0

    # Создание продуктов
    phone = Product("iPhone 15", "Смартфон Apple", 99990.0, 5)
    laptop = Product("MacBook Pro", "Ноутбук Apple", 199990.0, 3)

    # Создание категории и добавление продуктов через метод
    electronics = Category("Электроника", "Техника Apple")
    electronics.add_product(phone)
    electronics.add_product(laptop)

    print("Демонстрация геттера products:")
    print(electronics.products)

    print(f"\nОбщее количество категорий: {Category.category_count}")
    print(f"Общее количество товаров: {Category.product_count}")


def demonstrate_price_validation():
    """Демонстрация валидации цены"""
    print("\n=== Демонстрация валидации цены ===\n")

    product = Product("Тестовый товар", "Пример", 1000.0, 10)
    print(f"Исходная цена: {product.price}")

    # Попытка установить отрицательную цену
    print("Пытаемся установить отрицательную цену...")
    product.price = -500.0
    print(f"Цена после попытки установки отрицательного значения: {product.price}")

    # Установка корректной цены
    product.price = 1500.0
    print(f"Цена после установки корректного значения: {product.price}")


def demonstrate_class_method():
    """Демонстрация класс-метода"""
    print("\n=== Демонстрация класс-метода new_product ===\n")

    product_data = {
        "name": "Созданный через класс-метод",
        "description": "Товар созданный из словаря",
        "price": 50000.0,
        "quantity": 7
    }

    product = Product.new_product(product_data)
    print(f"Создан продукт: {product.name}")
    print(f"Цена: {product.price} руб.")
    print(f"В наличии: {product.quantity} шт.")


def demonstrate_json_loading():
    """Демонстрация загрузки из JSON"""
    print("\n=== Демонстрация загрузки из JSON ===\n")

    # Сброс счетчиков
    Category.category_count = 0
    Category.product_count = 0

    # Проверяем существование файла
    json_path = Path("products.json")
    if not json_path.exists():
        print("Файл products.json не найден")
        return

    categories = load_data_from_json("products.json")

    if not categories:
        print("Не удалось загрузить данные")
        return

    for category in categories:
        print(f"Категория: {category.name}")
        print(f"Описание: {category.description}")
        print("Товары:")
        print(category.products)
        print()


if __name__ == "__main__":
    demonstrate_private_attributes()
    demonstrate_price_validation()
    demonstrate_class_method()
    demonstrate_json_loading()