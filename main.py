from src.models import Product, Category, load_data_from_json
from pathlib import Path


def demonstrate_str_methods():
    """Демонстрация строковых представлений"""
    print("=== Демонстрация строковых представлений ===\n")

    # Создание продуктов
    phone = Product("iPhone 15", "Смартфон Apple", 99990.0, 5)
    laptop = Product("MacBook Pro", "Ноутбук Apple", 199990.0, 3)

    print("Строковое представление продуктов:")
    print(f"Продукт 1: {phone}")
    print(f"Продукт 2: {laptop}")

    # Создание категории
    electronics = Category("Электроника", "Техника Apple", [phone, laptop])

    print(f"\nСтроковое представление категории: {electronics}")
    print(f"Общее количество товаров: {electronics.get_total_quantity()}")


def demonstrate_addition_method():
    """Демонстрация сложения продуктов"""
    print("\n=== Демонстрация сложения продуктов ===\n")

    # Создание продуктов
    product1 = Product("Телефон", "Смартфон", 50000.0, 10)
    product2 = Product("Ноутбук", "Игровой ноутбук", 100000.0, 5)

    print(f"Продукт 1: {product1}")
    print(f"Продукт 2: {product2}")

    # Сложение продуктов
    total_value = product1 + product2
    print(f"\nСуммарная стоимость товаров на складе: {total_value} руб.")

    # Демонстрация расчета
    calculation = f"({product1.price} × {product1.quantity}) + ({product2.price} × {product2.quantity}) = {total_value}"
    print(f"Расчет: {calculation}")


def demonstrate_json_loading():
    """Демонстрация загрузки из JSON"""
    print("\n=== Демонстрация загрузки из JSON ===\n")

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
        print(f"Категория: {category}")
        print("Товары:")
        print(category.products)
        print()


def demonstrate_all_features():
    """Демонстрация всех новых функций"""
    print("=" * 50)
    print("ДЕМОНСТРАЦИЯ МАГИЧЕСКИХ МЕТОДОВ")
    print("=" * 50)

    demonstrate_str_methods()
    demonstrate_addition_method()
    demonstrate_json_loading()


if __name__ == "__main__":
    demonstrate_all_features()